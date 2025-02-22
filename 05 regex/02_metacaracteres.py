###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

# 1. El punto (.)
#Concidir en culquier caracter excepto en una nueva linea

import re

texto = 'Hola mundo, H0la otra vez, H$la de nuevo'
patron = 'H.la'

resultado = re.findall(patron, texto)

if resultado:
    print(resultado)
else:
    print('Nose ha encontrado el patron')


# Ejemplo 2
texto2 = 'casa cusa cassa cesa coso cuausa cusa cisa cesa'
patron2 = 'c.sa'

resultado2 = re.findall(patron2, texto2)
print(resultado2)



# 1. El punto (.)
# BUscar el punto en la cadena de textio, anular el comportamiento por default del punto ---  se debe colocar un backslach antes del punto
## OJO  PARA EXPRESIONES EL PATRON COO ES UN STRING AHORITA SE DEBE ANTECEDER UNA R


# Cómo usar la barra invertida para anular el significado especial de un símbolo
texto3 = 'Hola mi casa es blanca. y mi coche es negro.'
patron3 = r'\.'

resultado3 = re.findall(patron3, texto3)
print(resultado3)


# Buscar un digito 
# # \d: coincide con cualquier dígito (0-9)

texto4 = 'EL numero de telefono de Superman es 1234556789'
## hay \d 3 veces busca tres numeros de grupos de 3
patron4 = r'\d\d\d' ## busca primero numero  si se le coloca mas de \d cuantas veces se le ponga busca la misca cantida de numeros


resultado4 = re.findall(patron4,texto4)
print(resultado4)


# Buscar un rango

patron5 = r'\d{9}'
resultado4 = re.findall(patron5,texto4)
print(resultado4)


# detectar si un numero de telefono de colombia en el texto -- prefijo +57

texto6 = 'Mi numeor de telefono es el +57 3202087589 apuntalo here'
patron6 = r"\+57 \d{10}"

resultado6 = re.search(patron6, texto6)
if  resultado6 : print(resultado6.group())

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _) no simbolos especiales

texto7 = 'Hola_Mundo_ciomo_09'
patron7 = r'\w'
resultado7 = re.findall(patron7, texto7)
print(resultado7)

# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)

texto8 = 'Hola Mundo \n ciomo_09\t'
patron8 = r'\s'
resultado8 = re.findall(patron8, texto8)
print(resultado8)

# ^: Coincide con el principio de una cadena 

usename = '\789_name'
patron9 = r'^\w'  # si la cadena empiza con un simolo alfanumerico

valido =  re.search(patron9, usename)

print(valido)
if valido: print('El usuario es valido')
else: print('el usuario no es valido')


#EJERCICIOS NUMERO

texto10 = '+5788 3124596932'
patron10 = r'^\+\d{2} ' ## tiene que ncontrar el signo + y dos numeros antes de el espacio iniciando la cadena de texto

phone =  re.search(patron10, texto10)

print(phone)

# $: Coincide con el final de una cadena

texto11 = 'hola señor martinez'
patron11 = r'Martinez$'

resultado11 = re.search(patron11, texto11, re.IGNORECASE)
print(resultado11)


#========================================================== EJERCICIOS ==========================================================
# EJERCICIO
# Valida que un correo sea de gmail

correo = 'nestor12ma@gmail.com'
patron12 = r'^\w+@gmail.com$' ## con el cuantificador del  + seria una o mas veces que tenga caracteres alfanumericos

resultado12 = re.search(patron12, correo)
print(resultado12)

if resultado12: print('Es un correo valido')
else: print('CorreoInvalido')

text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)
print(valid)

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"

patron13 = r'\w+\.txt'

resultado13 = re.findall(patron13,files)
print(resultado13)
# for uno in resultado13:
#     print(uno)



# \b Coincide con el principio y final de una palabra

texto14 ='casa coche perro casada  casado casa'
patron14= r'\bcasa\b'

resultado14 = re.findall(patron14, texto14)
print(resultado14)

# |: Coincidir con una opcion u otra
    
frutas = 'banano manzana pera lulo palta lecherita'
patron15 = r'banano|pera|p...a|\w{9}'    

resultado15 = re.findall(patron15, frutas)
print(resultado15)