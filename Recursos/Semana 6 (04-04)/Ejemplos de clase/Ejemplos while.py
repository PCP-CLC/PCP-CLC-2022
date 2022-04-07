# While
#------------------------------------------------

# Ejemplo 0
# Revisemos la estructura del cíclico while
from time import sleep

# cuenta = 10
# while cuenta > 0:
#     print(cuenta)
#     cuenta -= 1
#     sleep(1)
# print("Despegue!")





#------------------------------------------------

# Ejemplo 1
# Modifiquemos el ejemplo anterior para que el mensaje
# de despegue ocurra dentro del while
#
# cuenta = 10
# while cuenta > 0:
#     print(cuenta)
#     cuenta -= 1
#     if cuenta == 0:
#         print("Despegue!")


#------------------------------------------------

# Ejemplo 2
# break

# cuenta = 10
# while True:                     # Nuestra condición es siempre verdadera.
#     print(cuenta)
#     cuenta -= 1
#     if cuenta == 0:
#         print("Despegue!")
#         break                   # while será un ciclo infinito a menos que
#                                 # se tope con un break.


#---------------------------------

#Jueguemos pipati

from random import randint

puntaje_jugador = 0
puntaje_pc = 0

while puntaje_pc < 3 != puntaje_jugador < 3:
    jugada = int(input("Elige: 1.-Piedra, 2.-Papel o 3.-Tijera"))
    jugada_pc = randint(1, 3)

    if jugada == jugada_pc:
        print("Empate")
    elif jugada == 1 and jugada_pc == 2:
        puntaje_pc += 1
        print("Pierdes")
    elif jugada == 1 and jugada_pc == 3:
        puntaje_jugador += 1
        print("Ganas")
    elif jugada == 2 and jugada_pc == 1:
        puntaje_jugador += 1
        print("Ganas")
    elif jugada == 3 and jugada_pc == 1:
        puntaje_pc += 1
        print("Pierdes")
    elif jugada == 2 and jugada_pc == 3:
        puntaje_pc += 1
        print("Pierdes")
    elif jugada == 3 and jugada_pc == 2:
        puntaje_jugador += 1
        print("Ganas")



if puntaje_jugador == 3:
    print("Ganaste la partida")
elif puntaje_pc == 3:
    print("Game over")

