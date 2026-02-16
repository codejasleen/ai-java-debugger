from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge sources
files = [
    "data/java_errors.txt",
    "data/stack_java_errors.txt"
]

knowledge_chunks = []

for file_path in files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            cleaned = [line.strip() for line in lines if line.strip()]
            knowledge_chunks.extend(cleaned)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

print("Total knowledge entries:", len(knowledge_chunks))

# Generate embeddings
embeddings = model.encode(knowledge_chunks)

print("Embeddings shape:", embeddings.shape)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

print("FAISS index built with", index.ntotal, "entries")

# Save index
faiss.write_index(index, "java_errors.index")

# Save mapping
with open("data/knowledge_chunks.pkl", "wb") as f:
    pickle.dump(knowledge_chunks, f)

print("Knowledge mapping saved.")
print("Vector database updated.")
