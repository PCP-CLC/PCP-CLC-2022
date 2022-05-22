s = input("Ingrese una frase")

i = 0
nPalabras = 0
palabra = ""

while i<len(s):
    if (s[i] != ' '):
        palabra += s[i]
    else:
        nPalabras += 1
        print(str(nPalabras) + ".", palabra)
        palabra = ""
    i += 1

nPalabras += 1
print(str(nPalabras) + ".", palabra)
