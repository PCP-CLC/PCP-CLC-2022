# While
#------------------------------------------------

# Ejemplo 0

# Recordemos el programa de cuenta regresiva
# que hicimos utilizando while.
#
# Cuando queremos implementar ciclos, pero la
# cantidad de repeticiones es conocida, usaremos
# for

from time import sleep

cuenta = 10
while cuenta > 0:
    print(cuenta)
    cuenta -= 1
    sleep(1)
print("Despegue!")
#
# for cuenta in range(10): # estamos creando una variable "cuenta" que iterará tomando los valores desde 0 hasta 9
#     print(10-cuenta)
#     sleep(1)
# print("Despegue!")

# Usando for la variable se inicializa
# e incrementa en la instrucción for
# por tanto nos ahorramos inicializar la
# variable y cambiar sus valores

# el comando range(fin) crea una secuencia
# de números que parte desde 0 y termina
# en fin-1

# También podemos escribir range(inicio, fin)
# en este caso se creará una secuencia que parte
# en inicio y termina en fin-1, por ejemplo
# range(8,14) crea la secuencia 8,9,10,11,12,13.

# Por último, si range recibe 3 parámetros
# range(inicio, fin, paso) se creará una secuencia
# que parte en inicio, termina en fin-1 y avanza de
# 3 en 3, por ejemplo
# range(8, 18, 3) creará la secuencia 8,11,14,17.

# De momento solo recorreremos secuencias con range,
# sin embargo, es posible recorrer strings y listas.
# Esto lo veremos más adelante.

#------------------------------------------------

# Ejemplo 1

# Así como podemos anillar if y while, también
# podemos anillar for

# for i in range(1, 100):
#     for j in range(1, 100):
#         print(i, j)

