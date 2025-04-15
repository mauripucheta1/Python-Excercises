# 1) Conversiones: Podemos realizar conversiones entre distintos tipos de variables numéricas, como por ejemplo:

# Conversión a int (entero):
numero_a_entero = int(88.2)

# Conversión a float (flotante, decimal):
numero_a_decimal = float(44)

# Conversión a complex (Complejo)
numero_a_complejo = 17

# 2) Operadores aritméticos: Correspondientes a matemáticas básica
numero_uno = 20 # Definimos un primer número
numero_dos = 60 # Definimos un segundo número

# Suma: Lo realizamos con el operador "+"
resultado = numero_uno + numero_dos # Sumamos los dos y lo almacenamos en una variable
print(f"La suma de {numero_uno} + {numero_dos} da como resultado: {resultado}") # Mostramos por pantalla el resultado de la suma

# Resta: Lo realizamos con el operador "-"
resultado = numero_dos - numero_uno
print(f"La resta de {numero_dos} - {numero_uno} da como resultado: {resultado}") # Mostramos por pantalla el resultado de la resta

# Multiplicación: Lo realizamos con el operador "*"
resultado = numero_uno * numero_dos
print(f"La multiplicación de {numero_uno} * {numero_dos} da como resultado: {resultado}") # Mostramos por pantalla el resultado de la multiplicación

# Divisón: Lo realizamos con el operador "/"
resultado = numero_dos / numero_uno
print(f"La división de {numero_dos} / {numero_uno} da como resultado: {resultado}") # Mostramos por pantalla el resultado de la división

# Módulo: Lo realizamos con el operador "%"
resultado = numero_dos % numero_uno
print(f"El resto de {numero_dos} entre {numero_uno} da como resultado: {resultado}") # Mostramos por pantalla el resultado del módulo

# Potenciación: Lo realizamos con **
resultado = numero_uno**numero_dos
print(f"El resultado de elevar {numero_uno} por {numero_dos} da como resultado: {resultado}") # Mostramor por pantalla el resultado de la potencia


# 3) Operadores de asignación: Se utilizan para asignar valores a las variables
a = 2 # Asignación simple (=)
a += 2 # Agrega y asigna (+=)
a -= 1 # Resta y asigna (-)
a *= 3 # Multiplica y asigna (*=)
a /= 1 # Divide y asigna (/=)


# 4) Operadores lógicos: Combinan dos o más condiciones y devuelven como resultado "True" o "False"
# Operador lógico "AND"
resultado = ((numero_uno > 19) and (numero_dos > 40)) # Defino en una variable el resultado de esta comparación
print("(numero_uno > 19) AND (numero_dos > 40)", resultado) # Muestra por pantalla la comparación escrita entre comillas y devuelve el valor booleano, en este caso True
resultado = ((numero_uno > 30) and (numero_dos < 33)) # Defino en una variable el resultado de esta comparación
print("(numero_uno > 30) AND (numero_dos < 33)", resultado) # Muestra por pantalla la comparación escrita entre comillas y devuelve el valor booleano, este caso False

# Operador lógico "OR"
resultado = ((numero_uno > 15) or (numero_dos > 33)) # Defino en una variable el resultado de esta comparación
print("(numero_uno > 15) OR (numero_dos > 33)", resultado) # Muestra por pantalla la comparación escrita entre comillas y devuelve el valor booleano, en este caso True
resultado = ((numero_uno < 15) or (numero_dos < 33)) # Defino en una variable el resultado de esta comparación
print("(numero_uno < 15) OR (numero_dos < 33)", resultado) # Muestra por pantalla la comparación escrita entre comillas y devuelve el valor booleano, en este caso False

# Operador lógico "NOT"
resultado = not((numero_uno > 8) and (numero_dos > 58))
print("not (numero_uno > 8) AND (numero_dos > 58)", resultado) # Muestra por pantalla la comparación entre comillas con la negación incluída anteriormente y devuelve el valor False

# 5) Operadores de comparación (relacionales):
print(numero_uno == numero_dos) # Muestra por pantalla False, ya que no son iguales
print(numero_uno != numero_dos) # Muestra por pantalla True, ya que son diferentes
print(numero_uno > numero_dos) # Muestra por pantalla False, ya que no es mayor
print(numero_uno < numero_dos) # Muestra por pantalla True, ya que es menor
print(numero_uno >= numero_dos) # Muestra por pantalla False, ya que no es mayor ni igual
print(numero_uno <= numero_dos) # Muestra por pantalla True, ya que en este caso no es igual pero si es menor

# 6) Operadores condicionales (ternario):
resultado = "Par" if numero_dos % 2 == 0 else "Impar" # Mostraremos por pantalla "Par" en caso de que el resto sea igual a 0, caso contrario, será "Impar"
print(resultado) # Mostrará por pantalla "Par"
# Otro ejemplo:
edad = 18
descuento = 10 if edad >= 18 else 5 # Mostraremos por pantalla un descuento del X% acorde a la condición que se cumpla, en este caso 10% por ser igual a 18 
print(f"El descuento es del: {descuento}%") # Mostrará por pantalla "El descuento es del 10%"