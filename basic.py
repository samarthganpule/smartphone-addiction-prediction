import pandas as pd

# Load the data (replace filename if needed)
df = pd.read_excel('mobile_usage_behavioral_analysis.xlsx')

# Optional: Fill or drop missing values as needed
df = df.fillna(df.mean(numeric_only=True))  # Fills missing numeric values with the mean

# Optional: Remove duplicate rows
df = df.drop_duplicates()

# Save the cleaned DataFrame for use in EDA
df.to_pickle("cleaned_data.pkl")  # Saves df as a binary file for fast loading

# Print column names for reference
print("Columns in dataset:", df.columns.tolist())


# import pandas as pd

# # Load the dataset (update the path with your local file path if needed)
# df = pd.read_excel('mobile_usage_behavioral_analysis.xlsx')

# # # Display first few rows
# # print(df.head())

# # # Get general info about the dataset
# # print(df.info())

# # # Check descriptive statistics for numeric columns
# # print(df.describe())

# # # Check for missing values
# # print(df.isnull().sum())

# # Remove rows with any missing values (if missing values are few)
# df_clean = df.dropna()

# # Alternatively, fill missing values (if critical columns have gaps)
# # Example: fill missing numerical values with column mean
# df_filled = df.fillna(df.mean(numeric_only=True))

# # Remove duplicate rows
# df_clean = df_clean.drop_duplicates()

# # Check the shape after cleaning
# print("Shape after cleaning:", df_clean.shape)

# # Inspect to confirm
# print(df_clean.info())





