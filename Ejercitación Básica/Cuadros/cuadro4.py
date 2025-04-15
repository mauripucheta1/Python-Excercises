# Resolución Ejercicio Nº 1:
# Escribe un programa que sume todos los números de una lista y luego responde ¿Qué tipo de variable utilizamos para resolver?
calificaciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La suma de todas nuestras calificaciones obtenidas, da como resultado: {sum(calificaciones)}")

# Resolución Ejercicio Nº 2:
# Escribe un programa que imprima el cuadrado de los números del 1 al 10.
for i in range(11):
    print(f"El cuadrado del número {i}, es igual a:", i ** 2)

# Resolución Ejercicio Nº 3:
# Escribe un programa que cuente los caracteres de una cadena de texto proporcionada por el usuario utilizando el for.
texto = input("Ingrese un texto cualquiera:\n")

while (True):

    if not (texto.strip()):
        texto = input("Ingresaste un valor vacío, prueba nuevamente:\n")
    else:
        a = 0
        for caracter in texto:
            a = a + 1
        print(f"La cantidad de carácteres es de: {a}")
        break

# Resolución Ejercicio Nº 4:
# Escribe un programa que cuente el número de vocales en una cadena de texto proporcionada por el usuario.
texto_dos = input("Ingrese otro texto cualquiera\n")

while (True):

    if not (texto_dos.strip()):
        texto_dos = input("Ingresaste un texto vacío, por favor, pruebe nuevamente:\n")
    else:
        texto_dos = texto_dos.lower()
        vocal = 0
        for letra in texto_dos:
            if letra in "aeiout":
                vocal = vocal + 1
        break

if (vocal > 0):
    print(f"La cantidad de vocales en tu texto fue de: {vocal}")
else:
    print("Lo siento... Tu texto no contiene vocales")

