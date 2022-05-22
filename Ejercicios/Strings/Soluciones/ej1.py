def cuentaletras(palabra, letra):
    cuenta = 0
    for i in range(len(palabra)):
        if (palabra[i] == str(letra)):
            cuenta += 1
    return cuenta

p = input("Ingrese una palabra\n")
l = input("Ingrese una letra\n")
print(f'La letra "{l}" aparece {cuentaletras(p,l)} veces en la palabra {p}')