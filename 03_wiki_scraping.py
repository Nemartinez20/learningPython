#
#

#1.
from bs4 import BeautifulSoup
#2.
import requests
#4.Obtener enlaces absolutos
from  urllib.parse import urljoin

def scrape_url(url:str):

  
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
        enlaces = [urljoin(url, enlace.get('href')) for enlace in sopa.find_all('a')]
        #print(enlaces)

        #Recuperar todo el texto 
        all_text = sopa.get_text()
        #print(all_text)

        #recuperar el texto del maain
        main = sopa.find('main').get_text()
        #print(main)

        # de un div en especial - pasandole el id del div
        #div = sopa.find('div', {'id': 'mw-content-text'}).get_text()
        #print(div)

        # Extraer el open graph si existe
        og_image = sopa.find('meta',{'property':'og:image'})
        if og_image:
            print(og_image['content'])
        else:
            print('No se encontro la imagen')



# Llamar a la funcion
#url ='https://es.wikipedia.org/wiki/Web_scraping'
url ='https://midu.dev'
scrape_url(url)