# 1) Bucle For: Ejecuta un bloque de código un número específico de veces

jugadores_seleccion = ["Dibu Martinez", "Lionel Messi", "Lautaro Martinez"] # Definimos una lista con nombres de jugadores

for jugador in jugadores_seleccion: # Recorremos esa lista
    print(f"Nombre jugador: {jugador}") # Mostramos por pantalla el jugador (elemento) en cada vuelta que da dentro de la lista

# Bucle for con la función range(), ejemplo uno:
for i in range (0, 11, 2): # Decimos que i (iterador) arranque desde 0, termine en 10 (uno antes de 11) con paso 2 en 2
    print(i) # En este caso, mostrará por pantalla los numeros pares

# Bucle for con la función range(), ejemplo dos:
for i in range (0, 31, 3): # Decimos que i (iterador) arranque desde 0, termine en 30 (uno antes de 31) con paso 3 en 3
    print(f"{i}") # En este caso, mostrará por pantalla la tabla del 3

# Bucle for con la función enumerate(), ejemplo uno:
figuras = ["Cuadrado", "Triangulo", "Circulo"] # Defino una lista

for indice, figura in enumerate(figuras):
    print(f"El indice {indice} corresponde a la figura: {figura}") # Recorro la lista, donde obtengo tanto el indice como el elemento (figura)

# Bucle for con la función enumerate(), ejemplo uno:
deportes = ["Fútbol", "Handball", "Hockey"] # Defino una lista

for indice, deporte in enumerate(deportes): 
    print(f"El deporte {deporte} tiene {indice} participantes...") # Recorro la lista, donde obtengo tanto el indice como el elemento (deporte)

# Bucle for con la función zip(), ejemplo uno:
destrezas = ["Cantar", "Bailar", "Correr"] # Defino una primer lista
alumnos = ["Joaquin", "Mauricio", "Juan"] # Defino una segunda lista

for alumno, destreza in zip(alumnos, destrezas):
    print(f"He logrado identificar que el alumno {alumno} tiene destreza para {destreza}.") # Recorro ambas listas y las "concateno", tomando el primer elemento de cada una, luego el segundo y así


# Declaración for en diccionarios (dict): Podemos iterar para recuperar los pares "Clave - Valor"
# Defino un diccionarios
libros = {
    1: "El principito",
    2: "Caperucita Roja",
    3: "Detectives en Córdoba"
}

# Ejemplo solo con claves:
print("Dentro de tu diccionario, tienes las siguientes pares de Clave - Valor :")
for clave in libros.items():
    print(f"Libro: {clave}")