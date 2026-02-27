import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


model = SentenceTransformer("all-mpnet-base-v2")


def embed_chunks(chunks):
    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    # Normalize for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings = embeddings / norms

    return embeddings