"""
encoder.py

Stacks multiple Encoder Blocks to build
the Transformer Encoder.
"""

import torch
import torch.nn as nn

from transformer.embedding import TokenEmbedding
from transformer.positional_encoding import PositionalEncoding
from transformer.encoder_block import EncoderBlock

class TransformerEncoder(nn.Module):

    def __init__(
        self,
        vocab_size,
        embed_dim,
        num_layers,
        num_heads,
        max_length=15,
        dropout=0.1
    ):

        super().__init__()

        self.embedding = TokenEmbedding(
            vocab_size,
            embed_dim
        )

        self.position = PositionalEncoding(
            embed_dim,
            max_length
        )

        self.layers = nn.ModuleList(
            [
                EncoderBlock(
                    embed_dim,
                    num_heads,
                    dropout=dropout
                )
                for _ in range(num_layers)
            ]
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        x = self.embedding(x)
        x = self.position(x)
        x = self.dropout(x)

        for layer in self.layers:
            x = layer(x)

        return x


def main():

    vocab_size = 140
    embed_dim = 128
    num_layers = 4
    num_heads = 8

    encoder = TransformerEncoder(
        vocab_size,
        embed_dim,
        num_layers,
        num_heads
    )

    sample = torch.randint(
        0,
        vocab_size,
        (2, 15)
    )

    output = encoder(sample)

    print("=" * 60)
    print("TRANSFORMER ENCODER")
    print("=" * 60)

    print("Input Shape :", sample.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()