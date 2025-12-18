from NLP.src.preprocessing.RegrexTokenizer import RegrexTokenizer
from NLP.src.preprocessing.SimpleTokenizer import SimpleTokenizer
from NLP.src.dataset_loaders import load_raw_text_data

if __name__ == "__main__":
    simple = SimpleTokenizer()
    regrex = RegrexTokenizer()

    dataset_path = r"C:\Users\admin\PycharmProjects\NLP\UD_English-EWT\en_ewt-ud-train.txt"
    rawtext = load_raw_text_data(dataset_path)
    sample_text = rawtext[:500]

    print("\n--- Tokenizing Sample Text from UD_English-EWT ---")
    print(f"Original Sample (first 100 chars): {sample_text[:100]}...\n")

    simple_tokens = simple.tokenize(sample_text)
    print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")

    regex_tokens = regrex.tokenize(sample_text)
    print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")