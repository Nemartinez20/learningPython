#CONSULTAR UNA API

#1.  *************** Sin dependencias -->Forma nativa  ************************
#2 Utilizando Json Placeholder

# Paso 1 importar |
import urllib.error
import urllib.request
# Paso 2 importar |
import json

# paso 3 definir la url de la Api
url_Json = 'https://jsonplaceholder.typicode.com/todos'

try:
    # Paso 4 Iniciar la peticion
    respuesta = urllib.request.urlopen(url_Json)
    data = respuesta.read()
    resultado = json.loads(data.decode('utf-8')) # decodificar los datos
    respuesta.close() # cerrar la peticion
    # print(resultado)
except urllib.error.URLError as e:
    print(f'Error en la solicitud: {e}')


#2.  *************** Con  dependencias --> requests  ************************

import requests
respuesta1 = requests.get(url_Json)
# print(respuesta1.json())



#3 Un POST

try:
    input={
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
    }

    respuesta2 = requests.post(url_Json, json=input)
    print(f'esta es la respuesta: {respuesta2}')
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud: {e}')

    #3 Un PUT

try:
    url_Json1 = 'https://jsonplaceholder.typicode.com/todos/1'
    input={
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
    }

    respuesta2 = requests.put(url_Json1, json=input)
    print(f'esta es la respuesta: {respuesta2}')
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud: {e}')