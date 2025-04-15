# Resolución Ejercicio Nº 2:
# Escribe un programa que tenga un menú para gestionar una lista de contactos.
# a. Agregar Contacto
# b. Eliminar Contacto
# c. Mostrar Contacto
# d. Salir

# Importamos expresiones regulares
import re

telefono_regex = re.compile(r"^[\+\d\(\)\-\s]+$")

def mostrar_contacto(contactos):
    
    if contactos:
        for nom, num in contactos.items():
            print(f'El contacto "{nom}" tiene el número: {num}.')
    else:
        print("La lista de contactos está vacía")

contactos = {

}

print("¡Bienvenido! A continuación te pediremos que selecciones una de las opciones válidas...")

while (True):

    # Opciones 
    opciones_disponibles = print(
    """
    Opciones disponibles:
    a. Agregar contacto
    b. Eliminar contacto
    c. Mostrar contacto
    d. Salir 
    """
    )

    # Opción del usuario
    opcion_usuario = input("Por favor, digite alguna de las opciones presentes:\n")

    # Validamos campos vacíos o ejecutamos correctamente la opción
    if not opcion_usuario.strip():
        print(("Error... Campo vacío no permitido. Pruebe nuevamente"))
    else:
        opcion_usuario = opcion_usuario.lower()
        match opcion_usuario:
            case "a":
                # Agregar contacto
                while (True):

                    nombre_contacto = input("Ingresa el nombre del contacto que deseas agregar a tu lista:\n")
                    nombre_contacto = nombre_contacto.lower()
                    numero_contacto = input("Ingresa el número del contacto:\n")

                    if not (nombre_contacto.strip()) or not (numero_contacto.strip()):
                        print("Campos vacíos no permitidos. Prueba nuevamente")
                    elif not telefono_regex.match(numero_contacto):
                        print("Error... El número ingresado no es válido. Asegúrate de que solo contenga números, guiones, espacios y/o signos '+'")
                    else:
                        contactos[nombre_contacto] = numero_contacto
                        print(f'El contacto "{nombre_contacto}" con número "{numero_contacto}" ha sido agregado exitosamente a la lista de contactos...')
                        break
            case "b":
                # Eliminar contacto
                while (True):

                    nombre_contacto = input("Ingresa el nombre del contacto que deseas eliminar en tu lista:\n")
                    nombre_contacto = nombre_contacto.lower()
                    
                    if not nombre_contacto.strip():
                        print("Error... Campo vacío no permitido. Prueba nuevamente")
                    else:
                        if nombre_contacto in contactos:
                            numero_contacto = contactos[nombre_contacto]
                            contactos.pop(nombre_contacto)
                            print(f'El contacto "{nombre_contacto}" con número "{numero_contacto}" ha sido eliminado exitosamente de la lista de contactos...')
                            break
                        else:
                            print("El contacto no existe en tu lista de contactos")
                            break
            case "c":
                # Mostrar contacto
                while (True):

                    nombre_contacto = input("Ingresa el nombre del contacto que deseas buscar:\n")
                    nombre_contacto = nombre_contacto.lower()

                    if not (nombre_contacto.strip()):
                        print("Error... Campo vacío no permitido. Prueba nuevamente")
                    else:
                        if nombre_contacto in contactos:
                            numero_contacto = contactos[nombre_contacto]
                            print(f'El contacto "{nombre_contacto}" posee el número "{numero_contacto}"')
                            break
                        else:
                            print("El contacto no existe en tu lista de contactos")
                            break
            case "d":
                # Salir
                print("Saliendo... ¡Éxito! Adiós")
                break
            case _:
                print("Error... Por favor, selecciona una opción válida dentro de las indicadas...")
                    
