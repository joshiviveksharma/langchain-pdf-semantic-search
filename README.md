# LangChain PDF Semantic Search

A semantic search API built using LangChain, ChromaDB, HuggingFace embeddings, and FastAPI.

## Features
- Upload and process PDF documents
- Generate embeddings using HuggingFace
- Store vectors in ChromaDB
- Perform semantic similarity search
- FastAPI REST API support
- Swagger UI support

---

## Tech Stack
- Python
- LangChain
- FastAPI
- ChromaDB
- HuggingFace Embeddings
- PyPDF
- Uvicorn

---

## Project Structure

```bash
.
├── app.py
├── ingest.py
├── requirements.txt
├── sample.pdf
├── chroma_db/
├── results.json
├── README.md
└── utils/
    └── config.py
```

---

## Installation

```bash
git clone https://github.com/joshiviveksharma/langchain-pdf-semantic-search.git

cd langchain-pdf-semantic-search

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Generate Embeddings

```bash
python3 ingest.py --file sample.pdf
```

---

## Run FastAPI Server

```bash
uvicorn app:app --reload
```

Server URL:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

## Query Example

POST Endpoint:

```bash
/query
```

Request Body:

```json
{
  "query": "Python skills",
  "top_k": 3
}
```

---

## Author

Joshi Vivek Sharma

GitHub:
https://github.com/joshiviveksharma
