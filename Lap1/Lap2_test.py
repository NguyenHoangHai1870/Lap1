from NLP.src.preprocessing.RegrexTokenizer import  RegrexTokenizer
from NLP.src.representations.CountVectorizer import CountVectorizer

if __name__ == "__main__":
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]

    # Dùng tokenizer từ Lab 1
    tokenizer = RegrexTokenizer()

    # Truyền tokenizer này vào CountVectorizer
    vectorizer = CountVectorizer(tokenizer)

    # Fit + Transform
    vectors = vectorizer.fit_transform(corpus)

    print("Vocabulary:", vectorizer.vocab)
    print("Document-Term Matrix:")
    for vec in vectors:
        print(vec)