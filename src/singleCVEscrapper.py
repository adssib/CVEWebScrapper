import requests
from bs4 import BeautifulSoup
import time

input_file = "tempCve.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

with open(input_file, "r") as f:
    urls = f.readlines() 

for url in urls:
    url = url.strip()  
    if not url:
        continue 

    print(f"Fetching: {url}")
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Successfully fetched: {url}")
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No title found"
            print(f"Page Title: {title}")
        else:
            print(f"Failed to fetch {url}, Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")

    time.sleep(1)