import requests

from bs4 import BeautifulSoup
import pandas as pd

def scrape_ktc_risers():
    # URL of the website you want to scrape
    url = 'https://keeptradecut.com/dynasty-rankings'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the top 5 risers section
        top_risers_section = soup.find('div', class_='riser insightWrapper')

        # Initialize lists to store data
        rising_players = []
        rising_values = []

        if top_risers_section:
            # Find all top 5 players within the section
            top_risers = top_risers_section.find_all('div', class_='topFivePlayer')
            
            for player in top_risers:
                # Extract player name
                player_name = player.find('div', class_='topFiveName').find('p').text
                
                # Extract number below value
                value_number = player.find('div', class_='topFiveValue').find('p').text

                # Append data to lists
                rising_players.append(player_name)
                rising_values.append(value_number)

            # Create DataFrame
            df = pd.DataFrame({'Player': rising_players, 'KTC Value': rising_values})
            return df
        
        else:
            print("Top risers section not found.")
            return None

def scrape_ktc_fallers():
    # URL of the website you want to scrape
    url = 'https://keeptradecut.com/dynasty-rankings'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the top 5 risers section
        top_fallers_section = soup.find('div', class_='faller insightWrapper')

        # Initialize lists to store data
        falling_players = []
        falling_values = []

        if top_fallers_section:
            # Find all top 5 players within the section
            top_fallers = top_fallers_section.find_all('div', class_='topFivePlayer')
            
            for player in top_fallers:
                # Extract player name
                player_name = player.find('div', class_='topFiveName').find('p').text
                
                # Extract number below value
                value_number = player.find('div', class_='topFiveValue').find('p').text

                # Append data to lists
                falling_players.append(player_name)
                falling_values.append(value_number)

            # Create DataFrame
            df = pd.DataFrame({'Player': falling_players, 'KTC Value': falling_values})
            return df

        else:
            print("Top fallers section not found.")
            return None

# Call the functions and assign the returned DataFrames to variables
df1 = scrape_ktc_risers()
df2 = scrape_ktc_fallers()

# Save DataFrames to CSV files
if df1 is not None:
    df1.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\risers.csv', index=False)

if df2 is not None:
    df2.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\fallers.csv', index=False)