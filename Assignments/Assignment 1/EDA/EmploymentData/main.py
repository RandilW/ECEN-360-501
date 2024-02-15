# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_acs_employment_data_fort_worth.csv')  # replace 'cleaned_acs_employment_data_fort_worth.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot a histogram for the Estimate Total: In labor force: Civilian labor force: Employed
df['Estimate Total: In labor force: Civilian labor force: Employed'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of Employed Civilian Labor Force')
plt.xlabel('Number of Employed')
plt.ylabel('Number of ZIP Codes')
plt.savefig('employed_distribution.png')
plt.show()

# Count the number of employed in each ZIP Code
zip_counts = df['zip code tabulation area'].value_counts()
print(zip_counts)

# Plot the number of employed in each ZIP Code
zip_counts.plot(kind='bar', figsize=(10,5))
plt.title('Number of Employed in Each ZIP Code')
plt.xlabel('ZIP Code')
plt.ylabel('Number of Employed')
plt.savefig('employed_per_zip.png')
plt.show()
