from app.services.embedding_service import generate_embeddings


texts = [
    "Large language models understand natural language.",
    "LLMs process human language.",
    "The stock market increased today."
]


embeddings = generate_embeddings(texts)


print("=" * 60)
print("EMBEDDING INFORMATION")
print("=" * 60)

print("Number of texts:", len(texts))
print("Embedding shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])