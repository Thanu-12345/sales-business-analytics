import pandas as pd
import numpy as np

np.random.seed(42)

num_records = 1000

regions = ["North", "South", "East", "West"]

categories = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Headphones"
    ],
    "Furniture": [
        "Office Chair",
        "Desk",
        "Bookshelf",
        "Table"
    ],
    "Office Supplies": [
        "Notebook",
        "Printer",
        "Pen Set",
        "File Folder"
    ]
}

segments = [
    "Consumer",
    "Corporate",
    "Small Business"
]

payment_modes = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Cash"
]

products = []
product_categories = []

for category, product_list in categories.items():
    for product in product_list:
        products.append(product)
        product_categories.append(category)

data = []

for i in range(num_records):

    product_index = np.random.randint(len(products))

    product = products[product_index]
    category = product_categories[product_index]

    quantity = np.random.randint(1, 10)

    price_ranges = {
        "Laptop": (50000, 90000),
        "Smartphone": (15000, 60000),
        "Tablet": (12000, 40000),
        "Headphones": (1000, 8000),
        "Office Chair": (5000, 18000),
        "Desk": (7000, 25000),
        "Bookshelf": (4000, 15000),
        "Table": (5000, 20000),
        "Notebook": (50, 300),
        "Printer": (5000, 25000),
        "Pen Set": (100, 500),
        "File Folder": (50, 250)
    }

    min_price, max_price = price_ranges[product]

    unit_price = np.random.randint(
        min_price,
        max_price + 1
    )

    sales = quantity * unit_price

    cost = sales * np.random.uniform(
        0.55,
        0.80
    )

    profit = sales - cost

    date = pd.Timestamp("2024-01-01") + pd.to_timedelta(
        np.random.randint(0, 730),
        unit="D"
    )

    data.append([
        f"ORD{i+1:05d}",
        date,
        f"Customer {np.random.randint(1, 301)}",
        np.random.choice(regions),
        category,
        product,
        quantity,
        unit_price,
        round(sales, 2),
        round(cost, 2),
        round(profit, 2),
        np.random.choice(segments),
        np.random.choice(payment_modes)
    ])

columns = [
    "Order_ID",
    "Order_Date",
    "Customer",
    "Region",
    "Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Sales",
    "Cost",
    "Profit",
    "Customer_Segment",
    "Payment_Mode"
]

df = pd.DataFrame(data, columns=columns)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df = df.sort_values("Order_Date")

file_path = "data/sales_data.csv"

df.to_csv(file_path, index=False)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {file_path}")
print()
print(df.head())