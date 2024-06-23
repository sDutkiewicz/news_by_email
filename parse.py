import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')
