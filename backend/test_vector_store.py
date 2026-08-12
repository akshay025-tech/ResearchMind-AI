from app.services.pdf_service import extract_pages_from_pdf
from app.services.chunk_service import chunk_pages
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import add_documents


PDF_PATH = "sample.pdf"


# 1. Extract pages
pages = extract_pages_from_pdf(PDF_PATH)


# 2. Create chunks
chunks = chunk_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
)


# 3. Extract chunk text
texts = [chunk["text"] for chunk in chunks]


# 4. Generate embeddings
embeddings = generate_embeddings(texts)


# 5. Generate IDs
ids = [
    f"finrobot_chunk_{chunk['chunk_id']}"
    for chunk in chunks
]


# 6. Create metadata
metadatas = [
    {
        "paper": "FinRobot",
        "page": chunk["page_number"],
        "chunk_id": chunk["chunk_id"]
    }
    for chunk in chunks
]


# 7. Store everything in ChromaDB
add_documents(
    ids=ids,
    documents=texts,
    embeddings=embeddings,
    metadatas=metadatas
)


print("=" * 60)
print("VECTOR DATABASE")
print("=" * 60)

print("Pages:", len(pages))
print("Chunks:", len(chunks))
print("Embeddings:", embeddings.shape)

print("\nDocuments successfully stored in ChromaDB.")