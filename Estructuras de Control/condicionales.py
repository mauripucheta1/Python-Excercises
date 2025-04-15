# 1) Estructuras condicionales: Requieren que el/la programador/a especifique una o más condiciones, con un bloque de instrucciones que se ejecutarán en caso de que la condición
# sea verdadera o falsa. Para ello haremos uso de:

# Estructura IF:
edad_primera_persona = 18 # Definimos la variable

if (edad_primera_persona >= 18): # Validamos que la edad sea mayor o igual a 18
    print("¡Felicitaiones! Puedes ingresar al boliche") # Mostramos esto por pantalla en caso de que la condición sea VERDADERA
  
# Estructura IF / ELSE:
edad_segunda_persona = 17
if (edad_segunda_persona >= 18):
     print("¡Felicitaiones! Puedes ingresar al boliche") # Mostramos esto por pantalla en caso de que la condición sea VERDADERA
else:
     print("¡Lo siento! No puedes ingresar")  # Mostramos esto por pantalla en caso de que la condición no sea VERDADERA

# Estructura IF / ELIF / ELSE:
edad_tercera_persona = 40
if (edad_tercera_persona > 50):
    print("¡Felicitaiones! Puedes ingresar al boliche a cualquier hora") # Mostramos esto por pantalla en caso de que la condición sea VERDADERA
elif (edad_tercera_persona > 35):
    print("¡Felicitaiones! Puedes ingresar al boliche a mitad de horario") # Mostramos esto por pantalla en caso de que la condición no sea VERDADERA y necesitamos volver a evaluar
else:
    print("¡Lo siento! No puedes ingresar")  # Mostramos esto por pantalla en caso de que la condición no sea VERDADERA

# IF anidados:
numero_uno = 513
numero_dos = 185
numero_tres = 712

if (numero_uno > numero_dos):
    if (numero_uno > numero_tres):
        print(f"El número {numero_uno} es mayor que {numero_dos} y {numero_tres}, por ende {numero_uno} es el más grande")
    else:
        print(f"El número {numero_uno} es mayor que {numero_dos} pero menor que {numero_tres}, por ende {numero_tres} es el mayor")
else:
    if (numero_dos > numero_tres):
        print(f"El numero {numero_dos} es mayor que {numero_uno} y {numero_tres}, por ende {numero_dos} es el mayor")
    else:
        print(f"El numero {numero_dos} es mayor que {numero_uno} pero menor que {numero_tres}, por ende {numero_tres} es el mayor")


# Declaración "MATCH": Permite que una variable se mida contra una lista de valores
marca_auto = "Volkswagen" # Definimos una variable y le asignamos un valor
match marca_auto: # Comparamos la variable para ver con cual hay match (coincide) y ejecutamos lo que está dentro de la opción (case) coincidente
    case "Volkswagen":
        print(f"Posees un auto de marca {marca_auto}, por ende, podemos realizarte un cambio de cubiertas.") # En este caso, esto se ejecutaría
        pass
    case "Ford":
        print(f"Posees un auto de marca {marca_auto}, por ende, no podemos brindarte ningún service. Disculpa")
        pass