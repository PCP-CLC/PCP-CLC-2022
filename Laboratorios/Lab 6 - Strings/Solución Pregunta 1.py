# Solución por Ema Buttazzoni

def decodificador (mensaje):
    mendeco = ""
    for x in mensaje:
        if x == "_":
            mendeco += " "
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if x == i:
                mendeco += i

    return mendeco

