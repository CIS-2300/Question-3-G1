import pandas as pd
import sqlite3

# Connect to SQLite database (creates if it doesn't exist)
conn = sqlite3.connect("/Users/stevenshi/Documents/athletes.db")
cursor = conn.cursor()

# Your CSV file paths
datasets = {
    "men_swimming": "/Users/stevenshi/Documents/men_swimming_players_heights.csv",
    "women_swimming": "/Users/stevenshi/Documents/women_swimming_players_heights.csv",
    "men_volleyball": "/Users/stevenshi/Documents/men_volleyball_players_heights.csv",
    "women_volleyball": "/Users/stevenshi/Documents/women_volleyball_players_heights.csv"
}

# Read each CSV and insert into a table
for table_name, csv_path in datasets.items():
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"{table_name} table created.")

conn.close()
print("Database created at ~/Documents/athletes.db")

