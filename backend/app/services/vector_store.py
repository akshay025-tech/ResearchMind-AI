import chromadb


CHROMA_PATH = "chroma_db"

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name="research_papers"
)


def add_documents(
    ids: list[str],
    documents: list[str],
    embeddings,
    metadatas: list[dict]
):
    """
    Store document chunks, embeddings, and metadata
    in ChromaDB.
    """

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


def search_documents(
    query_embedding,
    top_k: int = 5
):
    """
    Search the vector database using a query embedding.
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results