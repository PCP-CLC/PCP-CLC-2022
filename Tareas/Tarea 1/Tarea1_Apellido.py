import tableroGUI
import random

tablero = None 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
puntaje = 0


def iniciar_juego():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = tablero.inicia_juego()


def actualizar_tablero():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    tablero.update(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, puntaje)


def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()  


def tarea(tablero):
    global puntaje, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    #Aqui empieza tu tarea



    #Aqui termina tu tarea

tablero = tableroGUI.Application("tarea")
tablero.title('2048 - PCP CLC 2022')
tablero.loadProgram(tarea)
tablero.start()
