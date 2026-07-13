"""
dataloader.py

Creates DataLoader objects for training.
"""

from torch.utils.data import DataLoader

from transformer.dataset import IntentDataset


def main():

    dataset = IntentDataset(
        "datasets/training/encoded_intent_dataset.csv"
    )

    dataloader = DataLoader(
        dataset,
        batch_size=32,
        shuffle=True
    )

    print("=" * 60)
    print("DATALOADER")
    print("=" * 60)

    print("Total Batches:", len(dataloader))

    for batch_inputs, batch_labels in dataloader:

        print("\nBatch Input Shape:")
        print(batch_inputs.shape)

        print("\nBatch Label Shape:")
        print(batch_labels.shape)

        break


if __name__ == "__main__":
    main()