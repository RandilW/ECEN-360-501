# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_income_by_location.csv')  # replace 'cleaned_income_by_location.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot a histogram for the Household Income by Race
df['Household Income by Race'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of Household Income by Race')
plt.xlabel('Household Income')
plt.ylabel('Number of Census Tracts')
plt.savefig('income_distribution.png')
plt.show()

# Count the number of census tracts in each Geography
geo_counts = df['Geography'].value_counts()
print(geo_counts)

# Plot the number of census tracts in each Geography
geo_counts.plot(kind='bar', figsize=(10,5))
plt.title('Number of Census Tracts in Each Geography')
plt.xlabel('Geography')
plt.ylabel('Number of Census Tracts')
plt.savefig('tracts_per_geo.png')
plt.show()
