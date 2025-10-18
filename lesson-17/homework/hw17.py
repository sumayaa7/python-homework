#Task1
import pandas as pd
import numpy as np

#DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

print("First 3 rows:\n", df.head(3), "\n")

print("Mean age:", df['age'].mean(), "\n")

print("Name and City columns:\n", df[['first_name', 'City']], "\n")

df['Salary'] = np.random.randint(40000, 90000, size=len(df))
print("DataFrame with Salary:\n", df, "\n")

print("Summary statistics:\n", df.describe(include='all'))


#Task2
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

print("Maximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max(), "\n")

print("Minimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min(), "\n")

print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


#Task3
import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

expenses = expenses.set_index('Category')

print("Maximum expenses per category:\n", expenses.max(axis=1), "\n")

print("Minimum expenses per category:\n", expenses.min(axis=1), "\n")

print("Average expenses per category:\n", expenses.mean(axis=1))

