"""
model.py

Complete Transformer model for
intent classification.
"""

import torch
import torch.nn as nn

from transformer.encoder import TransformerEncoder


class IntentClassifier(nn.Module):

    def __init__(
        self,
        vocab_size,
        embed_dim,
        num_layers,
        num_heads,
        num_classes,
        max_length=15
    ):

        super().__init__()

        self.encoder = TransformerEncoder(
            vocab_size=vocab_size,
            embed_dim=embed_dim,
            num_layers=num_layers,
            num_heads=num_heads,
            max_length=max_length
        )

        self.classifier = nn.Linear(
            embed_dim,
            num_classes
        )

    def forward(self, x):

        x = self.encoder(x)

        # Mean Pooling
        x = x.mean(dim=1)

        logits = self.classifier(x)

        return logits


def main():

    vocab_size = 140
    embed_dim = 128
    num_layers = 4
    num_heads = 8
    num_classes = 30

    model = IntentClassifier(
        vocab_size,
        embed_dim,
        num_layers,
        num_heads,
        num_classes
    )

    sample = torch.randint(
        0,
        vocab_size,
        (2, 15)
    )

    output = model(sample)

    print("=" * 60)
    print("TRANSFORMER INTENT CLASSIFIER")
    print("=" * 60)

    print("Input Shape :", sample.shape)
    print("Output Shape:", output.shape)
if __name__ == "__main__":
    main()