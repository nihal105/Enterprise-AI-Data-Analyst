"""
vocabulary.py

Builds the vocabulary for the Transformer.
"""

import pandas as pd
from collections import Counter


class Vocabulary:

    def __init__(self):

        self.word2idx = {
            "<PAD>": 0,
            "<UNK>": 1
        }

        self.idx2word = {
            0: "<PAD>",
            1: "<UNK>"
        }

    def build(self, texts):

        counter = Counter()

        for sentence in texts:

            words = sentence.split()

            counter.update(words)

        index = 2

        for word, _ in counter.items():

            self.word2idx[word] = index
            self.idx2word[index] = word

            index += 1

    def __len__(self):

        return len(self.word2idx)


def main():

    df = pd.read_csv(
        "datasets/training/clean_intent_dataset.csv"
    )

    vocab = Vocabulary()

    vocab.build(
        df["clean_question"]
    )

    print("=" * 60)
    print("VOCABULARY CREATED")
    print("=" * 60)

    print("Vocabulary Size :", len(vocab))

    print("\nFirst 20 Words\n")

    for word, idx in list(vocab.word2idx.items())[:20]:

        print(f"{word:20} -> {idx}")


if __name__ == "__main__":
    main()