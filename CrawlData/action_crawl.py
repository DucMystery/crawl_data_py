
import lxml
from bs4 import BeautifulSoup
soup = BeautifulSoup (open("/home/ductn/Downloads/vnexpress.html", encoding="utf8"))

article = soup.find('article', class_='fck_detail')

links = article.find_all('p', class_='Normal')

for link in links:

    print(link.text)
    print("\n")