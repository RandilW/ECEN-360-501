import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('census_data.csv')

# Identify numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Replace negative values with NaN in numeric columns only
df[numeric_cols] = df[numeric_cols].apply(lambda x: x.where(x >= 0))

# Fill missing numeric data with the median of that column
for column in numeric_cols:
    if df[column].count() > 0:  # Check if there are any non-NaN values
        df[column] = df[column].fillna(df[column].median())
    else:
        df[column] = df[column].fillna(0)  # If all values are NaN, fill with 0 or another value of your choice

# Save the cleaned data
df.to_csv('cleaned_census_data.csv', index=False)
