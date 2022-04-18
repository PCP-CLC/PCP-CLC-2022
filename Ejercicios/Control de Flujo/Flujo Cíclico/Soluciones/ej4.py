print("Este programa dibujará un rombo")
ancho = int(input("Ingrese el ancho del rombo (debe ser impar): "))

if ancho % 2 == 1:
    sup = ""
    inf = ""
    for i in range(ancho):
        if i <= ancho//2:
            inf = (" "*(ancho//2 - i + 1) + "*"*(2*i-1) + "\n") + inf
            sup = sup + (" "*(ancho//2 - i + 1) + "*"*(2*i-1) + "\n")
    print(sup + "*" * ancho + "\n" + inf)
else:
    print("Ingresaste un número par, no se como dibujarlo")



