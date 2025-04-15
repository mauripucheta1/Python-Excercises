# 1) Excepciones: Permite básicamente realizar un manejo de errores, por ejemplo:

# Primer ejemplo: Manejamos un error en caso de que querramos dividir por 0
try: 
    numerador = 5 # Definimos un numerador
    denominador = 0 # Definimos el denominador
    resultado = numerador / denominador # Establecemos la operación aritmética, en este caso, la división
except ZeroDivisionError:
    print("Error: No es posible dividir por 0") # Manejamos el bloque "except" en caso de producirse un error, mostrando por pantalla el error
else:
    print(f"El resultado de dividir {numerador} por {denominador} da como resultado: {resultado}.") # En caso de no producirse error, mostramos esto por pantalla
finally:
    print("Ejecución finalizada. Saliendo...") # Bloque de ejecución final

# Segundo ejemplo: Manejamos un error en caso de que querramos abrir un archivo, pero con más bloques "except"

try:
    archivo = open('archivo_no_existente.txt', 'r')
    contenido = archivo.read()
    numero = int(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")
except ValueError:
    print("Error: El contenido del archivo no es un número válido.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print(f"El número es {numero}")
finally:
    if 'archivo' in locals():
        archivo.close()
    print("Operación de archivo completada.")


# 2) Manejo de excepciones: Lo acabamos de ver con dos ejemplos
# 3) Lanzar excepciones: Python nos permite lanzar excepciones con mensajes utilizando la palabra raise.
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser mayor o igual a 18.")
        return "Edad válida"

try:
    resultado = verificar_edad(16)
    print(resultado)
except ValueError as e:
    print(f"Error: {e}")