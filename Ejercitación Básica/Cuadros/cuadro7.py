# Resolución Ejercicio Nº 1:
# Crea una lista de números desordenados y ordénala en orden ascendente y descendente.
numeros = [6,3, 1, 4, 8, 10, 5, 2, 9, 7]
numeros_ascendente = sorted(numeros)
print(f"Los números ordenados de manera ascendente quedaría tal como:", numeros_ascendente)
numeros_descendente = sorted(numeros, reverse=True)
print(f"Los números ordenados de manera descendente quedaría tal como:", numeros_descendente)

# Resolución Ejercicio Nº 2:
# Crea una lista de números que cuente el número de veces que aparece el número ingresado por el usuario.
numeros_dos = [55, 23, 61, 18, 55, 9, 37, 55, 28, 28, 28, 9, 23]
print(f"Tienes la siguiente lista: {numeros_dos}.")
numero_usuario = input("Ingrese un número para ver cuántas veces se repite en la lista:\n")

while (True):
    
    if not (numero_usuario.strip()):
        numero_usuario = input("Valor vacío ingresado, pruebe nuevamente:\n")
    else:
        numero_usuario_entero = int(numero_usuario)
        a = 0
        for numero in numeros_dos:
            if (numero_usuario_entero == numero):
                a += 1
        print(f'La cantidad de veces que se repite "{numero_usuario}" es de {a} veces.')
        break

# Resolución Ejercicio Nº 3:
# Crea una tupla con tus tres colores favoritos e imprime sólo el segundo color.
colores = ("Blanco", "Negro", "Gris")
print(colores[1])

# Resolución Ejercicio Nº 4:
# Crea una tupla de números y verifica si el número ingresado por el usuario existe.
numeros_tres = (48, 24, 9, 57, 20)
numero_usuario_dos = input("Ingrese un número para verificar si existe o no en la túpla:\n")

while (True):

    if not (numero_usuario_dos.strip()):
        numero_usuario_dos = input("Valor ingresado vacío, por favor ingrese algo:\n")
    else:
        numero_usuario_dos_entero = int(numero_usuario_dos)
        for numero in numeros_tres:
            if (numero_usuario_dos_entero == numero):
                print(f"El valor {numero_usuario_dos_entero} existe en la túpla.")
                break
            else:
                print(f"El valor {numero_usuario_dos_entero} no existe en la túpla.")
                break
        break
