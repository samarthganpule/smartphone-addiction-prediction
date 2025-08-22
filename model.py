import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_pickle('cleaned_data.pkl')

# 2. Define 'Addicted' label (customizable threshold)
df['Addicted'] = (df['Daily_Screen_Time_Hours'] > 6).astype(int)  # Adjust threshold as you wish

# 3. Select features (columns used for prediction)
features = [
    'Age',
    'Total_App_Usage_Hours',
    'Number_of_Apps_Used',
    'Social_Media_Usage_Hours',
    'Productivity_App_Usage_Hours',
    'Gaming_App_Usage_Hours'
]

X = df[features]
y = df['Addicted']

# 4. Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Build Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Predict and evaluate
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Feature Importance
importances = model.feature_importances_
plt.figure(figsize=(8,4))
plt.barh(features, importances)
plt.title('Feature Importance')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.show()
