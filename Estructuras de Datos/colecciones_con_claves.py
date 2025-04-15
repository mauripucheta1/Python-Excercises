# 1) Diccionarios: Lo vimos con anterioridad, pero definimos uno nuevo aquí debajo...
revista_clarin = {

    "Nombre": "Clarín",
    "Editorial": "Clarín Bs As",
    "Portada": "Economía Argentina"

}

nombre_revista = revista_clarin["Nombre"] # Accedemos a un valor a través de su clave
print(nombre_revista) # Lo mostramos por pantalla

# Operaciones con los diccionarios:

# keys: Nos permite obtener todas las claves
claves = revista_clarin.keys() 
print(claves)

# values: Nos permite obtener todos los valores
valores = revista_clarin.values()
print(valores)

# items: Permite obtener todos los pares de items
items = revista_clarin.items()
print(items)

# pop: Permite eliminar un par Clave - Valor y obtener su valor
editorial = revista_clarin.pop("Editorial")
print(editorial)

# clear: Permite eliminar todos los elementos de un diccionario
revista_clarin.clear()
print(revista_clarin)