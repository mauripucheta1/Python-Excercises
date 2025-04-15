# Resolución Ejercicio Nº 1:
# Escribe un programa que tenga un menú para gestionar un inventario de productos:
# a. Agregar Producto
# b. Mostrar Inventario
# c. Buscar Producto
# d. Eliminar Producto
# e. Salir

def mostrarInventario(inventario):

    if inventario:
        for prod, cant in inventario.items():
            print(f'Producto: {prod}, Cantidad: {cant}')
    else:
        print("El inventario está vacío")

inventario = {

}

while (True):

    # Opciones
    opciones = print(
        """
        Bienvenido... Seleccione cualquiera de estas opciones digitando el número de la opción correspondiente:
        1. Agregar productos
        2. Mostrar inventario
        3. Buscar producto
        4. Eliminar producto
        5. Salir
        """)
    
    # Seleccionar opción
    opcion_usuario = input("¿Qué deseas realizar?\n")
    
    # Verificar campo vacío
    if not opcion_usuario.strip():
        opcion_usuario = input("Error... Campo vacío, pruebe nuevamente elegir una opción:\n")
    else:

        opcion_usuario = int(opcion_usuario)

        match opcion_usuario:
            case 1:
                # Agregar producto
                while (True):

                    nombre_producto = input("Ingrese el nombre del producto a agregar:\n")
                    cantidad_producto = input("Ingrese la cantidad del producto:\n")
                    nombre_producto = nombre_producto.lower()

                    if not nombre_producto.strip() or not (cantidad_producto.strip()):
                        if not nombre_producto.strip():
                            nombre_producto = input("Campo vacío no permitido. Por favor, ingrese el nombre del producto:\n")
                        if not cantidad_producto.strip():
                            cantidad_producto = input("Campo vacío no permitido. Por favor, ingrese la cantidad del producto:\n")
                    else:
                        cantidad_producto = cantidad_producto.replace(" ", "")
                        cantidad_producto = int(cantidad_producto)
                        if cantidad_producto <= 0:
                            print("Error... La cantidad del producto tiene que ser superior a 0")
                        else:
                            inventario[nombre_producto] = cantidad_producto
                            print(f'El producto "{nombre_producto}" ha sido agregado exitosamente al inventario')
                            break
            case 2:
                # Ver inventario
                (mostrarInventario(inventario))
            case 3:
                # Buscar un prodcuto
                while (True):

                    buscar_producto = input('Inserte el nombre del producto que desea obtener:\n')
                    buscar_producto = buscar_producto.lower()
                    
                    if not buscar_producto.strip():
                        buscar_producto = input("Error... Campo vacío no permitido. Pruebe nuevamente...\n")
                    else:
                        if buscar_producto in inventario:
                            cantidad = inventario[buscar_producto]
                            print(f'El producto "{buscar_producto}" tiene una cantidad de: {cantidad}')
                            break
                        else:
                            print(f'Error... El producto "{buscar_producto}" no existe dentro del inventario')
                            break

            case 4:
                # Eliminar un producto
                while (True):

                    eliminar_producto = input('Inserte el nombre del producto que desea eliminar:\n')
                    eliminar_producto = eliminar_producto.lower()

                    if not eliminar_producto.strip():
                        eliminar_producto = input("Error... Campo vacío no permitido. Pruebe nuevamente...\n")
                    else:
                        if eliminar_producto in inventario:
                            inventario.pop(eliminar_producto)
                            print(f'El producto "{eliminar_producto}" ha sido eliminado exitosamente del inventario')
                            break
                        else:
                            print(f'Error... El producto "{eliminar_producto}" no existe dentro del inventario')
                            break
            case 5:
                print("Saliendo... ¡Éxito! Adiós")
                break
            case _:
                print("Error... Estás intentando acceder a una opción no válida. Por favor, inserta una opción acorde")
                    