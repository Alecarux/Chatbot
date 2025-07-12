import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('italian'))

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^a-zàèéìòù\s]', '', text)
        return text

    def full_preprocess(self, text: str) -> str:
        text = self.clean_text(text)
        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in text.split()
            if word not in self.stop_words and len(word) > 2
        ]
        return ' '.join(tokens)