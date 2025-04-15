# Resolución Ejercicio Nº 9:
# Anagrama. Escribe una función que reciba dos palabras y retorne verdadero o falso según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existen.
# Dos palabras exactamente iguales no son anagrama.

def anagrama (paluno, paldos):
    
    paluno = paluno.lower()
    paldos = paldos.lower()

    if paluno == paldos:
        return False
    elif len(paluno) == len(paldos):
        if sorted(paluno) == sorted(paldos):
            return True
        else:
            return False
    else:
        return False
    
print(anagrama("Hola", "Aloh"))

# Resolución Ejercicio Nº 10:
# Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas, numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. 
# El alfil se desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una pieza puede ser capturada por otra si está en una casilla a la cual la otra puede desplazarse:
# Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de una torre, e indique cuál pieza captura a la otra:

tablero = [

    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 1
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 2
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 3
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 4
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 5
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 6
    [1, 2, 3, 4, 5, 6, 7, 8], # Fila 7
    [1, 2, 3, 4, 5, 6, 7, 8] # Fila 8
]

def quien_gana (alfil, torre):
    
   fila_alfil, col_alfil = alfil
   fila_torre, col_torre = torre

   if abs(fila_alfil - fila_torre) == abs(col_alfil - col_torre):
       return "Gana el alfil"

   if fila_alfil == fila_torre or col_alfil == col_torre:
       return "Gana la torre"
   
   return "Ninguna captura a la otra"


print(quien_gana((2, 4), (4, 3)))

# Resolución Ejercicio Nº 11:
# Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores deben elegir entre jugar tijera, papel o piedra. Las reglas para decidir quién gana la ronda son: 
# Tijera le gana a papel, papel le gana a piedra,
# Piedra le gana a tijera, y todas las demás combinaciones son empates.
# El ganador del juego es el primero que gane tres rondas.
# Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres rondas. Los jugadores deben 
# indicar su jugada escribiendo tijera, papel o piedra.

rondas_jugador_uno = 0
rondas_jugador_dos = 0

while (True):

    print(
        f"""
        El marcador de momento es:
        Jugador Nº 1: {rondas_jugador_uno} partidas ganadas
        Jugador Nº 2: {rondas_jugador_dos} partidas ganadas
        """
    )

    if rondas_jugador_uno >= 3:
        print(f'¡Felicitaciones! El Jugador Nº 1 ha sido el ganador. Saliendo del juego...')
        break
    elif rondas_jugador_dos >= 3:
        print(f'¡Felicitaciones! El Jugador Nº 2 ha sido el ganador. Saliendo del juego...')
        break

    pregunta_jugador_uno = input('Jugador Nº 1... ¿Cuál es tu jugada?\n')
    pregunta_jugador_uno = pregunta_jugador_uno.lower()
    pregunta_jugador_dos = input('Jugador Nº 2... ¿Cuál es tu jugada?\n')
    pregunta_jugador_dos = pregunta_jugador_dos.lower()

    print(f'La jugada del Jugador Nº 1 ha sido "{pregunta_jugador_uno}"...')
    print(f'La jugada del Jugador Nº 2 ha sido "{pregunta_jugador_dos}"...')

    if pregunta_jugador_uno != pregunta_jugador_dos:
        if pregunta_jugador_uno == "piedra" and pregunta_jugador_dos == "tijera":
            rondas_jugador_uno += 1
            print('Por ende, gana el Jugador Nº 1')

        if pregunta_jugador_uno == "tijera" and pregunta_jugador_dos == "papel":
            rondas_jugador_uno += 1
            print('Por ende, gana el Jugador Nº 1')
        
        if pregunta_jugador_uno == "papel" and pregunta_jugador_dos == "piedra":
            rondas_jugador_uno += 1
            print('Por ende, gana el Jugador Nº 1')

        if pregunta_jugador_dos == "piedra" and pregunta_jugador_uno == "tijera":
            rondas_jugador_dos += 1
            print('Por ende, gana el Jugador Nº 2')

        if pregunta_jugador_dos == "tijera" and pregunta_jugador_uno == "papel":
            rondas_jugador_dos += 1
            print('Por ende, gana el Jugador Nº 2')
        
        if pregunta_jugador_dos == "papel" and pregunta_jugador_uno == "piedra":
            rondas_jugador_dos += 1
            print('Por ende, gana el Jugador Nº 2')
    else:
        print('Empate, debido a que ambos jugadores eligieron la misma opción')

# Resolución Ejercicio Nº 12:
# Escriba un programa para simular un campeonato de tenis. Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
# debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El ganador de cada partido avanza a la ronda siguiente.
# El programa debe continuar preguntando ganadores de partidos hasta que quede un único jugador, que es el campeón del torneo.

print("Bienvenido al torneo de tenis. A continuación, te pediremos 8 nombres de tenistas")

tenistas = []

while (True):

    if len(tenistas) < 9:
        nombre_tenista = input("Ingresa el nombre del tenista:\n")
        tenistas.insert(nombre_tenista)
    else:
        break

print(tenistas)

# Resolución Ejercicio Nº 12:
# Escriba un programa para simular un campeonato de tenis. Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
# debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El ganador de cada partido avanza a la ronda siguiente.
# El programa debe continuar preguntando ganadores de partidos hasta que quede un único jugador, que es el campeón del torneo.

print("Bienvenido al torneo de tenis. A continuación, te pediremos 8 nombres de tenistas")

tenistas = []

while (True):

    if len(tenistas) < 8:
        nombre_tenista = input("Ingresa el nombre del tenista:\n")
        tenistas.append(nombre_tenista)
    else:
        break

