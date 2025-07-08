from chatbot.retrieval import search_answer
from chatbot.preprocessing import preprocess_documents, clean_text, expand_query


def main():
    # Carica e prepara i documenti
    docs = preprocess_documents('docs/')

    # Esempio query
    query = input("Fai una domanda: ")

    # Cerca la risposta migliore
    answer = search_answer(query, docs)

    print("Risposta trovata:", answer)


if __name__ == "__main__":
    main()
