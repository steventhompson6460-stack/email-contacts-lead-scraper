thonpython
import requests
from bs4 import BeautifulSoup

def fetch_and_clean_html(url: str):
 response = requests.get(url, timeout=10)
 response.raise_for_status()

 soup = BeautifulSoup(response.text, "html.parser")
 return soup.get_text(separator=" ", strip=True)