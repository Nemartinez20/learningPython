###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###


# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional



#ejemplo de  una funcion para imprimir algo en consola
def saludar_gente():
    print('hola  como estas')


saludar_gente()


# funcion con paramentros
def saludar_a(nombre):
    print(f'hola {nombre}')


saludar_a('Nestor Arley')
saludar_a('Mhilan')
saludar_a('Sara Valentina')

# funciones con mas paramentros

print('mas argumentos \n')

def sumar(a,b):
    suma = a + b
    return suma

print(sumar(8,7))

# Documentar las funciones con docstring
def restar(a,b):
    """Resta dos numeros y devuelve el resultado"""
    resta= a-b
    return resta

print(restar(10,5))

#Argumentos por defecto

def multiplicar(a, b = 10):
    mlt = a * b 
    return mlt

print(multiplicar(5))

##Argumentos por posicion

def descibir_person(nombre, edad, sexo):
    print(f'hola soy {nombre} tengo {edad} años y me identifico como {sexo}')


# funcion  con paramentros por posicion. 
descibir_person('juan',39,'Masculino')

## Argumentos pos valor o clave
descibir_person( edad = 25, sexo='femenino', nombre='Maria')


# Argumentos de longitud variable  (*args)

def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma = suma + numero
    return suma 

print(sumar_numeros(1,5,2,4,7))
print(sumar_numeros(1,5,2,4,7,8,7,9,5,4,6,2,5))

# Argumentos de clave-valor variable (**kwargs):

def saludando_aX(**kwargs):
    for  clave , valor in kwargs.items():
        print(f'{clave} : {valor}')

saludando_aX(nombre='juan',edad=30, sexo='Masculino')