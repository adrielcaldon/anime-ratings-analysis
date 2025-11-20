import pandas as pd
import os

print("🧪 THIS IS THE UPDATED SCRIPT")
print("📁 Current directory:", os.getcwd())

csv_path = "data/Top_Anime_data.csv"

if not os.path.exists(csv_path):
    print(f"❌ File not found: {csv_path}")
    exit()

print("✅ File found. Loading...")

df = pd.read_csv(csv_path)
print("🧾 Columns:", df.columns.tolist())
print("📊 Raw data preview:")
print(df.head())

df = df.dropna(subset=["Score"])
df["Score"] = pd.to_numeric(df["Score"], errors="coerce")
df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

df.to_csv("data/cleaned_anime.csv", index=False)
print("✅ Cleaned data saved to data/cleaned_anime.csv")