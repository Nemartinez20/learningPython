# Introsuccion a classe en python

#Las clases son plantillas para crear objetos , un objeto es un 
#instancia de una clase
#Nos permite agrupar datos (atributos o propiedades ) y funciones(metodos) en un solo lugar

#1. Ejemplo
class coche:
    # atributo de calse ( se comparte en todas las instancias)
    tipo= 'es un vehiculo de cuatro ruedas'

    #Metodo especial qie es el qie construye el objeto
    # al llamar a la clase con new
    #  se llama automaticamente ese metodo cuando creas la instancia

    #Este seria como el constructor
    def __init__(self, marca , modelo, color): # el self se refiere a la  clase misma
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def arrancar(self):
        print(f'El coche {self.marca} , {self.modelo} arranco en beunas condiciones')


# llamanos la clase
mi_coche = coche('Toyota', 'Corolla', 'Rojo')
mi_coche.arrancar()

# Nuevamente instanciams la clase
coche_namm = coche('Toyota', 'Fortuner', 'Plateada')
coche_namm.arrancar()
