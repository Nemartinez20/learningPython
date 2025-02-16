

## 02 bluce FOR
#Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista

# ITERAR EN UNA LISTA

#Lista
frutas = ['manzana', 'pera', 'uva', 'mandarina']

for fruta in frutas:
    print(fruta)


# Iterar sobre cualquier cosa que  sea iterable 
cadena = 'nestor'

for cad in cadena:
    print(cad)

# enumerate()

for index, fruta in enumerate(frutas):
    print(f'el indice es {index} y la fruta es {fruta}')


# bucles anidados

letras = ['a', 'b', 'c', 'd']
numeros = [1,2,3,4]

for letra in letras:
    for numero in numeros:
        print(f'{letra} x {numero} = {letra} * {numero}')


# break - para la ejecucion del bucle cuando se cumple la condicion

animales =['loro', 'pez', 'gato','pajaro','vaca', 'tigre']

for index,animal in enumerate(animales):
    print(f'el indece es {index} - y el animal es {animal}')
    
    if animal == 'gato':
        print(f'el gato esta en el indice {index}')
        break


# continnue 

for animal in animales:
    if(animal == 'gato'):
        continue
    print(animal)


# comprension de listas

print('compresion de litas')

animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

#Muestra los numeros pares

pares = [num for num in [1,2,3,4,5,6,6,7] if num % 2 == 0]
print(pares)
