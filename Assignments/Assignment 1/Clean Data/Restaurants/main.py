import pandas as pd

# Load the data
df = pd.read_csv('restaurants.csv')

# Check for missing values
print(df.isnull().sum())

df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['User Ratings Total'] = df['User Ratings Total'].fillna(df['User Ratings Total'].mean())
df['Price Level'] = df['Price Level'].fillna(df['Price Level'].mode()[0])

# Save the cleaned data
df.to_csv('cleaned_restaurants.csv', index=False)
