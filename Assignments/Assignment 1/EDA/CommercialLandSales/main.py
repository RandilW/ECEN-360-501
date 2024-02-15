# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_commercial_land_sales.csv')  # replace 'cleaned_commercial_land_sales.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot a histogram for the SalePricePAC (Price Per Acre)
df['SalePricePAC'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of Sale Price Per Acre')
plt.xlabel('Sale Price Per Acre')
plt.ylabel('Number of Sales')
plt.savefig('sale_price_per_acre_distribution.png')
plt.show()

# Count the number of sales in each ZIP Code
zip_counts = df['GeoCd'].value_counts()
print(zip_counts)

# Plot the number of sales in each ZIP Code
zip_counts.plot(kind='bar', figsize=(10,5))
plt.title('Number of Sales in Each ZIP Code')
plt.xlabel('ZIP Code')
plt.ylabel('Number of Sales')
plt.savefig('sales_per_zip.png')
plt.show()
