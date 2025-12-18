import re
from typing import List
from src.core.interface import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self,text: str) -> List[str]:
        text = text.lower()
        text = re.sub(r"([.,?!])", r" \1 ", text)
        token = text.split()
        return token