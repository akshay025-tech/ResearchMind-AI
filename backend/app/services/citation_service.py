def format_citations(sources):
    """
    Convert structured source metadata into readable citations.
    """

    citations = []

    for source in sources:
        citation = (
            f"[{source['source_id']}] "
            f"{source['paper']}, "
            f"Page {source['page']}, "
            f"Chunk {source['chunk_id']}"
        )

        citations.append(citation)

    return citations