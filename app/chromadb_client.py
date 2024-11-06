from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

class ChromaDBClient:
    def __init__(self):
        self.client = PersistentClient()
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def ingest_document(self, doc_name, content):
        embedding = self.model.encode(content.decode())
        self.client.add_document(name=doc_name, embedding=embedding)

    def query_document(self, query):
        query_embedding = self.model.encode(query)
        results = self.client.query(query_embedding)
        return results
