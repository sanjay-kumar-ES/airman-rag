import os
import faiss
import pickle
import numpy as np
from app.config import STORAGE_PATH


def build_faiss_index(embeddings, metadata):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)  # Inner product for cosine
    index.add(embeddings)

    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH)

    faiss.write_index(index, os.path.join(STORAGE_PATH, "faiss.index"))

    with open(os.path.join(STORAGE_PATH, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print("Index saved successfully.")


def load_faiss_index():
    index = faiss.read_index(os.path.join(STORAGE_PATH, "faiss.index"))

    with open(os.path.join(STORAGE_PATH, "metadata.pkl"), "rb") as f:
        metadata = pickle.load(f)

    return index, metadata