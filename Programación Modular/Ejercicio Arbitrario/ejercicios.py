# Resolución Ejercicio Nº 1:
# Escribe una función que tome una cantidad variable de cadenas y las concatene en una sola cadena. Ej. “Hola Mundo”

def concatenar_cadenas(*args):
    return " ".join(args)

resultado = concatenar_cadenas("Hola", "Mundo")
print(resultado)

# Resolución Ejercicio Nº 2:
# Escribe una función que muestre la cantidad de argumentos con nombre enviados.

def cantidad_argumentos(**kwargs):

    return len(kwargs)

resultado_dos = cantidad_argumentos(piernas = 2, recibimiento = "Hola", ojos = 2, dedos = 20, despedida = "Chau")
print(resultado_dos)

# Resolución Ejercicio Nº 3:
# Escribe una función que calcule el promedio de una cantidad variable de números.
def promedio(*args):

    return sum(args) / len(args)

resultado_tres = promedio(11, 45, 754, 1234, 52)
print(resultado_tres)