# Módulos:

Un módulo es un archivo que contiene el código Python. El nombre del archivo, es el nombre del módulo. Por ejemplo, el módulo: "math.py"
Para hacer uso de las funciones contenidas dentro de ese módulo podemos importarlas de distintas maneras, tales como:

1) # Importación de una función específica contenida en un módulo:
    Ejemplo: from math import sqrt

2) # Importación de varias funciones específicas contenidas en un módulo
    Ejemplo: from math import sqrt, log10, cos

3) # Importación de todas las funciones contenidas en el módulo
    Ejemplo: import math

En resumen, la programación modular es una técnica que se utiliza en el desarrollo de software para dividir un programa en módulos pequeños, autónomos y lógicos. Cada módulo
resuelve un problema específico y contiene todo lo necesario para cumplir con su funcionalidad. Además un módulo se puede modificar radicalmente sin afectar otros módulos, incluso sin 
alterar su función principal.

Usar if __name__ == "__main__" es una buena práctica cuando:
* Querés que tu script pueda ejecutarse directamente y también ser importado como módulo sin que se ejecute todo automáticamente
* Estás trabajando en un proyecto más grande y modular
* Querés mantener tu código más organizado y mantenible

En programación modular (y en buenas prácticas en general), no se espera que haya lógica "suelta" en los módulos. Todo debería estar dentro de funciones, clases o bloques protegidos 
con if __name__ == "__main__", según el propósito del módulo.

# ¿Por qué evitar lógica suelta?
* Reusabilidad: Al encapsular todo en funciones, podés importar ese módulo en otros archivos sin que se ejecute nada automáticamente (a menos que lo llames explícitamente).
* Evitar efectos secundarios: Si tenés código suelto (por ejemplo, inputs o prints), ese código se ejecutará automáticamente cuando importes el módulo. Eso puede ser confuso 
y causar errores inesperados.
* Organización y claridad: Facilita el mantenimiento del código, el testeo unitario, y la lectura.

# Funciones Lambda:
En Python las funciones lambda (o funciones anónimas) se definen sin un nombre explícito. Las mismas se usan comúnmente en operaciones como:
* map(): Para transformar elementos
* filter(): Para filtrar elementos
* sorted(): Para ordenar por criterios personalizados

# ¿Cuándo usar lambda?
1) Cuando necesitás una función pequeña, rápida y de una sola línea
2) Cuando no vas a reutilizar esa función en otras partes del código
3) No se recomienda cuando la lógica es compleja (ahí conviene usar def con nombre)

# Funciones con argumentos por omisión:
Las funciones con argumentos por omisión permiten especificar argumentos con valores predeterminados y se utilizan si no se proporciona una valor específico.
Ejemplo: def sumar (a = 2) 
En ese ejemplo, estamos diciendo que si no se proporciona el valor para "a", el predeterminado será 2

# Funciones con argumentos por palabra clave:
Las funciones con argumentos con palabras clave son funciones dónde los argumentos se identifican por su nombre y permiten pasar valores en cualquier orden.

# Funciones con argumentos especiales:
Un programador con sólo mirar la definición de la función podrá determinar si los mismos deben pasarse por posición o por palabra clave. Para ello, se utilizan los símbolos / y * 
en la definición de la función como sigue Los parámetros especiales en Python se refieren a formas avanzadas de manejo de argumentos en las funciones. Existen principalmente tres tipos de parámetros especiales:
1) *args: Permite recibir un número variable de argumentos posicionales.
2) **kwargs: Permite recibir un número variable de argumentos por palabra clave.
3) * (cuando se usa solo como un parámetro): Usado para indicar que los argumentos a partir de este punto deben ser pasados por palabra clave, y no por posición.
4) /: Indica que los parámetros anteriores deben ser pasados solo por posición, no por palabra clave.