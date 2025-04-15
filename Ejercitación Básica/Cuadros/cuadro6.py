# Resolución Ejercicio Nº 1:
# Dada la siguiente lista:
amigos = ['Ana', 'Monica', 'José', 'Camila', 'Raquel', 'Matías']

# 1) Devuelve la posición (el index, un número) del amigo “Matías”.

indice_matias = amigos.index("Matías")
print(f'La posición de "Matias" es:', indice_matias)

# 2) Devuelve la misma lista pero añadiendo los amigos de la infancia “Ivana” y “Andrés” como otra lista.

amigos_infancia = ["Ivana", "Andrés"] + amigos
print(f"La nueva lista, queda conformada entonces como: {amigos_infancia}")

# 3) Agrega un nuevo amigo “María” y devuelve el nro de amigos.
amigos_infancia.append("María")
a = 0
for amigo in amigos_infancia:
    a += 1
print(f"La cantidad de amigos en esta lista: {amigos_infancia} es de: {a}")

# 4) Elimina el último elemento amigo y devuelve el nombre del amigo eliminado.
ultimo_amigo_eliminado = amigos_infancia.pop()
print(f"El nombre del último amigo eliminado es: {ultimo_amigo_eliminado}.")

# 5) Devuelve un arreglo ordenado alfabéticamente.
amigos_infancia.sort()
print(f"El arreglo ordenado alfabéticamente resultaría como:", amigos_infancia)