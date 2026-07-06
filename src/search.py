import os 
from dotenv import load_dotenv
from src.vectorstore import FaissVectorStore
from langchain_groq import ChatGroq
from src.data_loader import load_all_documents

load_dotenv()

class RagSearch:
    def __init__(self,persist_dir:str="faiss_store",embedding_model: str = "all-MiniLM-L6-v2",llm_model:str="llama-3.3-70b-versatile"):
        self.vector_store = FaissVectorStore(persist_dir, embedding_model)
        #load or build vectorstore
        faiss_path=os.path.join(persist_dir,"faiss.index")
        meta_path=os.path.join(persist_dir,"metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            documents=load_all_documents("data")
            self.vector_store.build_documents(documents)
        else:
            self.vector_store.load()
        groq_api_key=os.getenv("groq_api_key")
        self.llm = ChatGroq(model=llm_model,groq_api_key=groq_api_key, temperature=0)
        print(f"[INFO] loaded LLM model:{llm_model}")

    def search_sum(self,query:str,top_k:int=5)->str:
        results=self.vector_store.query(query,top_k)
        texts=[r["metadata"].get("text","") for r in results if r["metadata"]]
        context="\n\n".join(texts)
        if not context:
            return "no relevant content found"
        prompt=f"summarize the following context:{context} for the query:{query} and give summary:"
        response=self.llm.invoke([prompt])
        return response.content
        