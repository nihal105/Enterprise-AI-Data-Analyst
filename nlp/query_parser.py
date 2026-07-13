"""
query_parser.py

Simple query parser.
"""

import re


OPERATIONS = {
    "total": ["total", "sum"],
    "average": ["average", "avg", "mean"],
    "top": ["top", "highest", "best", "maximum", "max"],
    "bottom": ["bottom", "lowest", "minimum", "min"]
}

METRICS = {
    "sales": ["sales", "revenue", "income"],
    "profit": ["profit", "margin"],
    "quantity": ["quantity", "qty", "units"]
}

DIMENSIONS = {
    "customer": ["customer", "client"],
    "product": ["product", "item"],
    "country": ["country"],
    "category": ["category"],
    "month": ["month", "monthly"],
    "year": ["year", "yearly"]
}


def parse_query(question):

    question = question.lower()

    parsed = {
        "operation": None,
        "metric": None,
        "dimension": None
    }

    for op, words in OPERATIONS.items():
        if any(word in question for word in words):
            parsed["operation"] = op
            break

    for metric, words in METRICS.items():
        if any(word in question for word in words):
            parsed["metric"] = metric
            break

    for dim, words in DIMENSIONS.items():
        if any(word in question for word in words):
            parsed["dimension"] = dim
            break

    return parsed