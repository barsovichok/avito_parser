import requests
from bs4 import BeautifulSoup

def params_input(search):
    search_params = {'q': search}
    return search_params

def get_requests(search_params):
    page = requests.get("https://www.avito.ru/", params=search_params)
    return page

def find_in_soup(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all(class_="item_table-header")
    return title

def parse_price(price):
    price = price.replace('₽', '').replace(' ', '').strip().lower()
    if price.isdigit():
        return int(price)
    elif price == 'бесплатно':
        return 0
    else:
        return -1

def find_price_list(title):
        socks_name = item.find(class_='title')
        socks_name = socks_name.get_text()
        socks_price = item.find(class_='price')
        socks_price = parse_price(socks_price.get_text())
        socks_name = socks_name.strip()
        price_list = dict(title=socks_name, price=socks_price)
        return price_list

search_params = params_input(input('Напишите, что хотите найти на Авито: \n'))
page = get_requests(search_params)
title = find_in_soup(page)
price_list = []
for item in title:
    find_price_list(title)
    price_list.append(find_price_list(title))
print(price_list)
