# 1) Listas: Lo desarrollamos con anterioridad, pero dejo nuevamente otro ejemplo:
telefonos = ["Samsung", "¡Apple", "Motorola"] # Esto es una lista

# Operaciones básicas:
# CREATE = Permite crear una lista 
ejemplo_create = ["Hola", "Chau"]
# GET = Permite obtener un elemento de mi lista
print(ejemplo_create[1])
# UPDATE = Permite actualizar un elemento de mi lista
ejemplo_create[1] = "Bienvenido"

# Operaciones mutables:
# append: Agrega un elemento al final de la lista
ejemplo_create.append("Hello")
# insert: Permite insertar un elemento en una posición específica
ejemplo_create.insert(1, "Hi")
# remove: Permite remover un elemento
ejemplo_create.remove(2)
# pop: Permite eliminar el último elemento de la lista
ejemplo_create.pop()
# sort: Permite ordenar la lista
ejemplo_create.sort()
# reverse: Permite invertir el orden de los elementos
ejemplo_create.reverse()
# extend: Permite agregar múltipler elementos a mi lista, por ejemplo
ejemplo_extend = ["Welcome", "Ciao"]
ejemplo_create.extend(ejemplo_extend)

# Operaciones inmutables:
# concatenar(+): Permite concatenar dos o más listas
lista_uno = [1, 2, 3]
lista_dos = [4, 5, 6]
lista_final = lista_uno + lista_dos
# replicar (*): Permite replicar una lista por X
lista_final = lista_uno * 2
# index: Permite encontrar el indice de un elemento
lista_uno.index(2)
# count: Permite contar la cantidad de ocurrencias de un elemento
lista_tres = [1, 2, 2, 2, 3, 4]
lista_tres.count(2)
# sum: Permite sumar elementos numéricos
print(sum(lista_tres))

# 2) Listas unidimensionales (vectores): Colección lineal de elementos a los cuales se accede por índice único
calificaciones = [2, 8, 3, 4, 10] # Definimos una lista
print(calificaciones[2]) # Mostramos por pantalla el elemento en la posición 2 dentro de la lista, en este caso, 3
print(calificaciones[0]) # Mostramos por pantalla el elemento en la posición 0 dentro de la lista, en este caso, 2

# 3) Listas bidimensionales (matríces): Es una lista de listas
lista_bidimensional = [ # Defino una lista con listas dentro
 
    [55, 33, 24], # Defino mi primer lista
    [13, 19, 78, 89], # Defino mi segunda lista
    [45, 1] # Defino mi tercer lista

]

print(lista_bidimensional[1][0]) # Muestro por pantalla la lista con el índice de fila 1 y el índice de columna 0. Obtendremos (13)
print(lista_bidimensional[2][1]) # Muestro por pantalla la lista con el índice de fila 2 y el índice de columna 1. Obtendremos (1)

# 4) Tuplas: Representan una colección ordenada e inmutable de elementos
tupla_uno = (1, 2, 3)

# ¡Ojo! Con nuestras tuplas nosotros podemos realizar las mismas operaciones anteriores, siempre y cuando no hagan referencia a una modificación... ¡Son inmutables!
# Podemos, desempaquetar una tupla
persona = ("Mauricio", 20, "Programador") # Defino una tupla
nombre, edad, profesion = persona # La descompongo en 3 variables
print(nombre) # Imprimirá "Mauricio"
print(edad) # Imprimirá 20 
print(profesion) # Imprimirá "Programador"