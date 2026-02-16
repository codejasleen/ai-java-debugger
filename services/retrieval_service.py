import faiss
import pickle
from sentence_transformers import SentenceTransformer, CrossEncoder

print("RETRIEVAL SERVICE LOADED")

# Load embedding model (for semantic search)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load cross-encoder reranker (for relevance scoring)
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Load FAISS index
index = faiss.read_index("java_errors.index")

# Load stored knowledge chunks
with open("data/knowledge_chunks.pkl", "rb") as f:
    knowledge_chunks = pickle.load(f)


def retrieve_relevant_context(query: str, top_k=5):
    print("RETRIEVAL FUNCTION CALLED")

    # Step 1: Embed query
    query_embedding = embedding_model.encode([query])

    # Step 2: Retrieve candidates from FAISS
    distances, indices = index.search(query_embedding, top_k)

    print("\n[Initial retrieved chunks]")
    candidates = [knowledge_chunks[i] for i in indices[0]]

    for c in candidates:
        print("-", c)

    # Step 3: Cross-encoder reranking
    # Prepare (query, chunk) pairs
    pairs = [(query, chunk) for chunk in candidates]

    # Get relevance scores
    scores = reranker.predict(pairs)

    # Combine scores with chunks
    scored_chunks = list(zip(scores, candidates))

    # Sort by score descending
    scored_chunks.sort(reverse=True)

    # Take top 3 most relevant chunks
    reranked = [chunk for score, chunk in scored_chunks[:3]]

    print("\n[Cross-encoder reranked chunks]")
    for r in reranked:
        print("-", r)

    # Return final context for LLM
    return "\n".join(reranked)
