from app.services.embedding_service import generate_embeddings
from app.services.vector_store import search_documents
from app.services.context_builder import build_context
from app.services.llm_service import generate_answer


question = "What are the four major layers of FinRobot?"

# 1. Convert question into embedding
query_embedding = generate_embeddings([question])[0]

# 2. Retrieve relevant chunks
results = search_documents(
    query_embedding=query_embedding,
    top_k=5
)

# 3. Build context from retrieved chunks
context, sources = build_context(results)

# 4. Generate grounded answer
answer = generate_answer(
    question=question,
    context=context
)

print("=" * 60)
print("RESEARCHMIND RAG TEST")
print("=" * 60)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)

print("\nSOURCES:")
for source in sources:
    print(source)

print("\n" + "=" * 60)
print("RAG GENERATION COMPLETED")
print("=" * 60)