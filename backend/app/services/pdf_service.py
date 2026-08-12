import pymupdf


def extract_pages_from_pdf(file_path: str) -> list[dict]:
    """
    Extract text from each page of a PDF while preserving
    page-level information.

    Args:
        file_path: Path to the PDF file.

    Returns:
        A list containing page text and page numbers.
    """

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        if text.strip():
            pages.append(
                {
                    "page_number": page_number,
                    "text": text
                }
            )

    document.close()

    return pages