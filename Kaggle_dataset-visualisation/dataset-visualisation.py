import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset (update path)
df = pd.read_csv("6S55F.csv")

# Preview
print(df.head())

# DATA PREPROCESSING


# Convert timestamp column (modify column name if needed)
df['datetime'] = pd.to_datetime(df['datetime'])

# Sort by time
df = df.sort_values(by='datetime')

# Handle missing values
df = df.ffill() # Updated from df.fillna(method='ffill') to df.ffill()


# SELECT DISTANCE COLUMN

# Replace 'distance' with actual column name
temp_col = 'temperature'
# Assign distance_col to the intended column, which is 'temperature'
distance_col = temp_col


# VISUALIZATION

plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df[distance_col])

plt.title("Distance vs Time (Proximity Trend)")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.xticks(rotation=45)
plt.grid()

plt.show()

# COMPUTE AVERAGES


# Overall average
avg_distance = df[distance_col].mean()
print("Average Distance:", avg_distance)

# Rolling average (smooth trend)
df['rolling_avg'] = df[distance_col].rolling(window=10).mean()

# Plot rolling average
plt.figure(figsize=(12, 6))
# Use 'datetime' for the x-axis as 'timestamp' is not present in the dataframe
plt.plot(df['datetime'], df[distance_col], label="Raw Data")
plt.plot(df['datetime'], df['rolling_avg'], label="Rolling Avg (Smooth)")

plt.legend()
plt.title("Smoothed Distance Trend")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.grid()

plt.show()

# INCIDENT DETECTION


# Define threshold
threshold = 50  # adjust

df['alert'] = df[distance_col] < threshold

# Count incidents
incident_count = df['alert'].sum()
print("Number of close-distance incidents:", incident_count)