s = input("Ingrese una frase\n")
i = 0
nPalabras = 0
while i<len(s):
    if (s[i] == ' '):
        nPalabras += 1
    i += 1
nPalabras += 1
print("Hay " + str(nPalabras) + " palabras en \"" + s + "\"")
