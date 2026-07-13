"""
embedding.py

Token embedding layer for the Transformer.
"""

import torch
import torch.nn as nn


class TokenEmbedding(nn.Module):

    def __init__(self, vocab_size, embed_dim):

        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embed_dim,
            padding_idx=0
        )

    def forward(self, x):

        return self.embedding(x)


def main():

    vocab_size = 140      # Your current vocabulary size
    embed_dim = 128

    embedding = TokenEmbedding(
        vocab_size,
        embed_dim
    )

    sample = torch.randint(
        0,
        vocab_size,
        (2, 15)
    )

    output = embedding(sample)

    print("=" * 60)
    print("TOKEN EMBEDDING")
    print("=" * 60)

    print("Input Shape :", sample.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()