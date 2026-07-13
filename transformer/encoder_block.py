"""
encoder_block.py

Single Transformer Encoder Block.
"""

import torch
import torch.nn as nn

from transformer.attention import MultiHeadSelfAttention
from transformer.feed_forward import FeedForward

class EncoderBlock(nn.Module):

    def __init__(self, embed_dim, num_heads, forward_expansion=4, dropout=0.1):

        super().__init__()

        self.attention = MultiHeadSelfAttention(embed_dim, num_heads)

        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

        self.feed_forward = FeedForward(embed_dim, forward_expansion)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        attention = self.attention(x)

        x = self.norm1(x + self.dropout(attention))

        forward = self.feed_forward(x)

        out = self.norm2(x + self.dropout(forward))

        return out


def main():

    batch_size = 2
    seq_len = 15
    embed_dim = 128
    num_heads = 8

    x = torch.randn(batch_size, seq_len, embed_dim)

    encoder = EncoderBlock(embed_dim, num_heads)

    output = encoder(x)

    print("=" * 60)
    print("ENCODER BLOCK")
    print("=" * 60)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()