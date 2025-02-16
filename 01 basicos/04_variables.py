
## Variables para guardar datos en memoria

# decalracion de variables
nombre = 'Nestor Arley'
print(nombre)

## Python es tipado dinamico , porque las variables pueden 
## cambiar el tipo de dato en tiempo de ejecucion 
## no hay que declarar el tipo de dato explicitamente

edad = 32
print(type(edad))  # int

edad = 'nombre'
print(type(edad)) # str


##Python es typado fuerte  - no realiza conversiones de tipo automaticamente
print(10 + '10')  # TypeError: unsupported operand type(s) for Add: 'int' and 'str' on line 20

#imprimir cadena de texto formateo
print(f'hola {nombre} , tengo {edad} anos') 

#Convension de nombre de variables

mi_variable = 1 # snake_case
miVariable = 5 # camelCase
MiNombreDeVariable = 4 # upperCase
minombredevar = 3 # lowerCase

