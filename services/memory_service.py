import json
import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

MEMORY_FILE = "memory/debug_memory.json"
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_to_memory(error, solution, validation):
    memory = load_memory()

    entry = {
        "error": error,
        "root_cause": solution["root_cause"],
        "fix": solution["recommended_fix"],
        "confidence": validation["fix_is_correct"]
    }

    memory.append(entry)
    save_memory(memory)


def search_memory(error_query):
    memory = load_memory()

    if not memory:
        return None

    texts = [m["error"] for m in memory]

    embeddings = EMBED_MODEL.encode(texts)
    query_embedding = EMBED_MODEL.encode([error_query])

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    D, I = index.search(np.array(query_embedding), k=1)

    best_match = memory[I[0][0]]

    if D[0][0] < 1.0:  # similarity threshold
        return best_match

    return None
