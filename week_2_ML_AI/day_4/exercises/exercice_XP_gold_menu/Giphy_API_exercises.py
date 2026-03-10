import requests
from pprint import pprint

query = 'hilarious'
rating = 'g'
api_key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'

url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={api_key}&limit=10"

response = requests.get(url)
status = response.status_code
data = response.json()
pprint(data)

filtered = []

for gif in data["data"]:
    height = int(gif["images"]["original"]["height"])
    if height >= 200:
        filtered.append(gif)


data 

