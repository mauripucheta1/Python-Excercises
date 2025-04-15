# Resolución Ejercicio Nº 1:
# Escribe un programa que administre el inventario de una tienda. El programa debe permitir agregar nuevos productos, actualizar las cantidades de los productos existentes, y mostrar el
# inventario actual.

inventario_productos = {

}

print("No posees productos con sus respectivas cantidades de momento...")

while (True):

    agregar_producto = input('¿Desea agregar productos? Por favor, digite "SI" o "NO"\n')
    agregar_producto = agregar_producto.lower()

    if not agregar_producto.strip():
        agregar_producto = input("Valor vacío, ingrese nuevamente:\n")
    else:

        if agregar_producto == "si":
            nombre_producto = input("Escriba el nombre del producto:\n")
            cantidad_producto = input(f"Escriba la cantidades del producto {nombre_producto}:\n")

            while (True):

                if not (nombre_producto.strip()) or not (cantidad_producto.strip()):
                    print("Valores vacíos no permitidos")
                    if not nombre_producto.strip():
                        nombre_producto = input("Ingrese un nombre correctamente:\n")
                    if not cantidad_producto.strip():
                        cantidad_producto = input("Ingrese la cantidad correctamente:\n")
                else:
                    cantidad_producto_entero = int(cantidad_producto)
                    inventario_productos[nombre_producto] = cantidad_producto_entero
                    break
        else:
            if agregar_producto != "no":
                print("Por favor, ingresa una respuesta válida...")
            else:
                break

if inventario_productos:

    while (True):

        opcion_actualizar = input('¿Deseas actualizar algún producto? Digite "SI" o "NO", por favor...\n')
        opcion_actualizar = opcion_actualizar.lower()

        if not opcion_actualizar.strip():
            opcion_actualizar = input("Valores vacíos no permitidos...\n")
        else:
            if (opcion_actualizar == "si"):
                nombre_producto = input("Escriba el nombre del producto a actualizar:\n")
                cantidad_producto = input(f'Escriba la cantidades del producto "{nombre_producto}" a actualizar:\n')

                while (True):

                    if not (nombre_producto.strip()) or not (cantidad_producto.strip()):
                        print("Valores vacíos no permitidos")
                        if not nombre_producto.strip():
                            nombre_producto = input("Ingrese un nombre correctamente:\n")
                        if not cantidad_producto.strip():
                            cantidad_producto = input("Ingrese la cantidad correctamente:\n")
                    else:
                        if nombre_producto in inventario_productos:
                            cantidad_producto_entero = int(cantidad_producto)
                            inventario_productos[nombre_producto] = cantidad_producto_entero
                            print(f'¡El producto "{nombre_producto}" con cantidades "{cantidad_producto_entero}" ha sido actualizado correctamente!')
                        else:
                            print(f"Error... El nombre del producto {nombre_producto} no existe en el inventario, pruebe nuevamente.")
                        break
            else:
                if opcion_actualizar != "no":
                    print("Por favor, ingresa una respuesta válida...")
                else:
                    break

if not inventario_productos:
    print("Tu inventario final es: Productos: 0, Cantidades: 0")
else:
    for prod, cant in inventario_productos.items():
            print(f"Nombre producto: {prod}, Cantidad: {cant}.")


# Resolución Ejercicio Nº 2:
# Escribe un programa que permita llevar un registro de las calificaciones de varios estudiantes. El programa debe permitir agregar estudiantes con sus calificaciones, actualizar las
# calificaciones de un estudiante existente y mostrar el promedio de calificaciones de un estudiante específico.

registro_calificaciones = {

}

print("De momento, no posees alumnos con sus respectivas calificaciones...")

while (True):

    ingresar_registro = input('¿Desea agregar un alumno con una calificación? Por favor, digite "SI" o "NO"\n')
    ingresar_registro= ingresar_registro.lower()

    if not ingresar_registro.strip():
        ingresar_registro= input("Error... Valores vacíos no permitidos. Pruebe nuevamente:\n")
    else:
        if ingresar_registro == "si":
            nombre_alumno = input("Por favor, ingresa el nombre del alumno:\n")
            calificacion = input("Por favor, ingresa la calificación del mismo:\n")

            while (True):

                if not (nombre_alumno.strip()) or not (calificacion.strip()):
                    print("Error... Valores vacíos no permitidos")
                    if not nombre_alumno.strip():
                        nombre_alumno = input("Pruebe nuevamente ingresar el nombre del alumno:\n")
                    if not calificacion.strip():
                        calificacion = input("Pruebe nuevamente ingresar la calificación del alumno:\n")
                else:
                    calificacion_entero = float(calificacion)
                    registro_calificaciones[nombre_alumno] = calificacion_entero
                    break
        else:
            if (ingresar_registro != "no"):
                print("Respuesta inválida, por favor, ingrese una opción correcta")
            else:
                break

if registro_calificaciones:

    while (True):

        actualizar_registro = input('¿Desea actualizar la calificación de un alumno? Por favor, digite "SI" o "NO"\n')
        actualizar_registro= actualizar_registro.lower()

        if not actualizar_registro.strip():
            actualizar_registro = input("Error... Valores vacíos no permitidos. Pruebe nuevamente:\n")
        else:
            if actualizar_registro == "si":
                nombre_alumno = input("Ingrese el nombre del alumno a actualizar:\n")
                calificacion = input("Ingrese la nueva calificación del mismo:\n")

                while (True):

                    if not (nombre_alumno.strip()) or not (calificacion.strip()):
                        if not nombre_alumno.strip():
                            nombre_alumno = input("Error, campo vacío... Pruebe insertar nuevamente el nombre del alumno a actualizar:\n")
                        if not calificacion.strip():
                            calificacion = input("Error, campo vacío... Pruebe insertar nuevamente la calificación actualizada del alumno:\n")
                    else:
                        if nombre_alumno in registro_calificaciones:
                            calificacion_decimal = float(calificacion)
                            registro_calificaciones[nombre_alumno] = calificacion_decimal
                            print(f"El alumno {nombre_alumno} ha actualizado su nota a {calificacion_decimal}")
                            break 
                        else:
                            print("Error... Alumno no encontrado. Pruebe nuevamente")
                            break
            else:
                if actualizar_registro != "no":
                    print("Error... Por favor, digite una opción válida. Pruebe nuevamente")
                else:
                    break


if registro_calificaciones:
    for nombre_alumno, calificacion_decimal in registro_calificaciones.items():
        print(f"Nombre alumno: {nombre_alumno}, Calificación: {calificacion_decimal}")     
else:
    print("Tu registro finalizó con: Alumnos: 0 y Calificaciones: 0")