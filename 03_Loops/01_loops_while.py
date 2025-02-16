

print('\n bucle while')


# bucle while

# contador = 0

# while contador < 5:
#     print(contador)
#     contador = contador + 1



# while contador <= 100:
#     contador = contador + 1
#     print(contador)
#     if contador % 5 == 0:
#         print('el numero es modulo de 5')
#         break

## bucle con continue
# print('\n bucle con continue')

# contador = 0

# while contador <10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(contador)


# contador = 0
# print('\n bucle  while con else')

# while contador <= 10:
#     print(contador)
#     contador = contador +1

# else:
#     print('eel bucle a terminado')


# perdir a usuario info dentro de un while
# quiero ser positivo si no no te dejo en paz

numero = -1

while numero <0:
    try:
     numero = int(input('Escribe un numero positivo:'))
     if numero < 0:
           print('El numero debe ser positivo')
    except:
       print('no escribiste un numero, tiene que ser un numero: ') 

print(f'Correcto --- el numero que haz introducido es {numero}')        
