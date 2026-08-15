import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].count()
monthly_sales.index = [f"{month}" for month in monthly_sales.index]
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.title("Order Count by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(df.groupby("Month")["Sales"].agg(["mean", "median", "count"]))
"""
Total sales are highest in September, November, and December — but this is driven
primarily by a higher NUMBER of orders in those months (e.g. 1,383 orders in
September vs. ~300-750 in most other months), not by individual orders being
larger. The median order size stays roughly flat across all months (~$47-60),
showing no real seasonal change in typical purchase size. The high MEAN in
March ($294 vs. a $59 median) is a separate effect - a small number of very
large outlier orders skewing the average, not a genuine trend.
"""