import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import TOP_K

# Load embedding model (same as ingestion)
model = SentenceTransformer("all-mpnet-base-v2")


def search_index(index, metadata, query):
    """
    Embed the query, search FAISS index,
    and return top-K results with scores and metadata.
    """

    # Expand query slightly for better semantic retrieval
    expanded_query = f"This is an aviation exam question: {query}"

    # Encode query
    query_embedding = model.encode(
        [expanded_query],
        convert_to_numpy=True
    )

    # Normalize for cosine similarity (since using IndexFlatIP)
    norm = np.linalg.norm(query_embedding, axis=1, keepdims=True)
    query_embedding = query_embedding / norm

    # Perform search
    scores, indices = index.search(query_embedding, TOP_K)

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue

        results.append({
            "score": float(score),
            "chunk": metadata[idx]
        })

    return results