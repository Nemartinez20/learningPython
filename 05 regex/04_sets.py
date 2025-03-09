
# [:] Coincide con cualquier caracter dentro de los corchetes

import re


usuario = 'rubio$.456+*'
patron= r'^[\w._+$*]+$'

rta= re.search(patron, usuario)

if rta: print(f'el usuario es valido {rta.group()}')
else:print('el usuario no es valido')
print(rta)


# buscar todas las vocales de una palabra

texto2 = 'Hoola mundo como estamn'
patron2 =r'[aeiou]'

rta2 = re.findall(patron2,texto2)
print(rta2)


# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
texto4 = "man ran fan ñan ban bynaan"
patron4 = r"[mfb]an"

rta4 = re.findall(patron4, texto4)
print(rta4)


texto3 = 'Mia anaMaria Mariana luzMaria aia'
patron3 = r'[Ma]ia'

rta3 = re.findall(patron3, texto3)
print(rta3)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
texto5 = "omniman fanatico man bandana"
# \b 


patron5= r'\b[om]an\b'

rta5= re.findall(patron5, texto5)
print(rta5)

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)