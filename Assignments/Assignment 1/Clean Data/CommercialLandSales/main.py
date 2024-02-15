import pandas as pd

# Load the data
df = pd.read_csv('commercial_land_sales.csv')

# Remove commas and dollar signs, then convert to float
df['SalePrice'] = df['SalePrice'].str.replace(',', '').str.replace('$', '').astype(float)
df['SalePricePSF'] = df['SalePricePSF'].str.replace('$', '').astype(float)
df['SalePricePAC'] = df['SalePricePAC'].str.replace(',', '').str.replace('$', '').astype(float)

# Convert 'LandSizeSF', 'LandSizeAc' to string, remove commas, then convert to float
df['LandSizeSF'] = df['LandSizeSF'].astype(str).str.replace(',', '').astype(float)
df['LandSizeAc'] = df['LandSizeAc'].astype(str).str.replace(',', '').astype(float)

# fill NaN values with the mean
df['LandSizeSF'] = df['LandSizeSF'].fillna(df['LandSizeSF'].mean())
df['LandSizeAc'] = df['LandSizeAc'].fillna(df['LandSizeAc'].mean())
df['SalePrice'] = df['SalePrice'].fillna(df['SalePrice'].mean())
df['SalePricePSF'] = df['SalePricePSF'].fillna(df['SalePricePSF'].mean())
df['SalePricePAC'] = df['SalePricePAC'].fillna(df['SalePricePAC'].mean())

# Save the cleaned data
df.to_csv('cleaned_commercial_land_sales.csv', index=False)
