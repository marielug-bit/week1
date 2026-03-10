import requests
URL = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print(response)

status = response.status_code
print(status)