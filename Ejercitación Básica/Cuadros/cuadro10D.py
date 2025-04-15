# Resolución Ejercicio Nº 4:
# Escribe un programa que tenga un menú para gestionar las tareas que permita agregar, marcar como completadas y mostrar tareas pendientes.

def mostrar_tareas_pendientes(tareas):

    if tareas:
        print("Tus tareas pendientes son:")
        for tarea, estado in tareas.items():
            if estado == "pendiente":
                print(f'"{tarea}"')
    else:
        print("No tienes tareas pendientes")

tareas = {}

print("¡Bienvenido a NotApp! Aquí podras realizar las siguientes operaciones...")

while (True):

    opciones = print(
        """""
        Por favor, selecciona una:
        1. Crear tarea
        2. Actualizar tarea
        3. Mostrar tareas pendientes
        4. Salir
        """""
    )

    opcion_usuario = input()

    if not opcion_usuario.strip():
        print("Error... Campo vacío no permitido. Prueba nuevamente")
    else:

        opcion_usuario = int(opcion_usuario)

        match opcion_usuario:
            case 1:
                # Crear tarea
                while (True):

                    tarea = input("Por favor, inserta la tarea que deseas almacenar:\n")
                    estado = input("Por favor, indica también el estado de la misma:\n")

                    if not (tarea.strip()) or not (estado.strip()):
                        print("Error... Campos vacíos no permitodos. Prueba nuevamente")
                    else:
                        estado = estado.lower()
                        tareas[tarea] = estado
                        print(f'¡Éxito! La tarea "{tarea}" se ha agregado correctamente a tu lista de tareas')
                        break
            case 2:
                # Actualizar tarea
                while (True):

                    tarea = input("Por favor, indique el nombre de la tarea que le gustaría modificar:\n")
                    estado = input("Por favor, indique también el estado de la misma:\n")

                    if not (tarea.strip()) or not (estado.strip()):
                        print("Error... Campos vacíos no permitidos. Pruebe nuevamente")
                    else:
                        if tarea in tareas:
                            tareas[tarea] = estado
                            print(f'¡Éxito! Ahora la tarea "{tarea}" tiene estado "{estado}"')
                            break
                        else:
                            print(f'Error... La tarea "{tarea}" no existe dentro de tu lista de tareas')
                            break
            case 3:
                # Mostrar tareas pendientes
                mostrar_tareas_pendientes(tareas)
            case 4:
                # Salir
                print("Saliendo... ¡Éxito! Adiós")
                break
            case _: 
                print("¡Ops! Parece que estás intentando acceder a una opción no disponible... Prueba nuevamente")