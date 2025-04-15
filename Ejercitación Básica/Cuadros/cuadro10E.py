# Resolución Ejercicio Nº 5:
# Escribe un programa tipo cajero automático que permita:
# a. Iniciar sesión a través de usuario y contraseña
# b. Realizar extracciones.
# c. Realizar depósitos.
# d. Salir

# Definición de usuario y contraseña
usuario_registrado = "mauriciopucheta20@gmail.com"
contraseña_registrada = "admin"

# Definición de intentos para ingresar
intentos_ingreso = 0

# Definición de monto en la cuenta
monto = 500000

# Definición de operaciones posibles
extracciones = 0
depositos = 0
       
# Ingreso de datos
usuario = input("Por favor, indique su nombre de usuario:\n")
contraseña = input("Por favor, ingrese su contraseña:\n")

# Definimos la "flag" para cerrar el bucle externo global
salir_programa = False

# Validación de datos ingresados
if not usuario.strip() or not contraseña.strip():
    print("Error... Campos vacíos no permitidos. Pruebe nuevamente")
else:
    while not (salir_programa):

        if usuario == usuario_registrado and contraseña == contraseña_registrada and intentos_ingreso < 3:

            intentos_ingreso = intentos_ingreso + 1

            print("¡Ingreso exitoso! Por favor, selecciona una de las siguienes operaciones disponibles")
            
            while (True):

                opciones = print(
                    """""
                    1. Consultar dinero disponible
                    2. Realizar extraccion
                    3. Realizar depósito
                    4. Salir
                    """""
                )

                while (True):

                    opcion_usuario = input()
                
                    if not opcion_usuario.strip():
                        print("Error... Campo vacío no permitido... Pruebe nuevamente")
                    else:
                        try:
                            opcion_usuario = int(opcion_usuario)
                            break
                        except ValueError:
                            print("Error... Debes ingresar un valor numérico")

                match opcion_usuario:
                    case 1:
                        # Consultar dinero disponible
                        print(f'Tu monto disponible es: "${monto}"')
                    case 2:
                        # Realizar extracción
                        while (True):

                            extraccion = input("Ingresa el valor de la extracción. Recuerda que debe ser mayor a $1.000,00 y menor a $45.000,00\n")

                            if not extraccion.strip():
                                print("Error... Campo vacío no permitido. Prueba nuevamente")
                            else:
                                try:
                                    extraccion = int(extraccion)

                                    extracciones = extracciones + 1

                                    if extracciones > 3:
                                        print("Error... Llegaste al límite de extracciones diarias")
                                        break

                                    if extraccion > 1000 and extraccion < 45000:
                                        monto = monto - extraccion
                                        print(f'¡Éxito! Extracción de "${extraccion}" realizada')
                                        print(f'Monto disponible: ${monto}')
                                        break
                                    else:
                                        print("Error... Comprueba si el valor de la extracción insertada está dentro de los parámetros indicados")
                                except ValueError:
                                    print("Error... Debes ingresar un valor numérico")
                    case 3:
                        # Realizar un depósito
                        while (True):

                            deposito = input("Ingresa el valor del depósito. Recuerda que debe ser mayor a $50.000,00 y menor a $225.000,00\n")

                            if not deposito.strip():
                                print("Error... Campo vacío no permitido. Prueba nuevamente")
                            else:
                                try:
                                    deposito = int(deposito)

                                    depositos = depositos + 1

                                    if (depositos > 2):
                                        print("Error... Llegaste al límite de depósitos diarios")
                                        break
                                    
                                    if deposito > 50000 and deposito < 225000:
                                        monto = monto + deposito
                                        print(f'¡Éxito! Depósito de "${deposito}" realizado')
                                        print(f'Monto disponible: ${monto}')
                                        break
                                    else:
                                        print("Error... Comprueba si el valor del depósito insertado está dentro de los parámetros indicados")
                                except ValueError:
                                    print("Error... Debes ingresar un valor numérico")
                    case 4:
                        # Salir
                        print("Retirando tarjeta... Espere... ¡Éxito! Adiós")
                        salir_programa = True
                        break

                    case _:
                        print("¡Ops! Parece que estás intentando acceder a una opción no válida... Prueba nuevamente")
        else:
            intentos_ingreso = intentos_ingreso + 1
            print("Error... Contraseña y/o usuarios incorrectos. Pruebe nuevamente")
            usuario = input("Por favor, indique su nombre de usuario:\n")
            contraseña = input("Por favor, ingrese su contraseña:\n")
            if intentos_ingreso > 1:
                print("¡Te quedaste sin intentos! Retirando tarjeta... Espere... ¡Éxito! Adiós")
                break
                        