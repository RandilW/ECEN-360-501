# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_means_of_transportation.csv')  # replace 'cleaned_means_of_transportation.csv' with your actual file name

# Display the first few rows of the DataFrame
print(df.head())

# Plot the total number of workers in each zip code
plt.figure(figsize=(10,5))
df.groupby('zipcode')['Total:'].sum().plot(kind='bar')
plt.title('Total Number of Workers in Each Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Total Number of Workers')
plt.savefig('total_workers_per_zip.png')
plt.show()

# Plot the number of people who drive alone to work in each zip code
plt.figure(figsize=(10,5))
df.groupby('zipcode')['Drove alone'].sum().plot(kind='bar')
plt.title('Number of People Who Drive Alone to Work in Each Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Number of People Who Drive Alone')
plt.savefig('drive_alone_per_zip.png')
plt.show()

# Use a horizontal bar chart
plt.figure(figsize=(10,5))
df.groupby('zipcode')['Total:'].sum().sort_values().plot(kind='barh')
plt.title('Total Number of Workers in Each Zip Code')
plt.xlabel('Total Number of Workers')
plt.ylabel('Zip Code')
plt.savefig('total_workers_per_zip_horizontal.png')
plt.show()

# Display a subset of the data
top_10_zip_codes = df.groupby('zipcode')['Drove alone'].sum().sort_values(ascending=False).head(20)
plt.figure(figsize=(10,8))
top_10_zip_codes.plot(kind='bar')
plt.title('Total Number of People Who Drive to Work in Top 10 Zip Codes')
plt.xlabel('Zip Code')
plt.ylabel('Total Number of People Who Drive')
plt.savefig('total_drove_top_10_zip.png')
plt.show()
