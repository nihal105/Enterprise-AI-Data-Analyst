"""
dataset.py

Custom PyTorch Dataset for intent classification.
"""

import pandas as pd
import torch  
from torch.utils.data import Dataset  

from transformer.vocabulary import Vocabulary
from transformer.tokenizer import Tokenizer
from transformer.padding import pad_sequence


class IntentDataset(Dataset):

    def __init__(self, csv_file):

        self.df = pd.read_csv(csv_file)

        self.vocab = Vocabulary()
        self.vocab.build(self.df["clean_question"])

        self.tokenizer = Tokenizer(self.vocab)

    def __len__(self):

        return len(self.df)

    def __getitem__(self, idx):

        row = self.df.iloc[idx]

        question = row["clean_question"]
        label = row["label"]

        tokens = self.tokenizer.tokenize(question)
        tokens = pad_sequence(tokens)

        return (
            torch.tensor(tokens, dtype=torch.long),
            torch.tensor(label, dtype=torch.long)
        )


def main():

    dataset = IntentDataset(
        "datasets/training/encoded_intent_dataset.csv"
    )

    print("=" * 60)
    print("PYTORCH DATASET")
    print("=" * 60)

    print("Dataset Size:", len(dataset))

    x, y = dataset[0]

    print("\nFirst Sample")

    print("Input Tensor:")
    print(x)

    print("\nLabel:")
    print(y)


if __name__ == "__main__":
    main()