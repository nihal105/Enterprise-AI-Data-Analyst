"""
text_cleaner.py

This module cleans the text in the intent dataset
before it is used for training.
"""

import re
import pandas as pd


class TextCleaner:

    def clean_text(self, text):
        """
        Clean a single sentence.
        """

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(r"[^\w\s]", "", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text


def main():

    # Load dataset
    df = pd.read_csv(
        "datasets/training/intent_dataset.csv"
    )

    cleaner = TextCleaner()

    # Create a cleaned version of every question
    df["clean_question"] = df["question"].apply(
        cleaner.clean_text
    )

    # Save cleaned dataset
    df.to_csv(
        "datasets/training/clean_intent_dataset.csv",
        index=False
    )

    print("=" * 60)
    print("TEXT CLEANING COMPLETED")
    print("=" * 60)

    print(df[["question", "clean_question"]].head(10))


if __name__ == "__main__":
    main()