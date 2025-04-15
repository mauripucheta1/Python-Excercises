# Resolución Problema Nº 1:
# Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es par o impar.
numero_a_verificar = int(input("Ingrese un numero entero positivo: \n"))

while (numero_a_verificar <= 0):
    print("¡Ingresaste un valor inferior o igual a 0! Por favor, ingresa otro:")
    numero_a_verificar = int(input())
    if (numero_a_verificar > 0):
        break


resultado = numero_a_verificar % 2

if (resultado == 0):
    print(f"El numero {numero_a_verificar} ingresado es PAR")
else:
    print(f"El numero {numero_a_verificar} ingresado es IMPAR")

# Resolución Problema Nº 2:
# Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es primo o no.
numero_ingresado = int(input("Ingrese un número entero positivo para verificar si es primo o no:\n"))

if numero_ingresado < 2:
    print(f"El número {numero_ingresado} no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero_ingresado ** 0.5) + 1): 
        if numero_ingresado % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"El número {numero_ingresado} es primo.")
    else:
        print(f"El número {numero_ingresado} no es primo.")

# Resolución Problema Nº 3:
# Escribe un programa que permita realizar la división de dos números siempre y cuando el denominador no sea 0.
numerador = int(input("Ingrese un numerador a dividir:\n"))
denominador = int(input("Ingrese un denominador para dividir mayor a 0:\n"))

while (denominador <= 0):
    print(f"Acabas de ingresar como denominador {denominador}, por ende no puedes realizar la división.")
    denominador = int(input("Ingrese otro denominador:\n"))

    if (denominador > 0):
        resultado = float(numerador / denominador)
        print(f"El resultado de dividir {numerador} / {denominador} es igual a: {resultado}.")
        break
