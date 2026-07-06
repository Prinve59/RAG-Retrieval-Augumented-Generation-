from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RagSearch
if __name__=="__main__":
    rag=RagSearch()
    print(rag.search_sum(query="The Pencil Maker took the pencil aside and said what",top_k=3))