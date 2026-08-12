from app.services.pdf_service import extract_pages_from_pdf
from app.services.chunk_service import chunk_pages


pdf_path = "sample.pdf"

pages = extract_pages_from_pdf(pdf_path)

chunks = chunk_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
)

print("=" * 60)
print("DOCUMENT INFORMATION")
print("=" * 60)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))


for chunk in chunks[:3]:
    print("\n" + "=" * 60)
    print(f"CHUNK {chunk['chunk_id']}")
    print(f"PAGE: {chunk['page_number']}")
    print("=" * 60)

    print(chunk["text"])