# Función para eliminar un usuario
def eliminar_usuario(usuarios):

    while (True):

        nombre_usuario = input("Por favor, ingresa el nombre del usuario que deseas eliminar:\n").lower()

        if not nombre_usuario.strip():
            print("Error... Campo vacío no permitido. Pruebe nuevamente")
        else:
            if nombre_usuario in usuarios:
                edad = usuarios.pop(nombre_usuario)
                print(f'¡Éxito! El usuario "{nombre_usuario}" con edad {edad} ha sido eliminado exitosamente de la lista de usuarios')
            else:
                print("Error... Usuario no encontrado. Pruebe nuevamente")
            break