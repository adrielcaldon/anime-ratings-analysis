import pandas as pd
import os

# Set path to CSV
csv_path = os.path.join("..", "data", "anime.csv")

# Load data
df = pd.read_csv(csv_path)

# Quick look
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

# Basic cleaning
df.dropna(subset=['rating'], inplace=True)
df['genre'] = df['genre'].fillna('Unknown')

# Save cleaned version
cleaned_path = os.path.join("..", "data", "anime_cleaned.csv")
df.to_csv(cleaned_path, index=False)

print("Cleaned data saved to:", cleaned_path)