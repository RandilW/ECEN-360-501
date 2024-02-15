# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a pandas DataFrame df
df = pd.read_csv('cleaned_payroll_employment.csv')  # replace 'cleaned_payroll_employment.csv' with your actual file name

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')

# Display the first few rows of the DataFrame
print(df.head())

# Plot the total employment over time
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Employment (in thousands)'])
plt.title('Total Employment Over Time')
plt.xlabel('Date')
plt.ylabel('Employment (in thousands)')
plt.savefig('employment_over_time.png')
plt.show()

# Plot the monthly change in employment over time
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Monthly change (in thousands)'])
plt.title('Monthly Change in Employment Over Time')
plt.xlabel('Date')
plt.ylabel('Monthly change (in thousands)')
plt.savefig('monthly_change_over_time.png')
plt.show()
