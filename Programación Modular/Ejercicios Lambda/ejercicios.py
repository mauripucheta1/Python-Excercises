# Resolución Ejercicio Nº 1:
# Crea una función anónima (lambda) que calcule el promedio de un arreglo de números enteros.

arreglo = [20, 24, 24, 2004, 1977, 80, 23, 1, 54]
promedio = lambda arreglo: sum(arreglo) / len(arreglo)
print(f'El promedio del arreglo "{arreglo}" es "{promedio(arreglo)}"')

# Resolución Ejercicio Nº 2:
# Escribe una función anónima que calcule el factorial dado un número entero.

import math
numero = int(input("Ingresa un número para conocer su factorial:\n"))
factorial = lambda numero: math.factorial(numero)
print(f'El factorial del número "{numero}" es "{factorial(numero)}"')

# Resolución Ejercicio Nº 3:
# Crea una función anónima que permita conocer si un número es par.

numero_dos = int(input("Ingresa un número para saber si es par:\n"))
es_par = lambda numero_dos: numero_dos % 2 == 0
if es_par(numero_dos):
    print(f'El número "{numero_dos}" es par')
else:
    print(f'El número "{numero_dos}" es impar')

# Resolución Ejercicio Nº 4:
# Dado un arreglo de números enteros, crea una función anónima que retorne una lista con los números pares.

arreglo_dos = [51, 20, 33, 40, 55, 78, 80, 82, 2048]
es_par_arreglo = list(filter(lambda n: n % 2 == 0, arreglo_dos))
print(f'Los números pares del arreglo "{arreglo_dos}" son "{es_par_arreglo}"')

# Resolución Ejercicio Nº 5:
# Utiliza una función lambda para elevar al cuadrado cada elemento de una lista de números.
arreglo_tres = [2, 3, 4, 5, 6]
elevacion = list(map(lambda a: a ** 2, arreglo_tres))
print(f'Los números del arreglo "{arreglo_tres}" elevados al cuadrado cada uno, da como resultado: "{elevacion}"')