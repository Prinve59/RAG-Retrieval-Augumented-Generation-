from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
if __name__=="__main__":
    doc=load_all_documents("data")
    vec_store=FaissVectorStore();
    emb=vec_store.build_documents(doc)
    vec_store.load()
    print(vec_store.query("The Pencil Maker took the pencil aside and said what",top_k=3))