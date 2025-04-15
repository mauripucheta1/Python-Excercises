# 1) Bucle While: Permite ejecutar un bloque de código repetidamente siempre y cuando se cumpla una condición

años = 0 # Definimos una variable y le asignamos el valor 0, nos servirá de contador
while años < 21: # Evaluamos, mientras la edad sea menor que 21
    print(f"Tu edad es de {años} años.") # Iremos mostrando por consola esto mientras se valide la condición de arriba
    años+=1 # Iremos aumentando en 1 (puede ser lo que querramos) el contador (años) para que pueda salir del bucle, sino sería infinito, ya que siempre sería 0

# 2) Bucle Do-While: Primero hace y luego valida, no es como el anterior que primero valida y luego hace. Con esto, nos aseguramos que al menos una vez este bloque se va a ejecutar
while True: # Mientras sea verdadero
    peso = int(input("Ingresa tu peso:")) # Pedimos al usuario que ingrese un número
    if (peso > 200): # Realizamos una validación
        print ("No estás apto para pelear, intenta de nuevo") # Mostrará esto en caso de que la condición sea VERDADERA, volviendose a ejecutar el loop
    else:
        print("Estás listo para pelear. ¡Éxitos!") # Mostrará esto en caso de que la condición sea FALSA, saliendo del loop
        break # Gracias a esta intrucción nos permite salir del loop



# ¡Ojo! Entonces ya vimos para que nos sirve la intrucción "break". ¡Nos sirve para salir/interrumpir el bucle!



# Ahora veremos la instrucción "continue"
for i in range (21): # Realizamos un for para recorrer los numeros del 1 al 20
    if (i % 2 == 0): # Decimos que si el resto de dividir i (numero en la vuelta que está dando el for en el rango) entre 2 da como resto 0...
        continue # lo salteamos y avanzamos a la próxima vuelta
    print(f"Número: {i}") # Mostramos por pantalla el número acorde a la vuelta que esté dando el bucle for 



# ¡Ojo! Entonces ya vimos para que nos sirve la instrucción "continue". ¡Para avanzar a la siguiente vuelta en un bucle!



# Ahora veremos la instrucción "pass"
for i in range(10):
    pass



# ¡Ojo! Así de sencillo es la instrucción "pass". Es una declaración nula que no realiza nada durante su ejecución, que se utiliza para mantener la estructura del código. Sirve para definir
# funciones, clases, bucles, etc; que aún no está definidas 



# 3) Bucles anidados: Vamos a realizarlo con un ejemplo sencillo, imprimir tablas de multiplicación
for i in range (1, 11):
    for j in range (1, 11):
        resultado = i * j
        print(f"{j} * {i} = {resultado}")