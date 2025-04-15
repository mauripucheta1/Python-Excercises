# Resolución Ejercicio Nº 1:
# Escribe una función que reciba como parámetros un nombre y devuelva un saludo personalizado.
def saludar(nombre):
    print(f"¡Hola {nombre}! ¿Cómo estás?")

saludar("Mauricio")

# Resolución Ejercicio Nº 2:
# Escribe una función que permita calcular el factorial de un número.
import math

def factorial(numero):
    print(f"El factorial de {numero} es:", math.factorial(numero))

factorial(5)

# Resolución Ejercicio Nº 3:
# Escribe una función que reciba una lista de números y devuelva el promedio.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def promedio(lista_numeros):
    promedio_lista = sum(lista_numeros) / len(lista_numeros)
    print(f'El promedio de la lista: "{lista_numeros}" es de: {promedio_lista}')

promedio(lista_numeros)

# Resolución Ejercicio Nº 4:
# Escribe una función que convierta un número entero a binario y otra que realice el cálculo inverso.
def convertir_a_binario (numero):
    binario= bin(numero)
    print(f"El resultado de convertir {numero} a binario es: {binario}")

def convertir_a_entero (binario):
    entero = int(binario, 2)
    print(f"El resultado de convertir {binario} a número entero es: {entero}")

convertir_a_binario(2)
convertir_a_entero("11")