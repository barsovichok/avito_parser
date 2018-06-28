import requests
from bs4 import BeautifulSoup

search = input('Напишите, что хотите найти на Авито: \n')
search_params = {'q': search}
page = requests.get("https://www.avito.ru/", params=search_params)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find_all(class_="item_table-header")

price_list = []

for item in title:
    socks_name = item.find(class_='title')
    socks_name = socks_name.get_text()
    socks_price = item.find(class_='price')
    socks_price = socks_price.get_text()
    socks_name = socks_name.strip()
    socks_price = int(socks_price.replace('₽', '').replace(' ', '').strip())
    price_list.append(dict(title=socks_name, price=socks_price))


print(price_list)
