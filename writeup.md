# Analyzing Customer Orders Using Python

## Objective
This project analyzes a small e-commerce dataset of customer orders using core Python data structures (lists, tuples, dictionaries, and sets) to derive business insights — without relying on external libraries like pandas.

## Dataset
The raw data is a list of orders, where each order is a tuple of `(customer, product, price, category)`. There are 12 customers, 27 orders, spanning 19 unique products across 3 categories: Electronics, Clothing, and Home Essentials.

## Data Structures Used
- **List of tuples (`orders`)** — the raw, ordered record of every purchase.
- **Dictionary (`customer_orders`)** — maps each customer to the list of products they bought, built by iterating over `orders`.
- **Dictionary (`product_categories`)** — maps each product to its category for quick lookup.
- **Set (`categories`)** — the distinct set of product categories, derived by de-duplicating category values.
- **Dictionaries (`customer_totals`, `customer_classification`)** — total spend per customer and a derived label (High/Moderate/Low-value buyer) based on spend thresholds.
- **Dictionary (`category_revenue`)** — total revenue per category, accumulated with `dict.get`.
- **Sets (`customer_category_map`, `multi_category_customers`, `electronics_customers_set`, `clothing_customers_set`)** — used with set operations (intersection `&`) to answer questions like "which customers bought from more than one category" and "which customers bought both Electronics and Clothing."
- **Dictionary (`product_frequency`)** — purchase count per product, sorted to find the most popular items.

## Business Insights Produced
1. **Customer spending & classification** — every customer's total spend, labeled High-value (>$100), Moderate ($50–$100), or Low-value (<$50).
2. **Category revenue** — total revenue generated per category, ranked highest to lowest.
3. **Electronics customers** — the list of customers who bought at least one electronics item.
4. **Top 3 highest-spending customers** — ranked by total spend.
5. **Multi-category customers** — customers who purchased from more than one category, found via set membership.
6. **Cross-category customers (Electronics ∩ Clothing)** — customers who bought from both categories, found via set intersection.
7. **Most frequently purchased products** — product purchase counts, sorted descending.

## Sample Output
```
CUSTOMER ORDER ANALYSIS
============================================================
Customers: 12
Orders: 27
Unique products: 19
Categories: Clothing, Electronics, Home Essentials

CUSTOMER SPENDING & CLASSIFICATION
------------------------------------------------------------
Aarav      $1150.00  High-value buyer
Bhavna     $ 740.00  High-value buyer
...

CATEGORY REVENUE
------------------------------------------------------------
Electronics          $ 3325.00
Home Essentials      $ 1355.00
Clothing             $  555.00

TOP 3 HIGHEST-SPENDING CUSTOMERS
------------------------------------------------------------
1. Aarav: $1150.00
2. Ishan: $900.00
3. Farah: $840.00
```
(Full output is available by running `customer_order_analysis.py` or in the attached screenshots.)

## Key Learnings
- Lists of tuples are a simple, readable way to model raw transactional data before it's reshaped into dictionaries for analysis.
- Dictionaries are well-suited for aggregation (totals, counts, categorical lookups) keyed by a natural identifier like customer name or product name.
- Set operations (union, intersection) make it trivial to answer "which items satisfy multiple conditions" questions — e.g., customers active in more than one category — with far less code than nested loops.
- Separating data (the `orders` list) from derived structures (dictionaries/sets) keeps the analysis logic clear and reproducible: every insight is computed fresh from the same source of truth.

## Conclusion
Using only built-in Python data structures, this project turns a flat list of order records into a set of actionable business insights: who the top customers are, which categories drive the most revenue, and which products are most popular — demonstrating that meaningful data analysis doesn't always require external libraries.
