import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (adjust the file name/path accordingly)
df = pd.read_excel('filename.xlsx')

# Fill missing numeric values with mean (adjust as needed)
df = df.fillna(df.mean(numeric_only=True))

# Example: Plot distribution of a numeric feature
if 'total_screen_time' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['total_screen_time'], bins=30, kde=True)
    plt.title('Distribution of Total Screen Time')
    plt.xlabel('Total Screen Time (minutes)')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Column 'total_screen_time' not found!")

# Plot correlation heatmap of numeric features
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Example: Boxplot by category if categorical column exists (adjust 'user_category')
if 'user_category' in df.columns and 'total_screen_time' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='user_category', y='total_screen_time', data=df)
    plt.title('Screen Time by User Category')
    plt.show()
else:
    print("Columns 'user_category' or 'total_screen_time' not found for boxplot!")
