import pandas as pd

# Load dataset
df = pd.read_csv('sales_data.csv')

# Show first rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True)

# Analysis
total_sales = df['Total_Sales'].sum()
avg_sales = df['Total_Sales'].mean()
max_sales = df['Total_Sales'].max()

# Best product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Results
print("\n--- Results ---")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{avg_sales:,.2f}")
print(f"Highest Sale: ₹{max_sales:,.2f}")
print(f"Best Product: {best_product}")
