#
#

#1.
from bs4 import BeautifulSoup
#2.
import requests


url ='https://es.wikipedia.org/wiki/Web_scraping'
headers={
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}

#3. 
respuesta = requests.get(url)

if respuesta.status_code == 200:
    print('la peticion se realizo correctamente')

    sopa = BeautifulSoup(respuesta.text, 'html.parser')

    #Extraer todos lost titulos h1

    titulos = [ titulo.string for titulo in sopa.find_all('h1')]
    if titulos:
        print(titulos)
    
    #Extraer todos los enlaces
    enlaces = [enlace.get('href') for enlace in sopa.find_all('a')]
    print(enlaces)