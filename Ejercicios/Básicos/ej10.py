# El siguiente programa contiene una función, pero, aún no sabemos lo que son :O
# Gran parte de lo que estudiaremos en clases y lo que harás en los laboratorios se integra dentro de funciones
# Lo que debemos saber de momento es:

# def funcion(a,b):
#   c=a+b
#   return c

"""
Mira la función de arriba (lineas 5,6 y7). En la primera línea lo más importante son los términos entre paréntesis.
Estos son los parámetros de la función, y son los valores que necesitamos para realizar las operaciones
que debe hacer nuestra función. Si, por ejemplo, queremos saludar a alguien,
el parámetro que necesitará la función será el nombre de la persona a saludar.
O, si queremos sumar dos números (como en el código de arriba), los parámetros serán los sumandos.
En el cuerpo de la función pondremos las operaciones que debemos realizar para obtener el resultado buscado.
Y una vez que tengamos en una variable el valor que nos piden, debemos retornarlo.
Esto es lo que hacemos para devolver el valor solicitado. Es decir,
si nos piden una función que sume dos números, tendremos que retornar la suma de los dos sumandos.
Siendo los parámetros a y b, esto puede hacerse de dos maneras equivalentes: c = a + b y después return c,
o bien directamente return a + b.
"""

# Completa el cuerpo de la función tunombre para que retorne el nombre completo de una persona.
# Los parámetros que recibe esta función son n y a. n hace referencia al nombre y a al apellido.

nombre = input("Ingresa tu primer nombre:")
apellido = input("Ingresa tu apellido:")

def tunombre (n, a):
    nombreCompleto = ""

    return nombreCompleto

print("Tu nombre es:",tunombre(nombre,apellido))