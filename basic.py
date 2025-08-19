import pandas as pd

# Load the dataset (update the path with your local file path if needed)
df = pd.read_excel('mobile_usage_behavioral_analysis.xlsx')

# Display first few rows
print(df.head())

# Get general info about the dataset
print(df.info())

# Check descriptive statistics for numeric columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())
