# Función para buscar un usuario
def buscar_usuario(usuarios):
    while (True):

        nombre_usuario = input("Por favor, ingresa el nombre del usuario que deseas buscar:\n").lower()

        if not nombre_usuario.strip():
                print("Error... Campo vacío no permitido. Pruebe nuevamente")
        else:
            if nombre_usuario in usuarios:
                 edad_usario = usuarios[nombre_usuario]
                 print(f'¡Éxito! Usuario: {nombre_usuario}, Edad: {edad_usario}')
            else:
                print("Error... Usuario no encontrado. Pruebe nuevamente")
            break