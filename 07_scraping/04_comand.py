#1. importar
import requests
import argparse # para persir darto por consola

# 2.
from bs4  import BeautifulSoup # para escraper mas facil
from urllib.parse import  urljoin # para concatenar las url


# 3.
parser = argparse.ArgumentParser(description="web scrapping para revissar el SEO  con la url")
parser.add_argument('url', type=str ,help="tienes que colocar la url del sitio que vas a ckecar y scrape")

args = parser.parse_args()
url = args.url

# 4. Iniciar con la peticion
respuesta = requests.get(url)

if respuesta.status_code == 200:
    print('todo sallio ok')
