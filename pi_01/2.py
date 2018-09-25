import requests

url = input("Link da imagem: ")
response = requests.get(url)

img = open("imagem.jpg", "wb")
img.write(response.content)

img.close()