# Resolución Ejercicio Nº 1:
# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

numero_tres_digitos = input("Ingrese un número de tres digitos para ser invertido:\n")
numero_tres_digitos_invertido = numero_tres_digitos[::-1]
print(f'El numero "{numero_tres_digitos}" de manera invertida es "{numero_tres_digitos_invertido}"')

# Resolución Ejercicio Nº 2:
# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas.

t = int(input("Ingrese la hora acual (SOLO HORA):\n"))
h = int(input("Ingrese la cantidad de horas proyección para conocer el resultado de la hora:\n"))
hora_futura = (t + h) % 24
print(f'El {t} horas, el reloj marcará "{hora_futura}:00,00"')

# Resolución Ejercicio Nº 3:
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero_primo = int(input("Ingrese un número entero para saber si es primo:\n"))

if numero_primo < 2:
    print("El numero no es primo")
else:
    es_primo = True
    for i in range(2, int(numero_primo ** 0.5) + 1): 
        if numero_primo % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"El número {numero_primo} es primo.")
    else:
        print(f"El número {numero_primo} no es primo.")

# Resolución Ejercicio Nº 4:
# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje. Desarrolle un programa que permita ingresar los tiempos de 
# viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos. El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

tiempo_almacenado = 0
while (True):
    
    tiempo = int(input("Ingresa la cantidad de minutos del viaje:\n"))

    if tiempo != 0:
        tiempo_almacenado = tiempo_almacenado + tiempo
    else:
        horas = int((tiempo_almacenado / 60))
        minutos = tiempo_almacenado % 60
        print(f'El tiempo total de viaje es de {horas} horas y {minutos} minutos')
        break

# Resolución Ejercicio Nº 5:
# Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un 
# cuarto de día. Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional en los años divisibles por 4 
# (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados. Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
# Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.
# Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año.

año = int(input("Por favor, ingrese un año para saber si es bisiesto, o no:\n"))

if año < 1852:
    if año % 4 == 0:
        print(f'El año {año} es bisiesto (calendario juliano)')
    else:
        print(f'El año {año} no es bisiesto (calendario juliano)')
else:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto (calendario gregoriano)")
    else:
        print(f"El año {año} no es bisiesto (calendario gregoriano)")

# Resolución Ejercicio Nº 6:
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo con tantos renglones como indique el usuario.

filas = int(input("Ingrese un número entero para la cantidad de renglones del triángulo:\n"))
print(f'Cantidad de renglones deseados: {filas}')
for i in range(1, filas + 1):
    numero = i * 2
    for j in range(i):
        print(numero - (j * 2), end=" ")
    print()

# Resolución Ejercicio Nº 7:
# La secuencia de Collatz de un número entero se construye de la siguiente forma:
# Si el número es par, se lo divide por dos;
# Si es impar, se le multiplica tres y se le suma uno;
# La sucesión termina al llegar a uno.

numero_collatz = int(input('Ingresa un número para saber su secuencia de "Collatz":\n'))
print(f'Numero ingresado: {numero_collatz}')
while numero_collatz != 1:
    print(numero_collatz, end= "-->")
    if numero_collatz % 2 == 0:
        numero_collatz = numero_collatz / 2
    else:
        numero_collatz = numero_collatz * 3 + 1
print("1")

# Resolución Ejercico Nº 8:
# Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011 en el campus Vitacura.
# Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10, $50 y $100.
# Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio del producto,
# el programa debe entregar las monedas de vuelto, una por una.

precios = {
    1: 270,
    2: 340,
    3: 390
}
print(
    """
    Productos disponibles:
    1. A = $270
    2. B = $340
    3. C = $390
    """
)
opcion = int(input("Elige el número del producto que deseas comprar:\n"))

if opcion not in precios:
    print("Opción inválida. Intenta nuevamente.")
else:
    precio = precios[opcion]
    dinero_ingresado = 0

    # Ingreso de monedas hasta cubrir el monto
    print(f"Debes pagar ${precio}. Ingresa monedas de $10, $50 o $100:")
    while dinero_ingresado < precio:
        moneda = int(input("Ingresa moneda:\n"))
        if moneda in [10, 50, 100]:
            dinero_ingresado += moneda
            print(f"Total ingresado: ${dinero_ingresado}")
        else:
            print("Moneda no aceptada. Solo se aceptan $10, $50 y $100")

    # Cálculo del vuelto
    vuelto = dinero_ingresado - precio
    print(f"\nProducto comprado. Vuelto a entregar: ${vuelto}")

    # Entrega del vuelto con monedas una por una
    for moneda in [100, 50, 10]:
        while vuelto >= moneda:
            print(f"Entregando moneda de ${moneda}")
            vuelto -= moneda
