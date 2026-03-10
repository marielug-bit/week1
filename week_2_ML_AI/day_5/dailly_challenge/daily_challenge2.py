import requests
import time

def get_load_time(url):
    start = time.time()          # début du chronomètre
    response = requests.get(url) # requête vers le site
    end = time.time()            # fin du chronomètre
    
    load_time = end - start
    return load_time