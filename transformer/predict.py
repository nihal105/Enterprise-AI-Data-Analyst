"""
predict.py

Loads the trained Transformer model and
predicts the intent of a user question.
"""

import torch
import pandas as pd

from preprocessing.intent_templates import INTENTS
from transformer.model import IntentClassifier
from transformer.vocabulary import Vocabulary
from transformer.tokenizer import Tokenizer
from transformer.padding import pad_sequence

from preprocessing.text_cleaner import TextCleaner
from preprocessing.label_encoder import LabelEncoder
from analytics.router import execute_intent


# --------------------------------------------------
# Configuration
# --------------------------------------------------

VOCAB_SIZE = 141
EMBED_DIM = 128
NUM_LAYERS = 4
NUM_HEADS = 8
NUM_CLASSES = len(INTENTS)


# --------------------------------------------------
# Build Vocabulary
# --------------------------------------------------

df = pd.read_csv("datasets/training/encoded_intent_dataset.csv")

vocab = Vocabulary()
vocab.build(df["clean_question"])

tokenizer = Tokenizer(vocab)

encoder = LabelEncoder()
encoder.fit(df["intent"])

cleaner = TextCleaner()


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = IntentClassifier(
    vocab_size=VOCAB_SIZE,
    embed_dim=EMBED_DIM,
    num_layers=NUM_LAYERS,
    num_heads=NUM_HEADS,
    num_classes=NUM_CLASSES,
)

model.load_state_dict(
    torch.load(
        "saved_models/intent_classifier.pth",
        map_location=torch.device("cpu"),
    )
)

model.eval()


# --------------------------------------------------
# Prediction Function (For Streamlit)
# --------------------------------------------------

def predict_intent(question):
    """
    Predicts the intent of a business question.

    Returns:
        intent (str)
        confidence (float)
    """

    question = cleaner.clean_text(question)

    tokens = tokenizer.tokenize(question)
    tokens = pad_sequence(tokens)

    x = torch.tensor(tokens).unsqueeze(0)

    with torch.no_grad():

        output = model(x)

        probabilities = torch.softmax(output, dim=1)

        confidence, prediction = torch.max(probabilities, dim=1)

        intent = encoder.id2label[prediction.item()]

    return intent, confidence.item() * 100


# --------------------------------------------------
# Terminal Version
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk a business question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        intent, confidence = predict_intent(question)

        print("\nQuestion:")
        print(question)

        print("\nPredicted Intent:")
        print(intent)

        print(f"\nConfidence: {confidence:.2f}%")

        print("\nBusiness Result:")
        print(execute_intent(intent))