
# 1. Store customer orders
customer_names = [
    "Aarav", "Bhavna", "Chandan", "Divya", "Eshan", "Farah",
    "Girish", "Harini", "Ishan", "Kavya", "Manoj", "Nisha"
]

# Each tuple: (customer name, product, price, category)
orders = [
    ("Aarav", "Laptop", 850, "Electronics"),
    ("Aarav", "Headphones", 120, "Electronics"),
    ("Aarav", "Office Chair", 180, "Home Essentials"),

    ("Bhavna", "Smartphone", 650, "Electronics"),
    ("Bhavna", "T-Shirt", 35, "Clothing"),
    ("Bhavna", "Jeans", 55, "Clothing"),

    ("Chandan", "Microwave", 160, "Home Essentials"),
    ("Chandan", "Sneakers", 75, "Clothing"),

    ("Divya", "Tablet", 320, "Electronics"),
    ("Divya", "Handbag", 90, "Clothing"),
    ("Divya", "Bed Sheet", 45, "Home Essentials"),

    ("Eshan", "Headphones", 80, "Electronics"),
    ("Eshan", "T-Shirt", 30, "Clothing"),

    ("Farah", "Refrigerator", 700, "Home Essentials"),
    ("Farah", "Vacuum Cleaner", 140, "Home Essentials"),

    ("Girish", "Jeans", 60, "Clothing"),
    ("Girish", "T-Shirt", 25, "Clothing"),

    ("Harini", "Smartwatch", 150, "Electronics"),
    ("Harini", "Sneakers", 85, "Clothing"),
    ("Harini", "Coffee Maker", 70, "Home Essentials"),

    ("Ishan", "Laptop", 900, "Electronics"),

    ("Kavya", "Sofa Cushion", 40, "Home Essentials"),
    ("Kavya", "Handbag", 65, "Clothing"),

    ("Manoj", "Monitor", 210, "Electronics"),
    ("Manoj", "Keyboard", 45, "Electronics"),

    ("Nisha", "Water Bottle", 20, "Home Essentials"),
    ("Nisha", "T-Shirt", 35, "Clothing"),
]

# Dictionary: customer -> ordered products
customer_orders = {name: [] for name in customer_names}
for customer, product, price, category in orders:
    customer_orders[customer].append(product)

# Dictionary: product -> category
product_categories = {}
for customer, product, price, category in orders:
    product_categories[product] = category

# Set of unique categories
categories = set(product_categories.values())

# 3. Analyze customer orders
customer_totals = {}
customer_classification = {}

for customer in customer_names:
    total = 0
    for order_customer, product, price, category in orders:
        if order_customer == customer:
            total += price

    customer_totals[customer] = total

    if total > 100:
        classification = "High-value buyer"
    elif total >= 50:
        classification = "Moderate buyer"
    else:
        classification = "Low-value buyer"

    customer_classification[customer] = classification

# 4. Business insights
category_revenue = {}
for customer, product, price, category in orders:
    category_revenue[category] = category_revenue.get(category, 0) + price

unique_products = {product for customer, product, price, category in orders}

electronics_customers = [
    customer for customer in customer_names
    if any(order_customer == customer and category == "Electronics"
           for order_customer, product, price, category in orders)
]

top_three_customers = sorted(
    customer_totals.items(),
    key=lambda item: item[1],
    reverse=True
)[:3]

# 5. Set operations for category purchasing behavior
customer_category_map = {customer: set() for customer in customer_names}
for customer, product, price, category in orders:
    customer_category_map[customer].add(category)

multi_category_customers = {
    customer for customer, customer_categories in customer_category_map.items()
    if len(customer_categories) > 1
}

electronics_customers_set = {
    customer for customer, customer_categories in customer_category_map.items()
    if "Electronics" in customer_categories
}
clothing_customers_set = {
    customer for customer, customer_categories in customer_category_map.items()
    if "Clothing" in customer_categories
}
electronics_and_clothing_customers = electronics_customers_set & clothing_customers_set

# Product purchase frequency
product_frequency = {}
for customer, product, price, category in orders:
    product_frequency[product] = product_frequency.get(product, 0) + 1

most_frequently_purchased_products = sorted(
    product_frequency.items(),
    key=lambda item: (-item[1], item[0])
)

# Demonstrate dictionary modification
customer_orders["Nisha"].append("Notebook")
customer_orders["Nisha"].remove("Notebook")  # demonstration without changing final dataset

# Display / export a reproducible summary
print("CUSTOMER ORDER ANALYSIS")
print("=" * 60)
print(f"Customers: {len(customer_names)}")
print(f"Orders: {len(orders)}")
print(f"Unique products: {len(unique_products)}")
print(f"Categories: {', '.join(sorted(categories))}")
print()

print("CUSTOMER SPENDING & CLASSIFICATION")
print("-" * 60)
for customer in sorted(customer_names):
    print(f"{customer:<10} ${customer_totals[customer]:>7.2f}  {customer_classification[customer]}")

print("\nCATEGORY REVENUE")
print("-" * 60)
for category, revenue in sorted(category_revenue.items(), key=lambda x: x[1], reverse=True):
    print(f"{category:<20} ${revenue:>8.2f}")

print("\nELECTRONICS CUSTOMERS")
print("-" * 60)
print(", ".join(sorted(electronics_customers)))

print("\nTOP 3 HIGHEST-SPENDING CUSTOMERS")
print("-" * 60)
for rank, (customer, total) in enumerate(top_three_customers, start=1):
    print(f"{rank}. {customer}: ${total:.2f}")

print("\nCUSTOMERS WHO PURCHASED FROM MULTIPLE CATEGORIES")
print("-" * 60)
print(", ".join(sorted(multi_category_customers)))

print("\nCUSTOMERS WHO BOUGHT BOTH ELECTRONICS AND CLOTHING")
print("-" * 60)
print(", ".join(sorted(electronics_and_clothing_customers)))

print("\nMOST FREQUENTLY PURCHASED PRODUCTS")
print("-" * 60)
for product, count in most_frequently_purchased_products:
    print(f"{product:<20} {count} purchase(s)")
