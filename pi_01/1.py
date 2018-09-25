import requests

url = input("Digite a url: ")

response = requests.get(url)
print(response.status_code)
print(response.headers['content-type'])
print(len(response.text))