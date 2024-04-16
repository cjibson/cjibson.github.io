import requests

from bs4 import BeautifulSoup

def scrape_ktc():
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

        #Initialize lists to store data
        players = []
        values = []

        if top_risers_section:
            # Find all top 5 players within the section
            top_risers = top_risers_section.find_all('div', class_='topFivePlayer')
            
            for player in top_risers:
                # Extract player name
                player_name = player.find('div', class_='topFiveName').find('p').text
                
                # Extract number below value
                value_number = player.find('div', class_='topFiveValue').find('p').text
                
    else:
        print('Failed to retrieve the webpage')