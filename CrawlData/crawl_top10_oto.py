from bs4 import BeautifulSoup

soup = BeautifulSoup (open("/home/ductn/Downloads/top10_oto.html", encoding="utf8"))


links = soup.find_all('h2')

for link in links:
    print(link.text)