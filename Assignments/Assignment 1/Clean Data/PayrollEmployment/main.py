import pandas as pd

# Load the data
df = pd.read_csv('payroll_employment.csv')

# List of columns to convert to float
cols_to_convert = ['Employment (in thousands)', 'Monthly change (in thousands)',
                   'M/M Annualized Pct Change', 'Dec/Dec Pct Change']

# Convert to float for the selected columns
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# fill NaN values with the mean for the selected columns
for col in cols_to_convert:
    df[col] = df[col].fillna(df[col].mean())

# Save the cleaned data
df.to_csv('cleaned_payroll_employment.csv', index=False)
