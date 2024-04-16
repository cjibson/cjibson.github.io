import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://keeptradecut.com/dynasty-rankings'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Get the title of the page
    title = soup.title.string
    print('Title:', title)

    # Example: Get all the <p> tags from the page
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print('Paragraph:', p.text)
else:
    print('Failed to retrieve the webpage')