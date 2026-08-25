def build_context(results):
    """
    Convert raw ChromaDB retrieval results
    into LLM-ready context and structured sources.
    """

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    context_parts = []
    sources = []

    for index, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1
    ):
        paper = metadata.get("paper", "Unknown")
        page = metadata.get("page", "Unknown")
        chunk_id = metadata.get("chunk_id", "Unknown")

        context_parts.append(
            f"[Source {index}]\n"
            f"Paper: {paper}\n"
            f"Page: {page}\n"
            f"Chunk: {chunk_id}\n\n"
            f"{document}"
        )

        sources.append(
            {
                "source_id": index,
                "paper": paper,
                "page": page,
                "chunk_id": chunk_id,
                "distance": distance
            }
        )

    context = "\n\n".join(context_parts)

    return context, sources