from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class CourseSearch:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        self.vector_store = Chroma(
            persist_directory="data/chroma_db",
            embedding_function=self.embeddings
        )
        
    def search(self, query: str, k: int = 3):
        results = self.vector_store.similarity_search(query, k=k)
        return results 