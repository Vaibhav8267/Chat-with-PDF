import faiss
import numpy as np

index = None
stored_chunks = []

def store_embeddings(chunks, embeddings):
    global index, stored_chunks
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    stored_chunks = chunks

def retrieve_similar_chunks(query, k=3):
    from embedder import get_embeddings
    query_embedding = get_embeddings([query])[0]
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [stored_chunks[i] for i in I[0]]
