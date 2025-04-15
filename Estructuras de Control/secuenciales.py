# 1) Estructura Secuencial: Representan el flujo de manera lineal, por ejemplo:

# ¡Ojo! Haremos uso de los "input", que básicamente es una instrucción que se ejecuta y queda en espera hasta que ingresemos un valor

# Solicitamos que ingreses tu nombre
nombre = input("Ingresa tu nombre")

# Solicitamos que ingreses tu edad
edad = int(input("Ingresa tu edad")) # Transformamos a int (entero) el valor ingresado

# Realizamos una operación aritmética
doble_edad = edad * 2

# Mostramos un mensaje final
print(f"¡Hola {nombre}! Al parecer, tu edad es de {edad} años, por ende no tienes acceso. Tendrías que esperar a tu doble de edad, es decir {doble_edad} años. ¡Lo siento!")