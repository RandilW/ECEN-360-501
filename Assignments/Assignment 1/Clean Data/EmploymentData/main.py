import pandas as pd

# Load the data
df = pd.read_csv('acs_employment_data_fort_worth.csv')

# List of columns to convert to float
cols_to_convert = ['Estimate Total:', 'Margin of Error Total:', 'Estimate Total: In labor force:',
                   'Margin of Error Total: In labor force:', 'Estimate Total: In labor force: Civilian labor force:',
                   'Margin of Error Total: In labor force: Civilian labor force:',
                   'Estimate Total: In labor force: Civilian labor force: Employed',
                   'Margin of Error Total: In labor force: Civilian labor force: Employed',
                   'Estimate Total: In labor force: Civilian labor force: Unemployed',
                   'Margin of Error Total: In labor force: Civilian labor force: Unemployed',
                   'Estimate Total: In labor force: Armed Forces',
                   'Margin of Error Total: In labor force: Armed Forces',
                   'Estimate Total: Not in labor force', 'Margin of Error Total: Not in labor force']

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
df.to_csv('cleaned_acs_employment_data_fort_worth.csv', index=False)
