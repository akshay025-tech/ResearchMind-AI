from app.services.embedding_service import generate_embeddings
from app.services.vector_store import search_documents


query = "What are the four major layers of FinRobot?"


# Convert the question into an embedding
query_embedding = generate_embeddings([query])[0]


# Search ChromaDB
results = search_documents(
    query_embedding=query_embedding,
    top_k=5
)


print("=" * 60)
print("RETRIEVAL RESULTS")
print("=" * 60)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1
):

    print("\n" + "=" * 60)
    print(f"RESULT {i}")
    print("=" * 60)

    print("Distance:", distance)
    print("Metadata:", metadata)

    print("\nText:")
    print(document[:1000])