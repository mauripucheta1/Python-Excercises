# Resolución Ejercicio Nº 3:
# Escribe un programa que tenga un menú para gestionar los usuarios y password de tus aplicaciones.

def mostrar_usuarios(usuarios):
    
    if usuarios:
        for nom, con in usuarios.items():
            print(f'El usuario "{nom}" tiene la siguiente contraseña: "{con}"')
    else:
        print("No tienes ningún usuario registrado")

usuarios = {}

print("¡Bienvenido! A continuación, te mostraremos una serie de acciones que puedes realizar en la aplicación")

while (True):

    opciones = print(
        """
        Seleccione una de las opciones disponibles:
        1. Agregar usuario
        2. Mostrar usuarios
        3. Eliminar usuario
        4. Salir
        """
    )

    opcion_usuario = input()

    if not opcion_usuario.strip():
        print("Error... Campo vacío no permitido. Pruebe nuevamente")
    else:

        opcion_usuario = int(opcion_usuario)
                                
        match opcion_usuario:
            case 1:
                # Agregar usuario
                while (True):

                    nombre_usuario = input("Ingresa el nombre del usuario a registrar:\n")
                    nombre_usuario = nombre_usuario.lower()
                    contraseña_usuario = input("Ingresa la contraseña del usuario:\n")

                    if not (nombre_usuario.strip()) or not (contraseña_usuario.strip()):
                        print("Error... Campos vacíos no permitidos. Pruebe nuevamente")
                    else:
                        usuarios[nombre_usuario] = contraseña_usuario
                        print(f'¡Éxito! El usuario "{nombre_usuario}" ha sido insertado correctamente...')
                        break
            case 2:
                # Mostrar usuarios
                mostrar_usuarios(usuarios)
            case 3:
                # Eliminar usuario
                while (True):

                    nombre_usuario = input("Ingresa el nombre del usuario que deseas eliminar:\n")
                    nombre_usuario = nombre_usuario.lower()

                    if not nombre_usuario.strip():
                        print("Error... Campo vacío no permitido. Prueba nuevamente")
                    else:
                        if nombre_usuario in usuarios:
                            usuarios.pop(nombre_usuario)
                            print(f'¡Éxito! El usuario "{nombre_usuario}" ha sido eliminado correctamente de la lista de usuarios...')
                            break
                        else:
                            print("El usuario no ha sido encontrado en la lista de usuarios...?")
                            break
            case 4:
                # Salir
                print("Saliendo... ¡Éxito! Adiós")
                break
            case _:
                print("¡Ops! Parece que estás intentando seleccionar una opción no disponible. Prueba nuevamente...")

