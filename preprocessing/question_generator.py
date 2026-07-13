"""
question_generator.py

Generates natural language questions from
intent templates.
"""

from intent_templates import INTENTS


# -------------------------------------------------
# Question Templates
# -------------------------------------------------

QUESTION_PATTERNS = [

    "{verb} {metric}",
    "{verb} the {metric}",
    "{verb} all {metric}",
    "{verb} overall {metric}",
    "{verb} complete {metric}",

    "Can you {verb_lower} {metric}?",
    "Can you {verb_lower} the {metric}?",
    "Could you {verb_lower} the {metric}?",
    "Please {verb_lower} {metric}.",
    "Kindly {verb_lower} the {metric}.",

    "I want {metric}.",
    "I want the {metric}.",
    "I need {metric}.",
    "I need the {metric}.",
    "I would like {metric}.",
    "I'd like the {metric}.",

    "What is {metric}?",
    "What is the {metric}?",
    "How much is {metric}?",
    "How much is the {metric}?",

    "Give me {metric}.",
    "Give me the {metric}.",
    "Show me {metric}.",
    "Show me the {metric}.",

    "Display {metric}.",
    "Display the {metric}.",

    "Reveal {metric}.",
    "Reveal the {metric}.",

    "Find {metric}.",
    "Find the {metric}.",

    "Provide {metric}.",
    "Provide the {metric}.",

    "Generate {metric}.",
    "Generate the {metric}.",

    "Analyze {metric}.",
    "Analyze the {metric}.",

    "View {metric}.",
    "View the {metric}.",

    "Fetch {metric}.",
    "Fetch the {metric}.",

    "Present {metric}.",
    "Present the {metric}.",

    "Please display {metric}.",
    "Please display the {metric}.",

    "Please calculate {metric}.",
    "Please calculate the {metric}.",

    "Tell me {metric}.",
    "Tell me the {metric}.",

    "Can I see {metric}?",
    "Can I see the {metric}?",

    "I'd like to know {metric}.",
    "I'd like to know the {metric}.",

    "Generate a report for {metric}.",
    "Create a report for {metric}.",

    "Summarize {metric}.",
    "Summarize the {metric}.",

    "Show insights for {metric}.",
    "Analyze performance of {metric}.",

    "Explain {metric}.",
    "Explain the {metric}.",

    "Give detailed {metric}.",
    "Provide detailed {metric}.",

    "Show complete {metric}.",
    "Display complete {metric}.",

    "Give complete {metric}.",
    "Show latest {metric}.",
    "Display latest {metric}.",

    "Create dashboard for {metric}.",
    "Visualize {metric}.",
    "Plot {metric}.",
    "Compare {metric}.",
    "Review {metric}.",
    "Inspect {metric}.",
]

# -------------------------------------------------
# Generate Dataset
# -------------------------------------------------

def generate_dataset():

    dataset = []

    for intent, values in INTENTS.items():

        verbs = values["verbs"]
        metrics = values["metrics"]

        for verb in verbs:
            for metric in metrics:

                for pattern in QUESTION_PATTERNS:

                    question = pattern.format(
                        verb=verb,
                        verb_lower=verb.lower(),
                        metric=metric
                    )

                    dataset.append(
                        (question, intent)
                    )

    return dataset