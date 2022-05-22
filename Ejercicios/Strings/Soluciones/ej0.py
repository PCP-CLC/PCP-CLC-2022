s = input("Ingrese una palabra\n")
i = 0
cuentaA = 0
while i<len(s):
    if (s[i] == 'a' or s[i] == 'A' or s[i] == 'á' or s[i] == 'Á'):
        cuentaA += 1
    i += 1
print("Hay", cuentaA, "letras 'a' en", s)
