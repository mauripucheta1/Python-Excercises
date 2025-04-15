# 1) Declaración de "Datos no Primitivos":
# Listas (list): Representan una colección ordenada y mutable. ¡Ojo! Averiguar por su cuenta qué operaciones podemos realizar con ellas, yo les dejo una sola...
frutas = ["Manzana", "Naranja", "Banana"] # Definimos una lista que contiene valores (string, en este caso)
print(frutas) # Mostrará por pantalla la lista (Todos los elementos)
print(frutas[0]) # Mostrará por pantalla el elemento en la posición 0 que contiene la lista (Manzana, en este caso)

# Operación posible:
frutas.append("Pera") # Agregamos al final de la lista un nuevo elemento, en este caso "Pera"
print(frutas) # Mostrará por pantalla la lista ya modificada, es decir, con ese elemento ya insertado

calificaciones = [4, 7, 10] # Definimos una lista que contiene valores (int, en este caso)
print(calificaciones) # Mostrará por pantalla la lista (Todos los elementos)
print(calificaciones[2]) # Mostrará por pantalla el elemento en la posición 2 que contiene la lista (10, en este caso)

# Tuplas (tuple): Representan una colección ordenada y no mutable
puntos = [60, 80, 95] # Definimos una tupla con estos tres elementos y no podrán sufrir modificaciones, ejemplo debajo:
# puntos[1] = 76 -> Estoy intentando asignar un nuevo valor (76) en la posición 1 de la tupla (80) para reemplazarlo, pero generará un error. ¡Son inmutables!

# Conjuntos (set): Son colecciones desordenadas que no permiten elementos duplicados, sumado a que los elementos no tienen indices. ¡Investiguen que operaciones podemos realizar, les dejo una sola!
marcas_vehiculos = {"Volkswagen", "Fiat", "Ford", "Chevrolet"} # Definimos un conjunto de string
print(marcas_vehiculos[3]) # Mostrará por pantalla el valor almacenado en la posición 3 (Chevrolet) dentro del conjunto 

# Operación posible:
marcas_vehiculos.add("Toyota") # Añade un elemento al conjunto
print(marcas_vehiculos) # Muestra por pantalla el conjunto actualizado

# Conjuntos inmutables (frozenset): Son como los conjuntos, pero inmutables. Cuando querramos generar una operación, generará error
dias =  frozenset (["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])

# Diccionarios (dict): Son colecciones de pares "clave - valor"
alumnos = {
    "Nombre": "Mauricio", # "Nombre" = clave y "Mauricio" = valor
    "Edad": 20,
}

print(alumnos["Nombre"]) # Mostrará por pantalla el valor del nombre, en nuestro caso: "Mauricio"
alumnos["Ciudad"] = "Córdoba" # Agregamos un nuevo par Clave ("Ciudad") - Valor ("Córdoba")