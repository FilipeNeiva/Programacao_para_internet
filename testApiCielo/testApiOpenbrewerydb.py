import requests


url = 'https://api.openbrewerydb.org/breweries/'

response = requests.get(url)

print(response.json())

