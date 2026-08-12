from app.services.embedding_service import generate_embeddings

texts = [
    "Large language models understand natural language.",
    "LLMs process human language.",
    "The stock market increased today."
]

embeddings = generate_embeddings(texts)

similarity_1_2 = embeddings[0] @ embeddings[1]
similarity_1_3 = embeddings[0] @ embeddings[2]

print("=" * 60)
print("SEMANTIC SIMILARITY")
print("=" * 60)

print("Sentence 1 vs Sentence 2:", similarity_1_2)
print("Sentence 1 vs Sentence 3:", similarity_1_3)