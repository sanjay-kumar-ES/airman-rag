from app.ingestion.loader import load_pdfs
from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import embed_chunks
from app.retrieval.index import build_faiss_index


def run_ingestion():
    print("Loading PDFs...")
    documents = load_pdfs()

    print("Cleaning text...")
    for doc in documents:
        doc["text"] = clean_text(doc["text"])

    print("Chunking...")
    chunks = chunk_text(documents)

    print(f"Total chunks created: {len(chunks)}")

    print("Generating embeddings...")
    embeddings = embed_chunks(chunks)

    print("Building FAISS index...")
    build_faiss_index(embeddings, chunks)

    print("Ingestion complete.")


    
    
    
if __name__ == "__main__":
    run_ingestion()