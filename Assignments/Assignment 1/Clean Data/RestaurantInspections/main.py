import pandas as pd

# Load the data
df = pd.read_csv('restaurant_inspections.csv')

# Check for missing values
print(df.isnull().sum())

df['# Inspections'] = df['# Inspections'].fillna(df['# Inspections'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())
df['Last Inspection'] = df['Last Inspection'].fillna(df['Last Inspection'].mode()[0])

# Save the cleaned data
df.to_csv('cleaned_restaurant_inspections.csv', index=False)
