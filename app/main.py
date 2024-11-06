from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Initialize the sentence-transformers model
model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory document store (this could be ChromaDB in your case)
documents = []

# Endpoint to ingest documents
@app.post("/ingest")
async def ingest_file(file: UploadFile):
    content = await file.read()
    text = content.decode("utf-8")  # Assuming text files; adapt for PDF/DOCX
    documents.append(text)
    return {"message": f"File '{file.filename}' uploaded successfully!"}

# Endpoint to query documents
@app.get("/query")
async def query_documents(q: str):
    # Here you would normally perform a search or retrieval from ChromaDB
    query_embedding = model.encode([q])
    results = []
    for doc in documents:
        doc_embedding = model.encode([doc])
        similarity = cosine_similarity(query_embedding, doc_embedding)  # You would need to implement similarity calculation
        if similarity > 0.7:  # Example threshold
            results.append({"text": doc})
    return {"query": q, "results": results}

def cosine_similarity(a, b):
    # Implement cosine similarity calculation (or use an existing library)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
