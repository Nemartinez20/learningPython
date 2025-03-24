

## Instalar dependecia en la terminal
# pip3 insatll bs4

from bs4 import BeautifulSoup
# IMportar request de python 
import requests


url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/13-pulgadas'

response = requests.get(url)
# print(response.status_code)

if response.status_code == 200:
    print('Se encontro la informacion de al web')
    
    html = response.text

    sopa =  BeautifulSoup(html, 'html.parser')

   # print(sopa.prettify())

    #Recuperar el titulo
    title_soup = sopa.title
    if title_soup:
        print(title_soup)
        print(title_soup.string)
        #Buscando todos los metas
        metas = sopa.title.parent.find_all('meta')
        print(metas)

    #
    price_span = sopa.find('span', class_='rc-prices-fullprice')

    if price_span:
        print(f'El precio es: {price_span.string}')

    # Buscarndo todos loprecios
    price_spanAll = sopa.find_all('span', class_='rc-prices-fullprice')
    for price in price_spanAll:
        print(f'el precio del proucto es: {price}')


    productos = sopa.find_all(class_='rc-productselection-item')

    for product in productos:
        name = product.find(class_='list-title')
        print(name)
        print('=====================')
        nombre =  product.find(class_='list-title').text
        precio =  product.find(class_='rc-prices-fullprice').text

        print(f'El producto : {nombre} y su precio es:{precio}')
        print('********************************')
