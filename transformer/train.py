"""
train.py

Training loop for the Transformer Intent Classifier.
"""

import torch
import torch.nn as nn
import torch.optim as optim

from transformer.dataset import IntentDataset
from transformer.model import IntentClassifier
from torch.utils.data import DataLoader
from preprocessing.intent_templates import INTENTS

def main():

    # Hyperparameters
    VOCAB_SIZE = 141
    EMBED_DIM = 128
    NUM_LAYERS = 4
    NUM_HEADS = 8
    NUM_CLASSES = len(INTENTS)
    BATCH_SIZE = 32
    LEARNING_RATE = 0.001
    EPOCHS = 5

    # Dataset
    dataset = IntentDataset(
        "datasets/training/encoded_intent_dataset.csv"
    )

    dataloader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    # Model
    model = IntentClassifier(
        vocab_size=VOCAB_SIZE,
        embed_dim=EMBED_DIM,
        num_layers=NUM_LAYERS,
        num_heads=NUM_HEADS,
        num_classes=NUM_CLASSES
    )

    # Loss and Optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE
    )

    # Training Loop
    print("=" * 60)
    print("TRAINING STARTED")
    print("=" * 60)

    for epoch in range(EPOCHS):

        total_loss = 0

        for inputs, labels in dataloader:

            optimizer.zero_grad()

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)

        print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {avg_loss:.4f}")

    # Save model
    torch.save(
        model.state_dict(),
        "saved_models/intent_classifier.pth"
    )

    print("\nTraining Completed!")
    print("Model saved to: saved_models/intent_classifier.pth")


if __name__ == "__main__":
    main()