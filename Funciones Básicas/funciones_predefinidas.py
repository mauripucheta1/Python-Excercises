# 1) Funciones predefinidas (built-in): Python nos proporciona una serie de funciones ya predefinidas, tales como:


# Funciones Matemáticas:
# abs(x): Retorna el valor absoluto de un número
a = -5
print(f"El valor absoluto de {a} es:", abs(a)) 

# round(x, n): Redondea un número al número de decimales especificados
numero = 3.3252523525252523525
print(f"El numero {numero} redondeado a dos decimales es:", round(numero, 2))

# max(iterable): Retorna el valor máximo de una secuencia
numeros = [1, 5, 3, 9]
print(f"El valor máximo de esta secuencia es:", max(numeros))  

# min(iterable): Retorna el valor mínimo de una secuencia
print(f"El valor mínimo de esta secuencia es:", min(numeros))  

# sum(iterable): Retorna la suma de los elementos de una secuencia
print(f"La suma de los elementos de mi secuencia da como resultado:", sum(numeros))


# Funciones de conversión de Datos:
# int(x): Convierte un valor a entero
numero = "22222"
print(f"El valor {numero} convertido a un numero entero es:", int(numero))

# float(x): Convierte un valor a decimal
print(f"El valor {numero} convertido a decimal es:", float(numero))

#str(x): Convierte un valor a un string
numero_dos = 364436
print(f"El numero {numero_dos} convertido a string es:", str(numero_dos))

# list(iterable): Convierte una secuencia en una lista
texto_saludo = "Hola"
print(f"El texto '{texto_saludo}' convertido a lista quedaría algo como:", list(texto_saludo))


# Funciones de Manejo de Cadenas:
# len(s): Retorna la longitud de una cadena o secuencia
print(f"La longitud de este texto: '{texto_saludo}' es de:", len(texto_saludo))

# str.upper(): Convierte una cadena a mayúsculas
print(f"El texto '{texto_saludo}' en mayúsculas luciría algo como:", texto_saludo.upper())

# str.lower(): Convierte una cadena a minúsculas
print(f"El texto '{texto_saludo}' en minúsculas luciría algo como:", texto_saludo.lower())

# str.strip(): Elimina espacios en blanco al final y principio de una cadena
texto_saludo_largo = "                                ¡Hola!                                      "
print(f"Si al texto '{texto_saludo_largo}' le suprimimos los espacios, quedaría algo como:", texto_saludo_largo.strip())


# Funciones de Lógica y Comparación:
# bool(x): Convierte un valor a booleano
b = 0
c = 1
print(f"El valor de B, equivalente a '{b}', trasladado a valor booleano sería:", bool(b))
print(f"El valor de C, equivalente a '{b}', trasladado a valor booleano sería:", bool(c))

# all(iterable): Retorna "True" si todos los elementos de una secuencia son verdaderos.
lista_all = [1, True, "Mauricio"]
print(f"Todos los valores de mi lista, expresados en booleano, equivalen a:", all(lista_all))

# any(iterable): Retorna "False" si todos los elementos de una secuencia son falsos.
lista_all = [0, False]
print(f"Todos los valores de mi lista, expresados en booleano, equivalen a:", any(lista_all))


# Funciones de Matríces y Listas: 
# len(list): Retorna la longitud de una lista
print(f"La longitud de la lista '{lista_all}' es de:", len(lista_all))

# append(list): Agrega un elemento al final de la lista
lista_all.append("Pucheta")
print(f"Mi lista modificada quedaría algo como: {lista_all}")

# list.pop(index): Elimina y retorna un elemento de una lista
lista_final = ["Mauricio", 20, "Pucheta"]
nombre_programador = lista_final.pop(0)
print(f"Nombre programador: {nombre_programador}")
print(f"Lista finalizada: {lista_final}")