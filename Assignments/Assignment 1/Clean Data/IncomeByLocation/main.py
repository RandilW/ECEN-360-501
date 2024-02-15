import pandas as pd

# Load the data
df = pd.read_csv('income_by_location.csv')

# List of columns to convert to float
cols_to_convert = ['Household Income by Race', 'Household Income by Race Moe']

# Remove commas and convert to float for the selected columns
for col in cols_to_convert:
    if df[col].dtype == 'object':
        df[col] = df[col].str.replace(',', '').astype(float)

# fill NaN values with the mean for the selected columns
for col in cols_to_convert:
    df[col] = df[col].fillna(df[col].mean())

# Remove columns with no data
df = df.dropna(axis=1, how='all')

# Save the cleaned data
df.to_csv('cleaned_income_by_location.csv', index=False)
