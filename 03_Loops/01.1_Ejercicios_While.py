

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

print("\nEjercicio 1:")

# contador = 10
# while contador >= 1:
#     print(contador)
#     contador = contador -1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")


contador2 = 0
suma = 0
while contador2 <= 20:
    contador2 = contador2 +1
    if contador2 % 2 == 0:
         suma = contador2 +suma         
print(suma) 

 

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input('Escribe un numero positivo: '))

contador = 1
factorial = 1

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1
print(factorial)     


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")


password = ''
while len(password)  < 8:
    password = input('Escribre un tu password , debe contener minio 8 caracteres: ')

    if len(password) < 8:
        print('La contraseña debe contener mas de 8 caracteres')
print(f'la contraseña es valida: {password}')        
 




# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")


numeroTabla = int(input('Escriba un numero: '))
contador = 1
res = 1

while  contador <= 10:
    res = numeroTabla * contador
    print(f'{numeroTabla} * {contador} =  {res}')
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")



numeroPrimo = int(input('Digite un numero: '))
contador = 0

while contador <= numeroPrimo:
    print(contador)
