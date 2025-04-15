# Importación de librerias necesarias para la resolución
import math

# Resolución Problema Nº 1:
# Escribe un programa que pida al usuario el radio de un círculo y calcule el área.
radio = float(input("Ingresa el radio de un círculo\n")) 
pi = 3.14159265359
area = (pi * (radio ** 2))
print(f"El area del círculo es {area}.")

# Resolución Problema Nº 2:
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.
grados_celcius = float(input("Ingresa la tempera en grados celcius\n"))
grados_fahrenheit = grados_celcius * 9 / 5 + 32
print(f"Los Grados Celcius {grados_celcius}º convertidos a Grados Fahrenheit equivale a: {grados_fahrenheit}º.")

# Resolución Problema Nº 3:
# Escribe un programa que pida al usuario los dos catetos de un triángulo rectángulo y calcule la hipotenusa.
cateto_uno = float(input("Ingrese la medida numérica del primer cateto expresado en centímetros:\n"))
cateto_dos = float(input("Ingrese la medida numérica del segundo cateto expresado en centímetros:\n"))
hipotenusa = float(math.sqrt((cateto_uno ** 2) + (cateto_dos ** 2)))
print(f"El valor de la hipotenusa es: {hipotenusa}.")

# Resolución Problema Nº 4:
# Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nombre y la edad calculada.
nombre_persona = input("Ingrese su nombre:\n")
año_de_nacimiento = int(input("Ingrese su año de nacimiento:\n"))
edad = 2025 - año_de_nacimiento
print(f"¡Hola {nombre_persona}! El año en el que naciste es {año_de_nacimiento}, por ende, tu edad en este año es de {edad} años.") 