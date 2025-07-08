from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_answer(query, docs):
    query_emb = model.encode([query])
    docs_emb = model.encode(docs)

    # Calcolo similarità cosine
    cosine_sim = np.dot(docs_emb, query_emb.T).squeeze()

    # Prendo l'indice con similarità massima
    idx = np.argmax(cosine_sim)
    return docs[idx]
