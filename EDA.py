import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_pickle("cleaned_data.pkl")


# 1. Distribution of Daily Screen Time
plt.figure(figsize=(8, 5))
sns.histplot(df['Daily_Screen_Time_Hours'], bins=30, kde=True)
plt.title('Distribution of Daily Screen Time (Hours)')
plt.xlabel('Daily Screen Time (Hours)')
plt.ylabel('Frequency')
plt.show()


# 2. Correlation Heatmap (Only numeric columns)
numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (Numeric Features Only)')
plt.show()

# 3. Average Screen Time by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='Daily_Screen_Time_Hours', data=df)
plt.title('Daily Screen Time by Gender')
plt.show()

# 4. Number of Users by Location
plt.figure(figsize=(10, 5))
sns.countplot(x='Location', data=df, order=df['Location'].value_counts().index)
plt.title('User Distribution by City')
plt.xlabel('City')
plt.ylabel('User Count')
plt.xticks(rotation=45)
plt.show()
