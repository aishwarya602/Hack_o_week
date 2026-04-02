import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("ai4i2020.csv")

print(df.head())

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

# Simulated "proximity risk" feature
df['stress_index'] = (
    0.4 * df['Air temperature [K]'] +
    0.3 * df['Process temperature [K]'] +
    0.2 * df['Torque [Nm]'] +
    0.1 * df['Tool wear [min]']
)

# Normalize stress index
df['stress_index'] = (df['stress_index'] - df['stress_index'].min()) / \
                     (df['stress_index'].max() - df['stress_index'].min())

# Binary proximity risk (like geofence breach)
df['high_risk'] = df['stress_index'] > 0.7

# -----------------------------
# FEATURES & TARGET
# -----------------------------
X = df[['Air temperature [K]', 'Process temperature [K]',
        'Torque [Nm]', 'Tool wear [min]', 'stress_index']]

y = df['Machine failure']   # target

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# MODEL TRAINING
# -----------------------------
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# -----------------------------
# PREDICTIONS
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# EVALUATION
# -----------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['stress_index'], label='Stress Index')
plt.title("Engineered Proximity (Stress) Trend")
plt.legend()
plt.show()

# Feature importance
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, importances)
plt.title("Feature Importance")
plt.show()