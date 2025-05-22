import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and labels
files = {
    "Men Swimming": "/Users/stevenshi/Documents/men_swimming_players_heights.csv",
    "Men Volleyball": "/Users/stevenshi/Documents/men_volleyball_players_heights.csv",
    "Women Swimming": "/Users/stevenshi/Documents/women_swimming_players_heights.csv",
    "Women Volleyball": "/Users/stevenshi/Documents/women_volleyball_players_heights.csv"
}

# Compute average heights
averages = {}
for team, filepath in files.items():
    df = pd.read_csv(filepath)
    averages[team] = df["Height_in"].mean()

# Plot the bar chart
plt.figure(figsize=(8, 6))
plt.bar(averages.keys(), averages.values(), color=["blue", "green", "purple", "orange"])
plt.ylabel("Average Height (inches)")
plt.title("Average Heights by Team")
plt.xticks(rotation=15)
plt.tight_layout()

# Save the figure
output_path = "/Users/stevenshi/Documents/average_heights_bar_chart.png"
plt.savefig(output_path)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Define file paths and labels
files = {
    "Men Swimming": "/Users/stevenshi/Documents/men_swimming_players_heights.csv",
    "Men Volleyball": "/Users/stevenshi/Documents/men_volleyball_players_heights.csv",
    "Women Swimming": "/Users/stevenshi/Documents/women_swimming_players_heights.csv",
    "Women Volleyball": "/Users/stevenshi/Documents/women_volleyball_players_heights.csv"
}

# Compute average heights
averages = {}
for team, filepath in files.items():
    df = pd.read_csv(filepath)
    averages[team] = df["Height_in"].mean()

# Plot the bar chart
plt.figure(figsize=(8, 6))
plt.bar(averages.keys(), averages.values(), color=["blue", "green", "purple", "orange"])
plt.ylabel("Average Height (inches)")
plt.title("Average Heights by Team")
plt.xticks(rotation=15)
plt.tight_layout()

# Save the figure
output_path = "/Users/stevenshi/Documents/average_heights_bar_chart.png"
plt.savefig(output_path)
plt.show()