ronda = 1

while len(tenistas) > 1:

    print(f'¡Atención! Ronda Nº {ronda}')
    ganadores = []

    for i in range(0, len(tenistas), 2):
        jugador1 = tenistas[i]
        jugador2 = tenistas[i + 1]
        print(f"Partido: {jugador1} vs {jugador2}\n")
    
    while (True):

        ganador = input("¿Quién fue el ganador de la ronda? Escriba el nombre\n")

        if ganador == jugador1 or jugador2:
            ganadores.append(ganador)
            break
        else:
            print("Error... Ingresaste un nombre no coincidente con el de los jugadores. Prueba nuevamente")
    
    tenistas = ganadores
    ronda += 1

print(f'El ganador del torneo fue "{tenistas[0]}"')

# Resolución Ejercicio Nº 13:
# El diccionario países asocia cada persona con el conjunto de los países que ha visitado:

paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

# Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han visitado la persona a y la persona b

def cuantos_en_comun(a,b):

    if a in paises and b in paises:
        paises_comunes = paises[a] & paises[b]
        print(f'"{a}" y "{b}" han visitado {len(paises_comunes)} en comun(es)')
    else:
        print("Los nombres ingresados no existen...")
        
cuantos_en_comun("Yayita", "John")

# Resolución Ejercicio Nº 14:
# El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una tupla

signos = {
    'aries': (( 3, 21), ( 4, 20)),
    'tauro': (( 4, 21), ( 5, 21)),
    'geminis': (( 5, 22), ( 6, 21)),
    'cancer': (( 6, 22), ( 7, 23)),
    'leo': (( 7, 24), ( 8, 23)),
    'virgo': (( 8, 24), ( 9, 23)),
    'libra': (( 9, 24), (10, 23)),
    'escorpio': ((10, 24), (11, 22)),
    'sagitario': ((11, 23), (12, 21)),
    'capricornio': ((12, 22), ( 1, 20)),
    'acuario': (( 1, 21), ( 2, 19)),
    'piscis': (( 2, 20), ( 3, 20)),
}

# Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de septiembre y el 23 de octubre. Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como 
# parámetro la fecha de nacimiento de una persona, representada como una tupla (año, mes, dia), y que retorne el signo zodiacal de la persona:

def determinar_signo(fecha_de_nacimiento):
    año, mes, dia = fecha_de_nacimiento
    nacimiento = (mes, dia)

    for signo, (inicio, fin) in signos.items():
        if inicio <= nacimiento <= fin:
            return signo
        if inicio > fin:
            if nacimiento >= inicio or nacimiento <= fin:
                return signo

    return "Fecha no válida"

signo = determinar_signo((2004, 9, 24))
print(f"Tu signo zodiacal es: {signo}")

# Resolución Ejercicio Nº 15:
# Este problema apareció en el certamen 2 del segundo semestre de 2011 en el campus Vitacura
libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
]

autores = {
    # autor: nacimiento, defunción, idioma
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español')
}

# Escriba las funciones necesarias para que el siguiente programa funcione:
# Función para obtener el idioma
def obtener_idioma(titulo):
    
    for libro in libros:
        if titulo == libro[0]:
            autor = libro[1]
            if autor in autores:
                idioma = autores[autor][2]
                print(f'El idioma es {idioma}')
                return
            
    print("El titulo no existe dentro de la colección de libros...")

# Función para obtener el autor
def obtener_autor(titulo):

    for libro in libros:
        if titulo == libro[0]:
            print(f'El autor del libro es "{libro[1]}"')
            return
        
    print("El titulo no existe dentro de la colección de libros...")

# Función para obtener los años antes de morir
def calcular_annos_antes_de_morir(titulo):

    for libro in libros:
        if titulo == libro[0]:
            autor = libro[1]
            if autor in autores:
                nacimiento = autores[autor][0][0]
                fallecimiento = autores[autor][1][0]
                edad = fallecimiento - nacimiento
                print(f'Su edad antes de fallecer fue de {edad} años')
                return
    
    print("El titulo no existe dentro de la colección de libros...")

titulo = input('Ingrese titulo del libro:\n')
obtener_idioma(titulo)
obtener_autor(titulo)
calcular_annos_antes_de_morir(titulo)

# Resolución Ejercico Nº 16:
# Código Morse. Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras " ".

diccionario_morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.', 'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',  'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',  'l': '.-..',
    'm': '--',    'n': '-.',    'ñ': '--.--','o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',  's': '...',
    't': '-',     'u': '..-',   'v': '...-', 'w': '.--',
    'x': '-..-',  'y': '-.--',  'z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.',
}

texto_comun = {v: k for k, v in diccionario_morse.items()}

def texto_a_morse(texto):
    resultado = []
    for palabra in texto.split():
        codigos = [diccionario_morse.get(c, '?') for c in palabra]
        resultado.append(' '.join(codigos))
    return '  '.join(resultado) 

def morse_a_texto(morse):
    resultado = []
    palabras = morse.split('  ')
    for palabra in palabras:
        letras = palabra.split()
        traducidas = [texto_comun.get(c, '?') for c in letras]
        resultado.append(''.join(traducidas))
    return ' '.join(resultado)

def es_morse(texto):
    return all(c in ".—- " for c in texto)

texto = input("Ingresa un texto para ser transformado a código morse o viceversa:\n").strip().lower()

if es_morse(texto):
    print("Código morse detectado... Cambiando a texto normal:")
    print(morse_a_texto(texto))
else:
    print("Texto normal detectado... Cambiando a código morse:")
    print(texto_a_morse(texto))