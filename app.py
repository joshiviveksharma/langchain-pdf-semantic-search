from fastapi import FastAPI
from pydantic import BaseModel

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

@app.post("/query")
def query_docs(request: QueryRequest):

    results = vectorstore.similarity_search_with_score(
        request.query,
        k=request.top_k
    )

    response = []

    for doc, score in results:
        response.append({
            "chunk_text": doc.page_content,
            "page_number": doc.metadata.get("page", "N/A"),
            "score": float(score)
        })

    return response