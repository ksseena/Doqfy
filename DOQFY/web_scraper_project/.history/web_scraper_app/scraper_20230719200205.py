import requests
from bs4 import BeautifulSoup
import redis
import threading
import time
from .models import Nifty50Data

def scrape_nifty_50():
    url = "https://www.nseindia.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    nifty_50_table = soup.find('table', {'id': 'topGainers'})

    if nifty_50_table:
        rows = nifty_50_table.find_all('tr')
        data = []

        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 3:
                company = columns[0].text.strip()
                last_price = columns[1].text.strip()
                change = columns[2].text.strip()

                data.append({
                    'company': company,
                    'last_price': last_price,
                    'change': change
                })

                # Save data to the database
                Nifty50Data.objects.create(company=company, last_price=last_price, change=change)

        threading.Timer(300, scrape_nifty_50).start()

# Start the scraper thread
scrape_nifty_50()
