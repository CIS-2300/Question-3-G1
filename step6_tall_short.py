import pandas as pd
import re

# Define paths to your CSV files (update paths if needed)
paths = {
    'men_swimming': '/Users/stevenshi/Documents/men_swimming_players_heights.csv',
    'women_swimming': '/Users/stevenshi/Documents/women_swimming_players_heights.csv',
    'men_volleyball': '/Users/stevenshi/Documents/men_volleyball_players_heights.csv',
    'women_volleyball': '/Users/stevenshi/Documents/women_volleyball_players_heights.csv',
}

def convert_height_to_inches(height_str):
    """
    Convert height from format '6-2' or '6′2″' etc. into inches.
    Returns int or None if format invalid.
    """
    # Match patterns like 6-2, 6'2", 6′2″ etc.
    match = re.search(r"(\d)[-′']\s?(\d{1,2})", height_str)
    if match:
        feet = int(match.group(1))
        inches = int(match.group(2))
        return feet * 12 + inches
    else:
        return None

for category, path in paths.items():
    try:
        print(f"\nReading data for {category} from {path}")
        df = pd.read_csv(path)
        
        # Check if 'Height' column exists
        if 'Height' not in df.columns:
            print(f"ERROR: No 'Height' column in {category} data.")
            continue
        
        # Convert Height strings to inches
        df['Height_in_inches'] = df['Height'].apply(convert_height_to_inches)
        
        # Drop rows where height conversion failed
        df = df.dropna(subset=['Height_in_inches'])
        
        # Find tallest and shortest
        tallest = df.loc[df['Height_in_inches'].idxmax()]
        shortest = df.loc[df['Height_in_inches'].idxmin()]
        
        print(f"Tallest player in {category}: {tallest['Name']} - {tallest['Height']} ({tallest['Height_in_inches']} inches)")
        print(f"Shortest player in {category}: {shortest['Name']} - {shortest['Height']} ({shortest['Height_in_inches']} inches)")
        
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error processing {category}: {e}")
