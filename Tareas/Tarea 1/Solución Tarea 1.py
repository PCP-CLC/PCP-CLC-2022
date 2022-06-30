# Solución por Clemente Witting

import tableroGUI
import random

tablero = None
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1 = (0,)*16
puntaje = 0

def comparar():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    global a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1
    a1 = a
    b1 = b
    c1 = c
    d1 = d
    e1 = e
    f1 = f
    g1 = g
    h1 = h
    i1 = i
    j1 = j
    k1 = k
    l1 = l
    m1 = m
    n1 = n
    o1 = o
    p1 = p

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

    iniciar_juego()
    actualizar_tablero()
    while True:
        comparar()
        jugada()
        n_random()
        actualizar_tablero()

def jugada():
    tecla = esperar_presionar_tecla()
    if tecla == "abajo":
        abajo()
        actualizar_tablero()
    if tecla == "arriba":
        arriba()
        actualizar_tablero()
    if tecla == "derecha":
        derecha()
        actualizar_tablero()
    if tecla == "izquierda":
        izquierda()
        actualizar_tablero()

def suma_total(c1, c2, c3, c4):
    global puntaje
    if c4 == c1 and c3 == 0 and c2 == 0:
        if c4 == c1:
            puntaje += c4 + c1
        c4 += c1
        c1 = 0
    if c3 == c1 and c2 == 0:
        if c3 == c1:
            puntaje += c3 + c1
        c3 += c1
        c1 = 0
    if c3 == 0 and c4 == 0:
        c4 = c2
        c3 = c1
        c1 = 0
        c2 = 0
    if c4 == c2 and c3 == 0 or c4 == 0 and c3 == 0 and c2 != 0:
        if c4 == c2:
            puntaje += c4 + c2
        c4 += c2
        c3 = c1
        c2 = 0
    if c2 == c3 and c4 == 0:
        if c2 == c3:
            puntaje += c2 + c3
        c4 = c2 + c3
        c3 = c1
        c2 = 0
        c1 = 0
    if c4 == c3 or c4 == 0 or c3 == 0:
        if c3 == c4:
            puntaje += c3 + c4
        c4 += c3
        c3 = c2
        c2 = c1
        c1 = 0
    if c3 == c2 or c2 == 0 or c3 == 0:
        if c2 == c3:
            puntaje += c3 + c2
        c3 += c2
        c2 = c1
        c1 = 0
    if c2 == c1 or c2 == 0:
        if c2 == c1:
            puntaje += c1 + c2
        c2 += c1
        c1 = 0
    return c1, c2, c3, c4

def abajo():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    a, e, i, m = suma_total(a, e, i, m)
    b, f, j, n = suma_total(b, f, j, n)
    c, g, k, o = suma_total(c, g, k, o)
    d, h, l, p = suma_total(d, h, l, p)

def arriba():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    m, i, e, a = suma_total(m, i, e, a)
    n, j, f, b = suma_total(n, j, f, b)
    o, k, g, c = suma_total(o, k, g, c)
    p, l, h, d = suma_total(p, l, h, d)

def derecha():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    a, b, c, d = suma_total(a, b, c, d)
    e, f, g, h = suma_total(e, f, g, h)
    i, j, k, l = suma_total(i, j, k, l)
    m, n, o, p = suma_total(m, n, o, p)

def izquierda():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    d, c, b, a = suma_total(d, c, b, a)
    h, g, f, e = suma_total(h, g, f, e)
    l, k, j, i = suma_total(l, k, j, i)
    p, o, n, m = suma_total(p, o, n, m)

def n_random():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    global a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1
    torrealba = 1
    if a != a1 or b != b1 or c != c1 or d != d1 or e != e1 or f != f1 or g != g1 or h != h1 or i != i1 or j != j1 or k != k1 or l != l1 or m != m1 or n != n1 or o != o1 or p != p1:
        if a == 0 or b == 0 or c == 0 or d == 0 or e == 0 or f == 0 or g == 0 or h == 0 or i == 0 or j == 0 or k == 0 or l == 0 or m == 0 or n == 0 or o == 0 or p == 0:
            while torrealba == 1:
                witting = random.randint(1, 16)
                if witting == 1 and a == 0:
                    a = 2
                    torrealba = 0
                elif witting == 2 and b == 0:
                    b = 2
                    torrealba = 0
                elif witting == 3 and c == 0:
                    c = 2
                    torrealba = 0
                elif witting == 4 and d == 0:
                    d = 2
                    torrealba = 0
                elif witting == 5 and e == 0:
                    e = 2
                    torrealba = 0
                elif witting == 6 and f == 0:
                    f = 2
                    torrealba = 0
                elif witting == 7 and g == 0:
                    g = 2
                    torrealba = 0
                elif witting == 8 and h == 0:
                    h = 2
                    torrealba = 0
                elif witting == 9 and i == 0:
                    i = 2
                    torrealba = 0
                elif witting == 10 and j == 0:
                    j = 2
                    torrealba = 0
                elif witting == 11 and k == 0:
                    k = 2
                    torrealba = 0
                elif witting == 12 and l == 0:
                    l = 2
                    torrealba = 0
                elif witting == 13 and m == 0:
                    m = 2
                    torrealba = 0
                elif witting == 14 and n == 0:
                    n = 2
                    torrealba = 0
                elif witting == 15 and o == 0:
                    o = 2
                    torrealba = 0
                elif witting == 16 and p == 0:
                    p = 2
                    torrealba = 0


    #Aqui termina tu tarea

tablero = tableroGUI.Application("tarea")
tablero.title('2048 - PCP CLC 2022')
tablero.loadProgram(tarea)
tablero.start()
