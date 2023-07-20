# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import Nifty50Data

# def display_data(request):
#     data = Nifty50Data.objects.all()
#     return render(request, 'index.html', {'data': data})


# web_scraper_app/views.py
# web_scraper_app/views.py
# web_scraper_app/views.py
import requests
from django.shortcuts import render
from django.views.decorators.http import require_GET
from bs4 import BeautifulSoup
import redis
import threading
import time

# Function to extract 'Nifty 50' table data and store it in Redis
def scrape_and_store_data():
    redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

    while True:
        url = 'https://www.nseindia.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            nifty_table = soup.find('table', {'id': 'id_tableNifty'})

            if nifty_table:
                nifty_data = []
                rows = nifty_table.find_all('tr')[1:]  # Skip the header row
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) >= 3:
                        name = columns[0].text.strip()
                        value = columns[1].text.strip()
                        change = columns[2].text.strip()
                        data_item = {
                            'name': name,
                            'value': value,
                            'change': change,
                        }
                        nifty_data.append(data_item)

                # Store the 'Nifty 50' data in Redis
                redis_instance.set('nifty_data', str(nifty_data))

        time.sleep(300)  # Wait for 5 minutes before fetching data again

# Start the scraper thread when the server starts
thread = threading.Thread(target=scrape_and_store_data)
thread.daemon = True
thread.start()

# View to render the data from Redis to the template
@require_GET
def display_data(request):
    redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)
    # Retrieve data from Redis and pass it to the template
    nifty_data_str = redis_instance.get('nifty_data')

    if nifty_data_str:
        # Convert the data from a string representation to a list of dictionaries
        nifty_data = eval(nifty_data_str.decode('utf-8'))
    else:
        nifty_data = []  # Handle the case where 'nifty_data' is empty

    context = {'nifty_data': nifty_data}
    return render(request, 'card_layout.html', context)