import pandas as pd
import matplotlib.pyplot as plt

# latin1 encoding needed here - the default utf-8 fails on this file, likely
# due to special characters in some of the text fields.
df = pd.read_csv("Superstore.csv", encoding="latin1")

# Convert Order Date from text to an actual datetime type so year/month can
# be pulled out of it - a plain text column can't be broken into date parts.
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Plotting order COUNT per month, not total or average sales. An earlier
# version of this chart plotted total sales, which made it look like sales
# increased in Sept/Nov/Dec because individual orders got bigger. Checking
# mean vs. median per month (see agg() below) showed that wasn't true - the
# real driver is more orders happening in those months, not bigger orders.
monthly_sales = df.groupby("Month")["Sales"].count()
monthly_sales.index = [f"{month}" for month in monthly_sales.index]
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.title("Order Count by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# agg() computes multiple stats per group in one call. Comparing mean vs.
# median here is what revealed March's mean was being skewed by a handful of
# large outlier orders rather than reflecting a genuine seasonal pattern.
print(df.groupby("Month")["Sales"].agg(["mean", "median", "count"]))

"""
Total sales are highest in September, November, and December - but this is driven
primarily by a higher NUMBER of orders in those months (e.g. 1,383 orders in
September vs. ~300-750 in most other months), not by individual orders being
larger. The median order size stays roughly flat across all months (~$47-60),
showing no real seasonal change in typical purchase size. The high MEAN in
March ($294 vs. a $59 median) is a separate effect - a small number of very
large outlier orders skewing the average, not a genuine trend.
"""