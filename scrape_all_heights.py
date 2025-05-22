import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Dictionary of URLs grouped by category
urls = {
    'men_volleyball': [
        'https://ccnyathletics.com/sports/mens-volleyball/roster',
        'https://lehmanathletics.com/sports/mens-volleyball/roster',
        'https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster',
        'https://johnjayathletics.com/sports/mens-volleyball/roster',
        'https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster',
        'https://mecathletics.com/sports/mens-volleyball/roster',
        'https://www.huntercollegeathletics.com/sports/mens-volleyball/roster',
        'https://yorkathletics.com/sports/mens-volleyball/roster',
        'https://ballstatesports.com/sports/mens-volleyball/roster',
    ],
    'women_volleyball': [
        'https://bmccathletics.com/sports/womens-volleyball/roster',
        'https://yorkathletics.com/sports/womens-volleyball/roster',
        'https://hostosathletics.com/sports/womens-volleyball/roster',
        'https://bronxbroncos.com/sports/womens-volleyball/roster/2021',
        'https://queensknights.com/sports/womens-volleyball/roster',
        'https://augustajags.com/sports/wvball/roster',
        'https://flaglerathletics.com/sports/womens-volleyball/roster',
        'https://pacersports.com/sports/womens-volleyball/roster',
        'https://www.golhu.com/sports/womens-volleyball/roster',
    ],
    'men_swimming': [
        'https://csidolphins.com/sports/mens-swimming-and-diving/roster',
        'https://yorkathletics.com/sports/mens-swimming-and-diving/roster',
        'https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster',
        'https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster',
        'https://lindenwoodlions.com/sports/mens-swimming-and-diving/roster',
        'https://mckbearcats.com/sports/mens-swimming-and-diving/roster',
        'https://ramapoathletics.com/sports/mens-swimming-and-diving/roster',
        'https://oneontaathletics.com/sports/mens-swimming-and-diving/roster',
        'https://bubearcats.com/sports/mens-swimming-and-diving/roster/2021-22',
        'https://albrightathletics.com/sports/mens-swimming-and-diving/roster/2021-22',
    ],
    'women_swimming': [
        'https://csidolphins.com/sports/womens-swimming-and-diving/roster',
        'https://queensknights.com/sports/womens-swimming-and-diving/roster',
        'https://yorkathletics.com/sports/womens-swimming-and-diving/roster',
        'https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster/2021-22?path=wswim',
        'https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster',
        'https://lindenwoodlions.com/sports/womens-swimming-and-diving/roster',
        'https://mckbearcats.com/sports/womens-swimming-and-diving/roster',
        'https://ramapoathletics.com/sports/womens-swimming-and-diving/roster',
        'https://keanathletics.com/sports/womens-swimming-and-diving/roster',
        'https://oneontaathletics.com/sports/womens-swimming-and-diving/roster',
    ]
}

def convert_height_to_inches(height_str):
    # Match feet-inches format like 6-2, 5'11", 6′2″, etc.
    match = re.search(r"(\d)[-′']\s?(\d{1,2})", height_str)
    if match:
        feet = int(match.group(1))
        inches = int(match.group(2))
        return feet * 12 + inches
    # Also try just feet or just inches if needed (optional)
    return None

def scrape_heights_raw(url):
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    players = []

    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        # Try to find name and height columns by heuristics
        # Assuming name is in the first col and height is nearby
        if len(cols) < 2:
            continue
        name = cols[0].get_text(strip=True)
        height = None
        # Search through columns for something that looks like height
        for col in cols:
            text = col.get_text(strip=True)
            if re.search(r"\d[-′']\d{1,2}", text):  # crude height pattern
                height = text
                break
        if name and height:
            players.append({'Name': name, 'Height': height})

    return pd.DataFrame(players)

def scrape_all(url_list):
    dfs = []
    for url in url_list:
        df = scrape_heights_raw(url)
        dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame(columns=['Name', 'Height'])

def convert_heights(df):
    df['Height_in'] = df['Height'].apply(convert_height_to_inches)
    return df

def main():
    for category, url_list in urls.items():
        df = scrape_all(url_list)
        df = convert_heights(df)
        # Drop rows with no valid height
        df_clean = df.dropna(subset=['Height_in'])
        # Calculate average height
        avg_height = df_clean['Height_in'].mean()
        print(f"\nCategory: {category}")
        print(f"Number of players scraped: {len(df_clean)}")
        print(f"Average height (inches): {avg_height:.2f}")
        # Save CSV
        csv_filename = f"{category}_players_heights.csv"
        df_clean.to_csv(csv_filename, index=False)
        print(f"Saved data to {csv_filename}\n")

if __name__ == "__main__":
    main()
