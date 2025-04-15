# Resolución Ejercicio Nº 1:
# Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinar el número. El programa debe brindar pistas (ej. el número secreto es mayor) y debe continuar pidiendo 
# al usuario que adivine hasta que acierte. Al finalizar, debe mostrar el número de intentos.

import random
numero_secreto = random.randint(1, 10)
print("Bienvenido al juego. Intentarás adivinar el número secreto a través de pistas. ¡Buena suerte!")
numero_ingresado = input("Ingresa un número\n")
intentos = 0

while (True):

    intentos = intentos + 1

    if not (numero_ingresado.strip()):
        numero_ingresado = input("Error, valor vacío... Ingrese un número nuevamente:\n")
    else:
        verificar_numero_ingresado = int(numero_ingresado)
        if (verificar_numero_ingresado < numero_secreto):
            print("¡Nop! El numero secreto es más grande...")
            numero_ingresado = input()
        if (verificar_numero_ingresado > numero_secreto):
            print("¡Nop! El numero secreto es más chico...")
            numero_ingresado = input()
        if (verificar_numero_ingresado == numero_secreto):
            print(f"¡Felicitaciones! Ganaste... El numero secreto era: {numero_secreto}.")
            print(f"Acertaste con un total de {intentos} intentos.")
            break