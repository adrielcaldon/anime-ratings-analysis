import pandas as pd
import sqlite3
import os

print("🧪 RUNNING UPDATED SQLITE SCRIPT")
# Load cleaned CSV
csv_path = "data/cleaned_anime.csv"
df = pd.read_csv(csv_path)

# Connect to SQLite database (creates it if it doesn't exist)
db_path = "data/anime.db"
conn = sqlite3.connect(db_path)

# Load data into a table
table_name = "anime"
df.to_sql(table_name, conn, if_exists="replace", index=False)

# ✅ Add this confirmation
print(f"✅ Loaded {len(df)} rows into '{table_name}' table in {db_path}")

# Optional: preview a few rows
preview = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5", conn)
print("📊 Sample rows:")
print(preview)

conn.close()