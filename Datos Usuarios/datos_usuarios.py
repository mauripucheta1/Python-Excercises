# 1) Enumeración (enum): Nos sirve para definir un conjunto de valores constantes que tienen nombres asociados. Ejemplo:

from enum import Enum

class mesesAño(Enum):
    Enero = 1
    Febrero = 2
    Marzo = 3
    Abril = 4
    Mayo = 5
    Junio = 6
    Julio = 7
    Agosto = 8
    Septiembre = 9
    Octubre = 10
    Noviembre = 11
    Diciembre = 12

# Uso de la enumeración: Asignamos la numeración a una variable
mes = mesesAño.Septiembre
print(mes) # Obtendremos "mesesAño.Enero", ya que lo asignamos anteriormente en la variable
print(mes.name) # Obtendremos el nombre de esa numeración, en este caso Septiembre
print(mes.value) # Obtendremos el valor de esa numeración, en este caso 9


# 2) Clases (class): Representan un objeto definido por el usuario (Conceptos de Programación Orientada a Objetos (POO)):

class Perro:

    # Método para inicializar sus atributos
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    # Método para mostrar información
    def saltar(self):
        print(f"¡Hola! Me llamo {self.nombre} y mi raza es {self.raza}.")


# Ahora, una vez creada la clase, definimos instancias (Objetos) de la clase creada:
perro_uno = Perro("Bruno", "Pitbull") # Creamos un objeto, incorporando sus dos atributos (Nombre y raza en este caso) y le asignamos un valor a cada uno
perro_dos = Perro("Frida", "Galgo") # Creamos otro objeto, incorporando sus dos atributos (Nombre y raza igualmente) y le asignamos un valor a cada uno

# Básicamente lo que hicimos para que lo entiendan, fue crear una "clase global" para luego crear objetos (instancias de esa clase) para que puedan heredar sus atributos y hacer uso de ellos