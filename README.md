# Analyse Customer Order

A small, dependency-free Python script that analyzes a sample e-commerce dataset of customer orders using core Python data structures (lists, tuples, dictionaries, and sets).

## Requirements
- Python 3.6+ (no external packages needed)

## Usage
```bash
python3 customer_order_analysis.py
```
The script prints a full analysis report to stdout — no arguments or setup required.

## What it does
Starting from a raw list of `(customer, product, price, category)` order tuples, the script derives:
- Per-customer spending totals and a High/Moderate/Low-value buyer classification
- Revenue per product category
- Customers who bought electronics
- The top 3 highest-spending customers
- Customers who purchased from multiple categories, and specifically both Electronics and Clothing (via set intersection)
- Most frequently purchased products

## Files
- [customer_order_analysis.py](customer_order_analysis.py) — the analysis script
- [writeup.md](writeup.md) — a detailed write-up of the dataset, data structures used, and the insights produced
- [PROBLEM_STATEMENT.md](PROBLEM_STATEMENT.md) — the original course-end project brief this script fulfills
