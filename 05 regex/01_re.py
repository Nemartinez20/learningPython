
# Expresiones regulares

#
""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. Importar el módulo de expresiones regulares "re"
import re

#2.crear un patron que es una cadena de texto que describe lo que qeuremos buscar
patron = 'Hola'

# 3. El texto en donde  queremos buscar
texto = 'Hola mundo'

# 4. Usar la funcion de busqueda 're'
resultado = re.search(patron, texto) ## Usando el metodo search(palabraABuscar, TextoDondeSeVaaBuscar)
print(resultado)

if(resultado):
    print('He encontradoe l patron en el texto')
else:
    print('No se ha encontrado el patron en el terxto')


## ================= Metodos =====================


# group() Devuelve la cadena   que coincide con el texto
print(resultado.group())  #Hola

# start() devuelve la posicion inicial de la coincidencia
print(resultado.start()) # 0

# end() devuelve la posicino final de la coincidencia
print(resultado.end()) # 4


#                   EJERCICIO 01 
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.


patronEj1 = 'IA'
textoEj1 = 'la IA es buena pero no es bueno confiarse de la IA'

retultEJ1 = re.search(patronEj1, textoEj1)

print(retultEJ1)

## ================= Metodo findall =====================

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

textoEj2 = "Me gusta Pyhhon. Py/hon es lo máximo. Aunque Python no es tan difícil, ojo con Python"
patronEj2 = 'Py.hon' # el punto equivale a cualquier caracter

resultadoEj2 = re.findall(patronEj2, textoEj2)

print(resultadoEj2)
print('Solo coincidencias', len(resultadoEj2))


## ================= Metodo finditer =====================


# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

textEj3 = "Me gusta *ython. Python es lo máximo. Aunque /ython no es tan difícil, ojo con Python"
patronEj3 = '.ython'

resultadoEj3  = re.finditer(patronEj3, textEj3)

for result3 in resultadoEj3:
    print(result3.group(), result3.start() , result3.end())


#                     EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
textEj4 = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
patronEj4 = 'midu'

resultadoEj4 = re.finditer(patronEj4, textEj4)

print(resultadoEj4)

for resulU4 in resultadoEj4:
    print(resulU4.group(), resulU4.start() , resulU4.end())



###    ================== Modificadores ===================

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text0Ej5 = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
patronEj5 = "IA"

resultadoEj5 = re.findall(patronEj5, text0Ej5, re.IGNORECASE)

if resultadoEj5 : print(resultadoEj5)



# EJERCICIO 06
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
textoEj6 = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
patronEj6 = 'PYthon'

resultadoEj6 = re.findall(patronEj6, textoEj6, re.IGNORECASE)

if resultadoEj6 : 
    print(resultadoEj6)




###                   Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

textoEj7 = 'Hola, como estan Hola a todos'
patronEj7 = 'Hola'
remplazoEj7 = 'Adios'

textoNuevoEj7 = re.sub(patronEj7, remplazoEj7, textoEj7)
print(textoNuevoEj7)

## con mas paramentros al re

#textoNuevo = re.sub(textoAbuscar, textoPorElCulSeRemplaza, texto, ccontador , flags=re.IGNORECASE)
#contador = 0  === si el contador es cero se remplazan todas
# contador en 1 se remplazan solo la primero y si es 2 se remplazan las dos primeras y asi susesivamente
textoNuevo = re.sub(patronEj7, remplazoEj7, textoEj7, count= 1, flags=re.IGNORECASE)
print(textoNuevo)