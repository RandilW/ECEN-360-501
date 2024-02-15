# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_census_data.csv')

# relevant columns for the restaurant business
relevant_columns = ['Total Population', 'Median Household Income', 'Employed', 'Total Households', 'Average Household Size', 'ZIP_Code']
df = df[relevant_columns]

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot histograms for each relevant numerical attribute
df.hist(bins=50, figsize=(20,15))
plt.savefig('census_histogram.png')
plt.show()

# Check for correlation among attributes
corr_matrix = df.corr()

# Create a larger figure
plt.figure(figsize=(14, 14))

# Create a heatmap with seaborn
sns.heatmap(corr_matrix, annot=True, fmt=".2f", square=True)

# Rotate the x-axis labels
plt.xticks(rotation=45)

# Rotate the y-axis labels
plt.yticks(rotation=45)

plt.savefig('census_heatmap.png')

# Show the plot
plt.show()
