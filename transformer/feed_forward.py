"""
feed_forward.py

Position-wise Feed Forward Network.
"""

import torch
import torch.nn as nn


class FeedForward(nn.Module):

    def __init__(self, embed_dim, forward_expansion=4):

        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(embed_dim, embed_dim * forward_expansion),
            nn.ReLU(),
            nn.Linear(embed_dim * forward_expansion, embed_dim)
        )

    def forward(self, x):

        return self.network(x)


def main():

    batch_size = 2
    seq_length = 15
    embed_dim = 128

    x = torch.randn(batch_size, seq_length, embed_dim)

    ff = FeedForward(embed_dim)

    output = ff(x)

    print("=" * 60)
    print("FEED FORWARD NETWORK")
    print("=" * 60)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()