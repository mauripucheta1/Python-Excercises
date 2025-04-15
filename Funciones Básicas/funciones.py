# 1) Definición de funciones: 

def saludar(nombre): # Definimos una función por su nombre y le decimos que obtendrá un parametro únicamente, en este caso, "nombre"
    print(f"¡Hola {nombre}! Un gusto verte nuevamente...") # Establecemos el cuerpo de la función, que queremos que haga la función

def multiplicador_por_dos(numero): # Definimos una función por su nombre y le decimos que obtendrá un parametro únicamente, en este caso, "numero"
    return numero * 2 # Establecemos el cuerpo de la función, que queremos que haga la función

# Invocación de la función: Una vez definida, podemos llamarla pero ¡Ojo!
saludar("Mauricio") # La llamamos por su nombre y dentro de los paréntesis especificamos los argumentos que tomará la función para trabajar, en este caso "Mauricio"

# Invocación de la función: Una vez definida, podemos llamarla pero ¡Ojo! Estamos trabajando con un "return", asique debemos recuperar ese return justamente (obtenerlo) y mostrarlo por pantalla
print(multiplicador_por_dos(10)) # La llamamos por su nombre y dentro de los paréntesis especificamos los argumentos que tomará la función para trabajar, en este caso "Mauricio"