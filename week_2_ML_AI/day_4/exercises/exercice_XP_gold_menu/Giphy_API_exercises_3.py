import requests
from pprint import pprint

term = input('enter a search term: ').strip()

API_key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'

query = term

url = f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={API_key}&limit=10"
response = requests.get(url)
status = response.status_code
data = response.json()
pprint(data)