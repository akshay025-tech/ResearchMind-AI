def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[dict]:
    """
    Split page-level text into overlapping chunks while
    preserving page metadata.

    Args:
        pages: List of page dictionaries containing page_number and text.
        chunk_size: Maximum number of characters in each chunk.
        chunk_overlap: Number of overlapping characters between chunks.

    Returns:
        List of chunks with metadata.
    """

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    chunks = []
    chunk_id = 1

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text.strip():
                chunks.append(
                    {
                        "chunk_id": chunk_id,
                        "page_number": page_number,
                        "text": chunk_text
                    }
                )

                chunk_id += 1

            start = end - chunk_overlap

    return chunks