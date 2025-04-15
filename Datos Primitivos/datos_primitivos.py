# Primero que nada, verán que estas frases están de color verde, entonces estamos ante la presencia de un comentario, el cual se puede realizar de dos formas:
# 1) A través de un hashtag (#): Se pone "#" para realizar un comentario, pero ¡Ojo! solo sirve para una única línea.
    # Ejemplo: Esto es un comentario de una sola línea
# 2) Docstrings: Se utiliza para realizar descripciones extensas o documentar funciones y clases. Se realiza con comillas triples """ y abarca varias líneas de código, ejemplo:
"""
Acabamos de 
realizar
un comentario "docstring"
aunque suele utilizarse con 
otro propósito. Esto es un ejemplo
"""

# Conceptos básicos en Python:
# Temario: 
# 1) Datos Primitivos
# 2) Constantes

# 1) Declaración de "Datos Primitivos": 
# Variables: Pueden cambiar su valor durante la ejecución.
nombre = "Mauricio" # Definimos una variable de tipo "string" (Cadena de texto)
edad = 20 # Definimos una variable de tipo "int" (Número/s entero/s)
altura = 1.83 # Definimos una variable de tipo "float" (De punto flotante, es decir, decimal)
estudiante = True # Definimos una variable de tipo "bool" (Booleana, es decir Verdadero o Falso)
nada = None # Definimos una variable como "NoneType", que representa la ausencia de un valor

# ¡Ojo! Podemos declarar variables que surgan de concatenaciones, por ejemplo:
a = 4
a += 2 # Se suma el valor anterior de A (4) y se asigna nuevamente, resultando A = 6

# Otro ejemplo:
saludo = "¡Adiós!"
saludo += "Que te vaya bien." # Se suman ambos strings (textos), resultando = "¡Adiós! Que te vaya bien."

# 2) Declaración de constantes: No pueden cambiar su valor durante la ejecución.
fecha_nacimiento = "24/09/2004"
dni = 111

# 3) Mostrar una variable, constantes, una función o lo que fuera por pantalla:
print(nombre) # Mostrará por pantalla el valor de esa variable, en este caso: Mauricio
print(dni) # Mostrará por pantalla el valor de esa constante, en este caso: 111

# ¡Ojo! Hasta aquí solamente hemos visto como mostrar por pantalla valores, pero... ¡Podemos concatenarlos! Mediante el uso de 'f-strings':
print(f"¡Hola! Mi nombre es {nombre} y mi edad es {edad}.") # Aquí concatenamos dos variables dentro de un string (Cadena de texto) mediante el uso de llaves {}

# ¡Aclaración! En un ejemplo práctico de la vida real, podemos tener mucho código de programación, por ende, nos puede ocurrir de no poder recordar el tipo de variable que definimos, por eso utilizamos:
print(type(edad)) # Nos mostrará por pantalla el TIPO de variable que hemos definido, en este caso: <class 'int'> (Entero)
print(type(fecha_nacimiento)) # Nos mostrará por pantalla el TIPO de constante que hemos definido, en este caso: <class 'string'> (Cadena de texto)