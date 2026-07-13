"""
intent_templates.py

Contains all business intents and their templates.
"""

INTENTS = {

# ==================================================
# AVERAGE SALES
# ==================================================
"average_sales": {
    "verbs": ["Show","Display","Calculate","Find","Give","Tell me","Provide","Reveal","Compute","View"],
    "metrics": [
        "average sales","mean sales","average revenue","average sales amount",
        "sales average","average business sales","average turnover","average income"
    ]
},

# ==================================================
# AVERAGE PROFIT
# ==================================================
"average_profit": {
    "verbs": ["Show","Display","Calculate","Find","Give","Tell me","Provide","Reveal","Compute","View"],
    "metrics": [
        "average profit","mean profit","average earnings","average business profit",
        "profit average","average net profit","average gross profit","average income"
    ]
},

# ==================================================
# SALES BY CATEGORY
# ==================================================
"sales_by_category": {
    "verbs": ["Show","Display","Compare","Analyze","Provide","Reveal","Find","Give"],
    "metrics": [
        "sales by category","category sales","category wise sales",
        "sales across categories","category performance",
        "sales for each category"
    ]
},

# ==================================================
# SALES BY SUBCATEGORY
# ==================================================
"sales_by_subcategory": {
    "verbs": ["Show","Display","Compare","Analyze","Provide","Reveal","Find","Give"],
    "metrics": [
        "sales by subcategory","subcategory sales",
        "subcategory wise sales","sales across subcategories",
        "subcategory performance"
    ]
},

# ==================================================
# SALES BY SEGMENT
# ==================================================
"sales_by_segment": {
    "verbs": ["Show","Display","Compare","Analyze","Provide","Reveal","Find","Give"],
    "metrics": [
        "sales by segment","segment sales",
        "segment wise sales","customer segment sales",
        "segment performance"
    ]
},

# ==================================================
# TOP CUSTOMERS
# ==================================================
"top_customers": {
    "verbs": ["Show","Display","List","Find","Identify","Reveal","Give","Provide"],
    "metrics": [
        "top customers","best customers",
        "highest spending customers","most valuable customers",
        "top 10 customers","premium customers"
    ]
},

# ==================================================
# TOP STATES
# ==================================================
"top_states": {
    "verbs": ["Show","Display","List","Find","Reveal","Provide"],
    "metrics": [
        "top states","best performing states",
        "highest sales states","top selling states",
    ]
},

# ==================================================
# TOP CITIES
# ==================================================
"top_cities": {
    "verbs": ["Show","Display","List","Find","Reveal","Provide"],
    "metrics": [
        "top cities","best cities",
        "highest sales cities","city performance",
        "top selling cities"
    ]
},

# ==================================================
# ORDER COUNT
# ==================================================
"order_count": {
    "verbs": ["Show","Display","Calculate","Find","Provide","Give"],
    "metrics": [
        "total orders","order count",
        "number of orders","overall orders",
        "total customer orders"
    ]
},

# ==================================================
# QUANTITY ANALYSIS
# ==================================================
"quantity_analysis": {
    "verbs": ["Show","Display","Analyze","Calculate","Provide","Find"],
    "metrics": [
        "quantity sold","sales quantity",
        "total quantity","quantity analysis",
        "product quantities"
    ]
},

# ==================================================
# DISCOUNT ANALYSIS
# ==================================================
"discount_analysis": {
    "verbs": ["Show","Display","Analyze","Calculate","Provide","Find"],
    "metrics": [
        "discount analysis","average discount",
        "discount percentage","overall discount",
        "discount offered"
    ]
},

# ==================================================
# SHIPPING ANALYSIS
# ==================================================
"shipping_analysis": {
    "verbs": ["Show","Display","Analyze","Compare","Provide","Find"],
    "metrics": [
        "shipping analysis","shipping mode",
        "delivery performance","shipping performance",
        "ship mode analysis"
    ]
},

# ==================================================
# SALES GROWTH
# ==================================================
"sales_growth": {
    "verbs": ["Show","Display","Analyze","Calculate","Provide","Find"],
    "metrics": [
        "sales growth","growth in sales",
        "sales trend","sales increase",
        "business growth"
    ]
},

# ==================================================
# PROFIT GROWTH
# ==================================================
"profit_growth": {
    "verbs": ["Show","Display","Analyze","Calculate","Provide","Find"],
    "metrics": [
        "profit growth","growth in profit",
        "profit trend","profit increase",
        "earnings growth"
    ]
},

# ==================================================
# HIGHEST PROFIT PRODUCT
# ==================================================
"highest_profit_product": {
    "verbs": ["Show","Find","Display","Identify","Reveal","Provide"],
    "metrics": [
        "highest profit product",
        "most profitable product",
        "top profit product",
        "best profit item"
    ]
},

# ==================================================
# LOWEST PROFIT PRODUCT
# ==================================================
"lowest_profit_product": {
    "verbs": ["Show","Find","Display","Identify","Reveal","Provide"],
    "metrics": [
        "lowest profit product",
        "least profitable product",
        "worst profit product",
        "lowest earning product"
    ]
},

# ==================================================
# DASHBOARD SUMMARY
# ==================================================
"dashboard_summary": {
    "verbs": ["Show","Display","Generate","Provide","Create","Give"],
    "metrics": [
        "dashboard summary",
        "business summary",
        "overall dashboard",
        "business overview",
        "executive summary"
    ]
},
# ==================================================
# BOTTOM PRODUCTS
# ==================================================
"bottom_products": {
    "verbs": ["Show","Display","Find","List","Identify","Reveal","Provide","Give"],
    "metrics": [
        "bottom products",
        "least selling products",
        "lowest selling products",
        "worst products",
        "bottom 10 products",
        "least popular products"
    ]
},

# ==================================================
# BOTTOM CUSTOMERS
# ==================================================
"bottom_customers": {
    "verbs": ["Show","Display","Find","List","Identify","Reveal","Provide","Give"],
    "metrics": [
        "bottom customers",
        "lowest spending customers",
        "least valuable customers",
        "bottom 10 customers",
        "inactive customers"
    ]
},

# ==================================================
# BOTTOM STATES
# ==================================================
"bottom_states": {
    "verbs": ["Show","Display","Find","List","Reveal","Provide"],
    "metrics": [
        "bottom states",
        "lowest sales states",
        "worst performing states",
        "least profitable states",
    ]
},

# ==================================================
# BOTTOM CITIES
# ==================================================
"bottom_cities": {
    "verbs": ["Show","Display","Find","List","Reveal","Provide"],
    "metrics": [
        "bottom cities",
        "lowest sales cities",
        "worst performing cities",
        "least profitable cities",
        "city performance"
    ]
},

# ==================================================
# REGION PROFIT
# ==================================================
"region_profit": {
    "verbs": ["Show","Display","Analyze","Compare","Provide","Reveal","Find"],
    "metrics": [
        "profit by region",
        "regional profit",
        "region wise profit",
        "profit across regions",
        "region profit performance"
    ]
},

# ==================================================
# CATEGORY PROFIT
# ==================================================
"category_profit": {
    "verbs": ["Show","Display","Analyze","Compare","Provide","Reveal","Find"],
    "metrics": [
        "profit by category",
        "category profit",
        "category wise profit",
        "profit across categories",
        "category profit performance"
    ]
},

# ==================================================
# MONTHLY PROFIT
# ==================================================
"monthly_profit": {
    "verbs": ["Show","Display","Calculate","Analyze","Provide","Reveal"],
    "metrics": [
        "monthly profit",
        "profit by month",
        "month wise profit",
        "monthly earnings",
        "monthly business profit"
    ]
},

# ==================================================
# YEARLY SALES
# ==================================================
"yearly_sales": {
    "verbs": ["Show","Display","Calculate","Analyze","Provide","Reveal"],
    "metrics": [
        "yearly sales",
        "annual sales",
        "sales by year",
        "year wise sales",
        "annual revenue"
    ]
},

# ==================================================
# YEARLY PROFIT
# ==================================================
"yearly_profit": {
    "verbs": ["Show","Display","Calculate","Analyze","Provide","Reveal"],
    "metrics": [
        "yearly profit",
        "annual profit",
        "profit by year",
        "year wise profit",
        "annual earnings"
    ]
},

# ==================================================
# CUSTOMER COUNT
# ==================================================
"customer_count": {
    "verbs": ["Show","Display","Calculate","Find","Provide","Give"],
    "metrics": [
        "customer count",
        "total customers",
        "number of customers",
        "overall customers",
        "registered customers"
    ]
},

# ==================================================
# BEST REGION
# ==================================================
"best_region": {
    "verbs": ["Show","Display","Find","Identify","Reveal","Provide"],
    "metrics": [
        "best region",
        "highest performing region",
        "top region",
        "most profitable region",
        "best sales region"
    ]
},

# ==================================================
# WORST REGION
# ==================================================
"worst_region": {
    "verbs": ["Show","Display","Find","Identify","Reveal","Provide"],
    "metrics": [
        "worst region",
        "lowest performing region",
        "least profitable region",
        "worst sales region",
        "lowest sales region"
    ]
},

# ==================================================
# INVENTORY SUMMARY
# ==================================================
"inventory_summary": {
    "verbs": ["Show","Display","Generate","Provide","Create","Give"],
    "metrics": [
        "inventory summary",
        "inventory overview",
        "stock summary",
        "inventory report",
        "stock overview"
    ]
},
"total_sales": {
    "verbs": [
        "Show","Display","Calculate","Find",
        "Give","Tell me","Provide","Reveal"
    ],
    "metrics": [
        "total sales",
        "overall sales",
        "grand total sales",
        "total revenue",
        "overall revenue",
        "business sales"
    ]
},
"monthly_sales": {
    "verbs": [
        "Show","Display","Calculate","Analyze",
        "Provide","Reveal"
    ],
    "metrics": [
        "monthly sales",
        "sales by month",
        "month wise sales",
        "monthly revenue",
        "monthly business sales"
    ]
},
# ==================================================
# TOTAL PROFIT
# ==================================================
"total_profit": {
    "verbs": [
        "Show",
        "Display",
        "Calculate",
        "Find",
        "Give",
        "Tell me",
        "Provide",
        "Reveal",
        "Compute",
        "View"
    ],
    "metrics": [
        "total profit",
        "overall profit",
        "grand total profit",
        "net profit",
        "overall earnings",
        "business profit",
        "company profit",
        "total earnings"
    ]
},
}