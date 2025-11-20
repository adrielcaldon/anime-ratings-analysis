# etl_load_sqlite.py

import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/cleaned_anime.csv")

# Connect to SQLite (use same DB path as other scripts)
conn = sqlite3.connect("data/anime.db")

# Load into SQL table
df.to_sql("anime", conn, if_exists="replace", index=False)

# Test query
query = """
SELECT english AS name, score AS rating
FROM anime
WHERE score > 8.5
ORDER BY score DESC
LIMIT 10
"""
top_anime = pd.read_sql(query, conn)
print("🏆 Top-rated anime (by score):")
print(top_anime)

conn.close()