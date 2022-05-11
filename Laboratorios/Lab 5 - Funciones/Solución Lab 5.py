#Código por Macarena Carvajal

from random import randint
numero = int(input('Denme un numero impar mayor o igual a 5:\n'))

deco = randint(1, 10)

def adornos (cosas):
    deco = randint(1, 10)
    if deco == 1:
        deco = '$'
    elif deco == 2:
        deco ='@'
    elif deco == 3:
        deco = '0'
    elif deco == 4:
        deco = '#'
    else:
        deco = '*'
    return deco


def dibujar_arbol(ancho):
    while ancho < 9 or ancho % 2 == 0:
        print('No puedo dibujar este arbol')
        print('No puedo dibujar este arbol, aquí tienes uno de ancho 9')
        dibujar_arbol(9)
        ancho = int(input('Denme un numero impar mayor o igual a 9:\n'))
    print(' ' * (ancho // 2), '*')
    espacio = ancho // 2
    m = 1
    for arbol in range(3, ancho + 1, 2):
        linea = ''
        m += 2
        arbol -= 1
        for final in range(m):
            linea = linea + adornos(deco)
        print((' ' * espacio) + linea)
        espacio -= 1
    print(ancho // 2 * ' ' + 'III')
    print(ancho // 2 * ' ' + 'III')
    return


dibujar_arbol(numero)

#confeccionar linea x linea

#Muy bueno!
