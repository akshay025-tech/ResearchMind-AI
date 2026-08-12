from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embeddings(texts: list[str]):
    """
    Generate embeddings for a list of text strings.

    Args:
        texts: List of text strings.

    Returns:
        Embeddings as a numerical array.
    """

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings