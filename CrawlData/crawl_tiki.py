from bs4 import BeautifulSoup


soup = BeautifulSoup (open("/home/ductn/Downloads/tiki.html", encoding="utf8"), "html5lib")

links = soup.find_all('div', class_='product-item')

for link in links:

    print('Tên hàng: ' + link['data-title'] + ' | Giá: ' + link['data-price'] + ' | ID: ' + link['product-sku'])

