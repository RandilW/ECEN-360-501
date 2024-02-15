import pandas as pd

# Load the data
df = pd.read_csv('transportation.csv')

# List of columns to convert to float
cols_to_convert = [col for col in df.columns if 'Estimate' in col or 'Margin of Error' in col]

# Convert to float for the selected columns
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Now you can fill NaN values with the mean for the selected columns
for col in cols_to_convert:
    df[col] = df[col].fillna(df[col].mean())

# Remove columns with no data
df = df.dropna(axis=1, how='all')

# Save the cleaned data
df.to_csv('cleaned_transportation.csv', index=False)
