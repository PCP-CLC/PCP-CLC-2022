import random

respuesta = random.randint(0, 100)

while True:
    usuario = int(input('En que número estoy pensando? '))

    if usuario == respuesta:
        print(f'Adivinaste!  El número era {usuario}') # Investigar f strings
        break

    if usuario < respuesta:
        print('El número que estoy pensando es mayor')

    else:
        print('El número que estoy pensando es menor')