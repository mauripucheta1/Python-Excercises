# Resolución Ejercicio Nº 1:
# Escribe un programa que solicite tres lados de un triángulo e indique si es equilátero, isósceles o escaleno.
lado_uno = float(input("Ingrese la medida del primer lado de un triangulo, expresado en centímetros:\n"))
lado_dos = float(input("Ingrese la medida del segundo lado de un triangulo, expresado en centímetros:\n"))
lado_tres= float(input("Ingrese la medida del tercer lado de un triangulo, expresado en centímetros:\n"))

if ((lado_uno == lado_dos) and (lado_uno == lado_tres) and (lado_dos == lado_tres)):
    print(f"Acorde a tus medidas ingresadas: {lado_uno}cm, {lado_dos}cm y {lado_tres}cm, es un triangulo equilátero.")
elif ((lado_uno == lado_dos) and (lado_uno != lado_tres)):
    print(f"Acorde a tus medidas ingresadas: {lado_uno}cm, {lado_dos}cm y {lado_tres}cm, es un triangulo isósceles.")
elif ((lado_uno == lado_tres) and (lado_uno != lado_dos)):
    print(f"Acorde a tus medidas ingresadas: {lado_uno}cm, {lado_dos}cm y {lado_tres}cm, es un triangulo isósceles.")
elif ((lado_dos == lado_tres) and (lado_dos != lado_uno)):
    print(f"Acorde a tus medidas ingresadas: {lado_uno}cm, {lado_dos}cm y {lado_tres}cm, es un triangulo isósceles.")
else:
    print(f"Acorde a tus medidas ingresadas: {lado_uno}cm, {lado_dos}cm y {lado_tres}cm, es un triangulo escaleno.")

# Resolución Ejercicio Nº 2:
# Escribe un programa que solicite al usuario que ingrese una contraseña y confirme la contraseña. El programa debe verificar si ambas contraseñas coinciden y no están vacías.
contraseña = input("Ingrese una contraseña:\n")
verificar_contraseña = input("Ingrese nuevamente la contraseña:\n")
while (True):
    if ((len(contraseña) <= 7) or (verificar_contraseña != contraseña)):
        print("¡Error! Contraseña no generada. Intente nuevamente...")
        contraseña = input("Ingrese una contraseña:\n")
        verificar_contraseña = input("Verifique nuevamente su contraseña:\n")
    else:
        print(f"¡Contraseña generada con éxito! Tu nueva contraseña es: {contraseña}. (NO LA COMPARTAS CON NADIE)")
        break

# Resolución Ejercicio Nº 3:
# Escribe un programa que solicite al usuario el precio y la cantidad de un producto. Clasifique el producto como "caro" si el precio es mayor de $100 o si la cantidad es menor que 10 y el precio es
# mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye condiciones para manejar valores falsos (0 o vacío).

precio_producto = input("Ingrese el precio del producto:\n")
cantidad_producto = input("Ingrese la cantidad del producto:\n")

while(True):
        
    if not (precio_producto.strip()) or not (cantidad_producto.strip()):
        print("Error... Ingresaste un valor vacío, por favor, ingresa otro valor nuevamente.")
        if not (precio_producto.strip()):
            print("Ingresa el precio del producto:")
            precio_producto = input()
        if not (cantidad_producto.strip()):
            print("Ingresa la cantidad del producto:")
            cantidad_producto = input()
    else:
        numero_precio_producto = float(precio_producto)
        numero_cantidad_producto = int(cantidad_producto)
        if ((numero_precio_producto <= 0) or (numero_cantidad_producto <= 0)):
            print("No puedes ingresar un valor menor o igual a 0...")
            if (numero_precio_producto <= 0):
                print("Ingresa el precio del producto:")
                precio_producto = input()
            if (numero_cantidad_producto <= 0):
                print("Ingresa la cantidad del producto:")
                cantidad_producto = input()
        else:
            break

if ((numero_precio_producto> 100) or (numero_cantidad_producto < 10 and numero_precio_producto > 50)):
    print("El producto es caro.")
else:
    print("El producto es barato.")

# Resolución Ejercicio Nº 4:
# Escribe un programa que solicite al usuario su nombre, edad y número de teléfono. Verifica que ninguno de estos datos esté vacío o sea un valor falso (por ejemplo, 0).
nombre_usuario = input("¡Hola! Por favor, ingresa tu nombre\n")
edad_usuario = input("Ahora, ingresa tu edad:\n")
numero_telefono_usuario = input("Por último, ingresa tu número de teléfono:\n")

while (True):

    if not (nombre_usuario.strip()) or not (edad_usuario.strip()) or not (numero_telefono_usuario.strip()):
        print("Error... Ingresaste un valor vacío...")
        if not (nombre_usuario.strip()):
            print("Ingresa nuevamente tu nombre:")
            nombre_usuario = input()
        if not (edad_usuario.strip()):
            print("Ingresa nuevamente tu edad:")
            edad_usuario = input()
        if not (numero_telefono_usuario.strip()):
            print("Ingresa nuevamente tu número de teléfono:")
            numero_telefono_usuario = input()
    else:
        verificar_edad_usuario = int(edad_usuario)
        if (verificar_edad_usuario <= 0) or (len(numero_telefono_usuario) < 5):
            print("Error... Ingresaste un número inválido.")
            if (verificar_edad_usuario <= 0):
                edad_usuario = input("Ingresa nuevamente tu edad:\n")
            if (len(numero_telefono_usuario) < 5):
                numero_telefono_usuario = input("Ingresa nuevamente tu número de teléfono:\n")
        else:
            break

print(f"Tus datos ingresados son... Nombre: {nombre_usuario}; Edad: {edad_usuario}; Número de teléfono: {numero_telefono_usuario}.")