from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from chatbot.preprocessing import TextPreprocessor
import torch
import os


class LiteChatbot:
    def __init__(self, folder='docs'):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.qa_model = pipeline('question-answering', model='deepset/roberta-base-squad2')
        self.preprocessor = TextPreprocessor()
        self.folder = folder
        self.paragraphs = []
        self.embeddings = None

    def load_docs(self):
        all_paragraphs = []
        sources = []

        for filename in os.listdir(self.folder):
            if filename.endswith(".txt"):
                path = os.path.join(self.folder, filename)
                with open(path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    raw_paragraphs = text.split('\n\n')
                    for p in raw_paragraphs:
                        cleaned = self.preprocessor.full_preprocess(p)
                        if cleaned.strip():
                            all_paragraphs.append(cleaned)
                            sources.append((p.strip(), filename))

        self.paragraphs = sources
        self.embeddings = self.model.encode(all_paragraphs, convert_to_tensor=True)

    def search(self, query, top_k=3):
        query_embed = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embed, self.embeddings)[0]
        top_indices = torch.topk(scores, k=top_k).indices.tolist()

        top_paragraphs = [(self.paragraphs[i][0], self.paragraphs[i][1], scores[i].item()) for i in top_indices]
        return top_paragraphs

    def answer_query(self, query):
        top_paragraphs = self.search(query, top_k=3)

        for paragraph, source, score in top_paragraphs:
            answer = self.qa_model(question=query, context=paragraph)
            if answer['score'] > 0.3 and answer['answer'].strip():
                return {
                    "answer": answer['answer'],
                    "source": source,
                    "confidence": round(answer['score'], 2)
                }

        return {
            "answer": "Mi dispiace, non ho trovato una risposta precisa.",
            "source": None,
            "confidence": 0.0
        }
