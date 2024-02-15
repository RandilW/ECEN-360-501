import pandas as pd

# Load the data
df = pd.read_csv('means_of_transportation.csv')

# List of columns to convert to float
cols_to_convert = df.columns[2:]  # Assuming all columns after the second one should be numeric

# Convert to float for the selected columns
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# fill NaN values with the mean for the selected columns
for col in cols_to_convert:
    df[col] = df[col].fillna(df[col].mean())

# Save the cleaned data
df.to_csv('cleaned_means_of_transportation.csv', index=False)
