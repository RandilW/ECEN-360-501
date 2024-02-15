# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_restaurant_inspections.csv')  # replace 'cleaned_restaurant_inspections.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot a histogram for the scores
df['Score'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of Inspection Scores')
plt.xlabel('Score')
plt.ylabel('Number of Restaurants')
plt.savefig('inspection_scores_distribution.png')
plt.show()