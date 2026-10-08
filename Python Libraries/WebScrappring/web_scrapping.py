# using  requests

import requests
a = requests.get('https://books.toscrape.com')
with open(f"./page1.html","w") as file:
    file.write(a.text)


from bs4 import BeautifulSoup
with open("./page1.html","r") as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser')

h3s = (soup.find_all("h3"))

for h3 in h3s:
    print(h3.find("a")['title'])



