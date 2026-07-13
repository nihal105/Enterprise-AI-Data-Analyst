"""
attention.py

Multi-Head Self Attention
"""

import torch
import torch.nn as nn


class MultiHeadSelfAttention(nn.Module):

    def __init__(self, embed_dim, num_heads):

        super().__init__()

        assert embed_dim % num_heads == 0

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.query = nn.Linear(embed_dim, embed_dim)
        self.key = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

        self.fc_out = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):

        batch_size = x.shape[0]
        seq_length = x.shape[1]

        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        Q = Q.view(batch_size, seq_length,
                   self.num_heads, self.head_dim).transpose(1, 2)

        K = K.view(batch_size, seq_length,
                   self.num_heads, self.head_dim).transpose(1, 2)

        V = V.view(batch_size, seq_length,
                   self.num_heads, self.head_dim).transpose(1, 2)

        scores = torch.matmul(
            Q,
            K.transpose(-2, -1)
        ) / (self.head_dim ** 0.5)

        attention = torch.softmax(scores, dim=-1)

        out = torch.matmul(attention, V)

        out = out.transpose(1, 2).contiguous()

        out = out.view(
            batch_size,
            seq_length,
            self.embed_dim
        )

        out = self.fc_out(out)

        return out


def main():

    batch_size = 2
    seq_length = 15
    embed_dim = 128
    num_heads = 8

    x = torch.randn(
        batch_size,
        seq_length,
        embed_dim
    )

    attention = MultiHeadSelfAttention(
        embed_dim,
        num_heads
    )

    output = attention(x)

    print("=" * 60)
    print("MULTI-HEAD SELF ATTENTION")
    print("=" * 60)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()