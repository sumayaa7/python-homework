import pandas as pd

df = pd.read_csv("task\\sales_data.csv")
category_stats = df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
).reset_index()

print("🔹 Category Summary:")
print(category_stats)
top_products = (
    df.groupby(["Category", "Product"])["Quantity"]
    .sum()
    .reset_index()
    .sort_values(["Category", "Quantity"], ascending=[True, False])
)

top_product_each_category = top_products.groupby("Category").first().reset_index()

print("\n🔹 Top-Selling Product per Category:")
print(top_product_each_category)
df["TotalSales"] = df["Quantity"] * df["Price"]
date_max_sales = df.groupby("Date")["TotalSales"].sum().reset_index()
max_sales_date = date_max_sales.loc[date_max_sales["TotalSales"].idxmax()]

print("\n🔹 Date with Highest Total Sales:")
print(max_sales_date)


import pandas as pd
orders = pd.read_csv("task\\customer_orders.csv")


orders_per_customer = orders.groupby("CustomerID")["OrderID"].count().reset_index(name="OrderCount")
active_customers = orders_per_customer[orders_per_customer["OrderCount"] >= 20]
print("🔹 Customers with ≥ 20 orders:")
print(active_customers)


avg_price_per_customer = orders.groupby("CustomerID")["Price"].mean().reset_index(name="AvgPrice")
rich_customers = avg_price_per_customer[avg_price_per_customer["AvgPrice"] > 120]
print("\n🔹 Customers with Avg Price > $120:")
print(rich_customers)
product_summary = orders.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
).reset_index()

popular_products = product_summary[product_summary["total_quantity"] >= 5]
print("\n🔹 Products with Total Quantity ≥ 5:")
print(popular_products)


import pandas as pd
import sqlite3

conn = sqlite3.connect("task\\population.db")
population = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()


salary_bands = pd.read_excel("task\\population salary analysis.xlsx")
def categorize_salary(salary):
    for _, row in salary_bands.iterrows():
        if row["MinSalary"] <= salary < row["MaxSalary"]:
            return row["Band"]
    return "Unknown"

population["SalaryBand"] = population["Salary"].apply(categorize_salary)
band_stats = population.groupby("SalaryBand").agg(
    PopulationCount=("Salary", "count"),
    AverageSalary=("Salary", "mean"),
    MedianSalary=("Salary", "median")
).reset_index()

total_population = band_stats["PopulationCount"].sum()
band_stats["Percentage"] = (band_stats["PopulationCount"] / total_population * 100).round(2)

print("🔹 Overall Salary Band Statistics:")
print(band_stats)
state_band_stats = population.groupby(["State", "SalaryBand"]).agg(
    PopulationCount=("Salary", "count"),
    AverageSalary=("Salary", "mean"),
    MedianSalary=("Salary", "median")
).reset_index()
state_totals = state_band_stats.groupby("State")["PopulationCount"].transform("sum")
state_band_stats["Percentage"] = (state_band_stats["PopulationCount"] / state_totals * 100).round(2)
print("\n🔹 Salary Band Statistics per State:")
print(state_band_stats)


