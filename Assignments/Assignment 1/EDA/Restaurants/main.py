# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_restaurants.csv')  # replace 'cleaned_restaurants.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the numerical data
print(df.describe())

# Plot a histogram for the ratings
df['Rating'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Restaurants')
plt.savefig('ratings_distribution.png')
plt.show()

# Plot a histogram for the user ratings total
df['User Ratings Total'].hist(bins=20, figsize=(10,5))
plt.title('Distribution of User Ratings Total')
plt.xlabel('User Ratings Total')
plt.ylabel('Number of Restaurants')
plt.savefig('user_ratings_total_distribution.png')
plt.show()

# Count the number of restaurants in each ZIP Code
zip_counts = df['ZIP Code'].value_counts()
print(zip_counts)

# Plot the number of restaurants in each ZIP Code
zip_counts.plot(kind='bar', figsize=(10,8))
plt.title('Number of Existing Mediterranean Restaurants in Each ZIP Code')
plt.xlabel('ZIP Code')
plt.ylabel('Number of Restaurants')
plt.savefig('restaurants_per_zip.png')
plt.show()
