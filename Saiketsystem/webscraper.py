import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h3")

    print("\n--- News Headlines ---\n")
    for headline in headlines[:10]:
        print("-", headline.get_text())
else:
    print("Failed to retrieve the webpage.")
