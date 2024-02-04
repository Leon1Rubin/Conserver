# scrab mfg overview dashboard
from bs4 import BeautifulSoup
import requests

url = f"http://10.42.0.6/mfg/html/overview.html"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

