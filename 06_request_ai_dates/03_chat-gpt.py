import requests

def onen(prompt):
    OPENAI_API_KEY = 'unosoasdas'
    url = 'https://api.openai.com/v1/chat/completions'
    headers ={
        "Content-Type": "application/json",
        "Authorization": f"Bearer ${OPENAI_API_KEY}" 
    }

    datos = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    respuesta = requests.post(url,json=datos, headers=headers)
    print(f'esta es:{respuesta}')


onen('escribe un cuento de niños de dos parrafos')

