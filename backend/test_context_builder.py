from app.services.embedding_service import generate_embeddings
from app.services.vector_store import search_documents
from app.services.context_builder import build_context


query = "What are the four major layers of FinRobot?"

# 1. Convert query into embedding
query_embedding = generate_embeddings([query])[0]

# 2. Retrieve relevant chunks
results = search_documents(
    query_embedding=query_embedding,
    top_k=5
)

# 3. Build LLM-ready context
context, sources = build_context(results)


print("=" * 60)
print("CONTEXT BUILDER TEST")
print("=" * 60)

print("\nGENERATED CONTEXT")
print("=" * 60)
print(context)

print("\n")
print("=" * 60)
print("STRUCTURED SOURCES")
print("=" * 60)

for source in sources:
    print(source)

print("\nContext Builder completed successfully.")