import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV
canteen_df = pd.read_csv("canteen_sales_data.csv")

# Convert to datetime
canteen_df["Date"] = pd.to_datetime(canteen_df["Date"])
canteen_df["Time"] = pd.to_datetime(canteen_df["Time"], format="%H:%M").dt.time

# Extract hour properly using known format
canteen_df["Hour"] = pd.to_datetime(canteen_df["Time"].astype(str), format="%H:%M:%S").dt.hour

# Data prep
top_items = canteen_df.groupby("Item")["Quantity"].sum().sort_values(ascending=False).head(5)
daily_sales = canteen_df.groupby("Date")["Total_Price"].sum()
hourly_sales = canteen_df.groupby("Hour")["Quantity"].sum()
category_income = canteen_df.groupby("Category")["Total_Price"].sum()

# Plotting
plt.figure(figsize=(16, 12))

# Top Selling Items
plt.subplot(2, 2, 1)
top_items.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 5 Selling Items")
plt.ylabel("Total Quantity Sold")
plt.xlabel("Item")
plt.xticks(rotation=45)

# Daily Sales Trend
plt.subplot(2, 2, 2)
daily_sales.plot(kind="line", marker="o", linestyle="-", color="green")
plt.title("Total Sales Per Day")
plt.ylabel("Revenue (₹)")
plt.xlabel("Date")
plt.xticks(rotation=45)

# Most Active Hours
plt.subplot(2, 2, 3)
hourly_sales.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Most Active Hours")
plt.xlabel("Hour of the Day")
plt.ylabel("Items Sold")

# Income by Category
plt.subplot(2, 2, 4)
category_income.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=["lightcoral", "lightblue", "lightgreen"])
plt.title("Revenue by Category")
plt.ylabel("")

plt.tight_layout()
plt.show()
