
# pip3 install requests -Z instala las dependecias para hacer peticiones

import requests;
# importar para hacer las reges
import re

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/13-pulgadas'
#url = 'https://www.alkosto.com/marcas/apple/computadores-apple/imac/c/imac'
response = requests.get(url)
# print(response.status_code)
# print(response.text)

if response.status_code == 200:
    print('la perticion fue existosa')

    html = response.text
    #print(html)

    #regular expresion para encontrar el precio

    #quiero que me caputres el contenido de ese span
    precio_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'

    #(patron , dedonde)
    buscar = re.search(precio_pattern, html)

    if buscar:
        print(f"El precio del producto es: {buscar.group(1)}")