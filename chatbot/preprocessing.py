import os
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # rimuove punteggiatura
    return text.strip()

def preprocess_documents(folder):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            path = os.path.join(folder, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                docs.append(clean_text(text))
    return docs

def expand_query(query):
    return query
