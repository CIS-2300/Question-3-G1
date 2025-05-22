import pandas as pd

# File paths for all four teams
files = {
    "Men Swimming": "/Users/stevenshi/Documents/men_swimming_players_heights.csv",
    "Men Volleyball": "/Users/stevenshi/Documents/men_volleyball_players_heights.csv",
    "Women Swimming": "/Users/stevenshi/Documents/women_swimming_players_heights.csv",
    "Women Volleyball": "/Users/stevenshi/Documents/women_volleyball_players_heights.csv"
}

averages = {}

# Read each CSV and compute the average height
for team, file in files.items():
    df = pd.read_csv(file)
    averages[team] = df['Height_in'].mean()  # Use the correct column name

# Print the average height for each team
for team, avg in averages.items():
    print(f"Average height for {team}: {avg:.2f} inches")

