"""
tokenizer.py

Converts text into integer tokens.
"""

import pandas as pd

from transformer.vocabulary import Vocabulary


class Tokenizer:

    def __init__(self, vocabulary):

        self.vocab = vocabulary

    def tokenize(self, sentence):

        words = sentence.split()

        tokens = []

        for word in words:

            token = self.vocab.word2idx.get(
                word,
                self.vocab.word2idx["<UNK>"]
            )

            tokens.append(token)

        return tokens


def main():

    df = pd.read_csv(
        "datasets/training/clean_intent_dataset.csv"
    )

    vocab = Vocabulary()

    vocab.build(df["clean_question"])

    tokenizer = Tokenizer(vocab)

    print("=" * 60)
    print("TOKENIZER")
    print("=" * 60)

    for sentence in df["clean_question"].head(10):

        print("\nSentence:")
        print(sentence)

        print("Tokens:")
        print(tokenizer.tokenize(sentence))


if __name__ == "__main__":
    main()