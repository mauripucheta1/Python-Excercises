# Resolución Ejercicio Nº 1:
# Crea una función para calcular el área de un triángulo. Si no se proporciona la altura, asumimos una altura de 1.

def calcular_area_triangulo(h = 1):

    base = float(input("Ingresa la longitud de la base:\n"))
    area = (base * h) / 2
    print(f'El área de un triangulo es "{area}"')

calcular_area_triangulo()

# Resolución Ejercicio Nº 2:
# Crea una función para saludar con un mensaje personalizado. Si no se proporciona el nombre, asumimos “Invitado”.

def saludar(nombre = "Invitado"):

    print(f'¡Hola {nombre}! ¿Cómo estás?')

saludar()

# Resolución Ejercicio Nº 3:
# Crea una función para proporcionar un porcentaje de descuento. Si no se proporciona el porcentaje, asumimos 10%.

def descuento_o_no(precio_producto, descuento = 10):

    valor_descuento = (precio_producto * descuento) / 100
    precio_final = precio_producto - valor_descuento
    print(f'El precio del producto ${precio_producto} ha sufrido un descuento del {descuento}%, resultando un precio final de ${precio_final}')

descuento_o_no(100)