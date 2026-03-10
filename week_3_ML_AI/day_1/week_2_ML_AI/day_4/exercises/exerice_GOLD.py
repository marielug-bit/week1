import requests

API_KEY = "3mD1rwNxJ3vPgcfxbTouSJwz5lqJmWXS"
url = "https://api.giphy.com/v1/gifs/random"

params = {
    "api_key": API_KEY,
    "tag": "cat"
}

response = requests.get(url, params=params) #request gere le lien avec internet, request a besoin de savoir
#qui je suis avec la cle et ce que je veux avec cat

data = response.json()

gif_url = data["data"]["images"]["original"]["url"]

print("Here is your GIF:")
print(gif_url)
