# Función para registrar un usuario
def registrar_usuario(usuarios):
     while (True):
            nombre_usuario = input("Por favor, ingresa el nombre del usuario que deseas registrar:\n").lower()
            edad_usuario = input("Por favor, ingresa la edad del usuario:\n")

            if not nombre_usuario.strip() or not edad_usuario.strip():
                print("Error... Campo/s vacío/s no permitido/s. Pruebe nuevamente")
            else:
                try:
                    edad_usuario = int(edad_usuario)
                    usuarios[nombre_usuario] = edad_usuario
                    print(f'¡Éxito! El usuario "{nombre_usuario}" ha sido agregado exitosamente a la lista de usuarios')
                    break
                except ValueError:
                    print("Error... Comprueba que la edad sea un número válido y prueba nuevamente")