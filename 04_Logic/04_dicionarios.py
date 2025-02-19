## Dicionarios

persona ={
    'nombre': 'Nestor',
    'edad': 20,
    'estudiante': True,
    'calificaciones': [7,8,9],
    'socials':{
    'twitter': 'Nestor12',
    'Facebook': 'Nestormarti',
    'Instagram': 'Nestor1',

    }
}

# al acceder a las propiedades del diccionario
print(persona['nombre'])
print(persona['calificaciones'][1])
print(persona['socials']['twitter'])


# cambiar valores al acceder
persona['nombre'] = 'Arley'

#Eliminar una propiedad

del persona['edad']
# elimina pero devuelve el valor eliminado
est = persona.pop('estudiante')

print(persona)

## Sobreescribir un diccionario con otro
a ={'nombre':'jose', 'edad':30}
b ={'nombre':'Juan', 'edad':34 ,'casado':True}

a.update(b)
print(a)


## comprobar si existe una propiedad
print('name' in persona) # false
print('nombre' in persona) # true


# Obtener todas las claves
print(persona.keys())

#obtener todos los valores
print(persona.values())


# obtener tanto clave como valor
print(persona.items())

print('terando')

#iterar
for key , values in persona.items():
    print(f'las llaves : {key} - y el valor : {values}')