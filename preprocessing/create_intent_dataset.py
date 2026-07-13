"""
create_intent_dataset.py

Main script to generate the complete
Transformer training dataset.
"""

import pandas as pd

from question_generator import generate_dataset


def main():

    # Generate all questions
    dataset = generate_dataset()

    # Create DataFrame
    df = pd.DataFrame(
        dataset,
        columns=["question", "intent"]
    )

    # Remove duplicates
    df = df.drop_duplicates()

    # Shuffle dataset
    df = df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)

    # Save CSV
    output_path = "datasets/training/intent_dataset.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("=" * 60)
    print("DATASET GENERATED SUCCESSFULLY")
    print("=" * 60)

    print(f"Total Samples : {len(df)}")
    print(f"Total Intents : {df['intent'].nunique()}")

    print("\nFirst 10 Samples:\n")
    print(df.head(10))

    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()