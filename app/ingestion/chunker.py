from app.config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_text(documents):
    chunks = []

    for doc in documents:
        words = doc["text"].split()
        start = 0
        chunk_id = 0

        while start < len(words):
            end = start + CHUNK_SIZE
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            chunks.append({
                "chunk_id": f"{doc['doc']}_p{doc['page']}_c{chunk_id}",
                "doc": doc["doc"],
                "page": doc["page"],
                "text": chunk_text
            })

            start += CHUNK_SIZE - CHUNK_OVERLAP
            chunk_id += 1

    return chunks