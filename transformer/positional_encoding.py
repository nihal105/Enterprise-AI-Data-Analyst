"""
positional_encoding.py

Implements sinusoidal positional encoding.
"""

import math
import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):

    def __init__(self, embed_dim, max_len=5000):

        super().__init__()

        pe = torch.zeros(max_len, embed_dim)

        position = torch.arange(
            0,
            max_len,
            dtype=torch.float
        ).unsqueeze(1)

        div_term = torch.exp(
            torch.arange(0, embed_dim, 2).float()
            * (-math.log(10000.0) / embed_dim)
        )

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0)

        self.register_buffer("pe", pe)

    def forward(self, x):

        return x + self.pe[:, :x.size(1)]


def main():

    batch_size = 2
    seq_len = 15
    embed_dim = 128

    x = torch.randn(batch_size, seq_len, embed_dim)

    pe = PositionalEncoding(embed_dim)

    output = pe(x)

    print("=" * 60)
    print("POSITIONAL ENCODING")
    print("=" * 60)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()