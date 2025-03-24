

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
