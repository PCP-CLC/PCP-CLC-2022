def cuentapalabras(frase):
    i = 0
    nPalabras = 0
    while i < len(s):
        if (frase[i] == ' '):
            nPalabras += 1
        i += 1
    nPalabras += 1
    return nPalabras

s = input("Ingrese una frase\n")
print(f'La frase {s} tiene {cuentapalabras(s)} palabras')


