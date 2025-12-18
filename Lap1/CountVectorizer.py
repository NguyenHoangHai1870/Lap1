from typing import List,Dict
from src.core.interface import Vectorizer
from src.core.interface import Tokenizer

class CountVectorizer(Vectorizer):
    def __init__(self,tokenizer : Tokenizer):
        self.tokenizer = tokenizer
        self.vocab : Dict[str,int] = {}

    def fit(self, corpus: List[str]):
        unique_token = set()
        for doc in corpus:
            tokens = self.tokenizer.tokenize(doc)
            unique_token.update(tokens)

        self.vocab = {token: idx for idx, token in enumerate(sorted(unique_token))}

    def transform(self, document: List[str]) -> List[List[int]]:
        vectors = []
        for doc in document:
            vecto = [0] * len(self.vocab)
            tokens = self.tokenizer.tokenize(doc)
            for token in tokens:
                idx = self.vocab[token]
                vecto[idx] += 1
            vectors.append(vecto)
        return vectors

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        self.fit(corpus)
        return self.transform(corpus)

