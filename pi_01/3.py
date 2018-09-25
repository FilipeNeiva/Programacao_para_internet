import requests
import re

arq = open("links.txt", 'w')

#url = input("url : ")
url = "http://www.facebook.com"
response = requests.get(url)

link_re = re.findall(r"<a \w+ href[=\"http://www.\w*./?-]+[\ ]+[\w*=> ]+</a>", response.text)

links = ""

for link in link_re:
    links += link

print(links)

arq.write(links)
arq.close()


