# Resolución Ejercicio Nº 1:
# Escribe un programa para llevar la gestión de usuarios de una aplicación. La misma debe permitir registrar usuarios, eliminar y buscar usuarios utilizando módulos. Para ello,
# Define un módulo para manejar las operaciones relacionadas con los usuarios.
# Define otro módulo para el programa principal que presente un menú para seleccionar la operación y manejar las entradas del usuario.

from registrar import registrar_usuario
from buscar import buscar_usuario
from eliminar import eliminar_usuario

usuarios = {}

print("¡Bienvenido! A continuación te describiremos una serie de opciones de las cuales deberás optar por una")

while (True):

    print(
        """
        ¿Qué operación deseas realizar?
        1. Registrar un usuario
        2. Buscar un usuario
        3. Eliminar un usuario
        4. Salir
        """
    )

    opcion_usuario = input("Para seleccionar una opción digite un número:\n")

    if not opcion_usuario.strip():
        print("Error... Campo vacío no permitido. Pruebe nuevamente")
    else:
        
        opcion_usuario = int(opcion_usuario)

        match opcion_usuario:
            case 1:
                registrar_usuario(usuarios)
            case 2:
                buscar_usuario(usuarios)
            case 3:
                eliminar_usuario(usuarios)
            case 4:
                print('Saliendo... ¡Éxito! Adiós')
                break
            case _:
                print('¡Ops! Parece que estás intentando acceder a una opción no disponible. Prueba nuevamente')