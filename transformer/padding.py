"""
padding.py

Pads tokenized sentences to equal length.
"""

import pandas as pd

from transformer.vocabulary import Vocabulary
from transformer.tokenizer import Tokenizer


MAX_LENGTH = 15


def pad_sequence(tokens, max_length=MAX_LENGTH):

    if len(tokens) < max_length:
        tokens = tokens + [0] * (max_length - len(tokens))
    else:
        tokens = tokens[:max_length]

    return tokens


def main():

    df = pd.read_csv(
        "datasets/training/clean_intent_dataset.csv"
    )

    vocab = Vocabulary()
    vocab.build(df["clean_question"])

    tokenizer = Tokenizer(vocab)

    print("=" * 60)
    print("PADDING")
    print("=" * 60)

    for sentence in df["clean_question"].head(5):

        tokens = tokenizer.tokenize(sentence)
        padded = pad_sequence(tokens)

        print("\nSentence:")
        print(sentence)

        print("Original:")
        print(tokens)

        print("Padded:")
        print(padded)


if __name__ == "__main__":
    main()