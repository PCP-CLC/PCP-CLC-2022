suma = 0
n = 0
colección = ""

interrumpido = False
while not interrumpido:
    val = float(input("Ingrese un valor (0 para salir): "))
    if val != 0:
        suma += val
        n += 1
        colección = str(val) + ", " + colección
    else:
        interrumpido = True

prom = suma / n
print(f'El promedio entre {colección[:-2]} es:\n{prom}') #Invesigue sobre los f'strings #Investigue que le hace [:-1] a un string