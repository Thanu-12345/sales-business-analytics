import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create dashboard
fig = plt.figure(figsize=(16, 10))

# 1. Monthly Sales
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

ax1 = plt.subplot(2, 2, 1)
monthly_sales.plot(ax=ax1)

ax1.set_title("Monthly Sales Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")

# 2. Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

ax2 = plt.subplot(2, 2, 2)
region_sales.plot(kind="bar", ax=ax2)

ax2.set_title("Sales by Region")
ax2.set_xlabel("Region")
ax2.set_ylabel("Sales")
ax2.tick_params(axis="x", rotation=0)

# 3. Sales by Category
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

ax3 = plt.subplot(2, 2, 3)
category_sales.plot(kind="bar", ax=ax3)

ax3.set_title("Sales by Category")
ax3.set_xlabel("Category")
ax3.set_ylabel("Sales")
ax3.tick_params(axis="x", rotation=0)

# 4. Profit by Customer Segment
segment_profit = (
    df.groupby("Customer_Segment")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

ax4 = plt.subplot(2, 2, 4)
segment_profit.plot(kind="bar", ax=ax4)

ax4.set_title("Profit by Customer Segment")
ax4.set_xlabel("Customer Segment")
ax4.set_ylabel("Profit")
ax4.tick_params(axis="x", rotation=0)

plt.suptitle(
    "Sales & Business Analytics Dashboard",
    fontsize=18
)

plt.tight_layout()

# Save dashboard
plt.savefig(
    "images/sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Dashboard created successfully!")
print("Saved to: images/sales_dashboard.png")