"""
label_encoder.py

Encodes intent labels into integer IDs.
"""

import pandas as pd


class LabelEncoder:

    def __init__(self):
        self.label2id = {}
        self.id2label = {}

    def fit(self, labels):

        unique_labels = sorted(labels.unique())

        for idx, label in enumerate(unique_labels):
            self.label2id[label] = idx
            self.id2label[idx] = label

    def transform(self, labels):

        return labels.map(self.label2id)

    def fit_transform(self, labels):

        self.fit(labels)
        return self.transform(labels)


def main():

    df = pd.read_csv(
        "datasets/training/clean_intent_dataset.csv"
    )

    encoder = LabelEncoder()

    df["label"] = encoder.fit_transform(df["intent"])

    print("=" * 60)
    print("LABEL ENCODING COMPLETED")
    print("=" * 60)

    print(df[["intent", "label"]].drop_duplicates().head(30))

    print("\nTotal Classes:", len(encoder.label2id))

    df.to_csv(
        "datasets/training/encoded_intent_dataset.csv",
        index=False
    )


if __name__ == "__main__":
    main()