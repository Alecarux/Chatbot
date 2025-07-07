def search_answer(query, documents):
    # Per ora ritorna il documento più "simile" con una semplice ricerca
    # Poi lo miglioreremo con modelli ML
    query = query.lower()
    for doc in documents:
        if query in doc.lower():
            return doc
    return "Non ho trovato niente di utile."

