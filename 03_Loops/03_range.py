
###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print('\n range')

## range(Inicio, Hasta)
numeros = range(10)
print(type(numeros))
print(numeros)

## recorrer el range // a generado una secuencia de el 0 al 9

for num in numeros:
    print(num)


print('Con paso')
## con paso // que imprima cada cierto numero de  ?
# range(Inicio, Fin, Paso)

for num in range(0, 10 ,2):
    print(num)


print('Numeros negativos')

for numl in range(-5 , 0):
    print(numl)

for numl in range(10 , 0, -1):
    print(numl)
   

#Pasar rango a lista

nume = range(10)

range_Lista = list(nume)
print(range_Lista)

# Hacer  5 veces algo
for _ in range(5):
    print('hola haeiendo cinco veces algo')