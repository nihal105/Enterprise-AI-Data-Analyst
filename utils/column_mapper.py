"""
column_mapper.py

Maps different column names to a standard format.
"""

COLUMN_SYNONYMS = {

    "sales": [
        "sales",
        "revenue",
        "amount",
        "total sales",
        "net sales"
    ],

    "profit": [
        "profit",
        "margin",
        "net profit"
    ],

    "quantity": [
        "quantity",
        "qty",
        "units",
        "pieces"
    ],

    "price": [
        "price",
        "unitprice",
        "unit price",
        "selling price"
    ],

    "customer": [
        "customer",
        "customerid",
        "customer id",
        "customer name",
        "client"
    ],

    "product": [
        "product",
        "product name",
        "description",
        "item"
    ],

    "date": [
        "date",
        "order date",
        "invoicedate",
        "invoice date"
    ]
}


def normalize_columns(df):

    mapping = {}

    for column in df.columns:

        clean = column.lower().strip()

        for standard, names in COLUMN_SYNONYMS.items():

            if clean in names:
                mapping[standard] = column

    return mapping