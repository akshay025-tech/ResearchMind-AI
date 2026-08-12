from app.services.pdf_service import extract_pages_from_pdf


pdf_path = "sample.pdf"

pages = extract_pages_from_pdf(pdf_path)

print("=" * 60)
print("DOCUMENT INFORMATION")
print("=" * 60)

print("Total pages:", len(pages))

for page in pages[:3]:
    print("\n" + "=" * 60)
    print(f"PAGE {page['page_number']}")
    print("=" * 60)

    print(page["text"][:1000])