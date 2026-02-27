import os
import fitz  # PyMuPDF
from app.config import DATA_PATH


def load_pdfs():
    documents = []

    for filename in os.listdir(DATA_PATH):
        if not filename.endswith(".pdf"):
            continue

        filepath = os.path.join(DATA_PATH, filename)
        print(f"Processing: {filename}")

        doc = fitz.open(filepath)

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            text = page.get_text("text")

            if text and text.strip():
                documents.append({
                    "doc": filename,
                    "page": page_number + 1,
                    "text": text
                })

        doc.close()

    return documents