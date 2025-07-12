# chatbot/retrieval.py

from sentence_transformers import SentenceTransformer, util
from chatbot.preprocessing import TextPreprocessor
import torch
import os


class LiteChatbot:
    def __init__(self, folder='docs'):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.preprocessor = TextPreprocessor()
        self.folder = folder
        self.paragraphs = []  # ogni entry: (paragrafo, nome_file)
        self.embeddings = None

    def load_docs(self):
        all_paragraphs = []
        sources = []

        for filename in os.listdir(self.folder):
            if filename.endswith(".txt"):
                path = os.path.join(self.folder, filename)
                with open(path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    raw_paragraphs = text.split('\n\n')  # dividi per paragrafi
                    for p in raw_paragraphs:
                        cleaned = self.preprocessor.full_preprocess(p)
                        if cleaned.strip():  # evita paragrafi vuoti
                            all_paragraphs.append(cleaned)
                            sources.append((p.strip(), filename))  # salva originale + sorgente

        self.paragraphs = sources
        self.embeddings = self.model.encode(all_paragraphs, convert_to_tensor=True)

    def search(self, query):
        query_embed = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embed, self.embeddings)[0]
        best_idx = torch.argmax(scores).item()

        best_paragraph, source_file = self.paragraphs[best_idx]
        similarity = scores[best_idx].item()
        return best_paragraph, source_file, similarity