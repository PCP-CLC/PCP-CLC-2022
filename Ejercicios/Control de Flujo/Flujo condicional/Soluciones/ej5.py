s1 = float(input("Ingresa la medida del primer lado: "))
s2 = float(input("Ingresa la medida del segundo lado: "))
s3 = float(input("Ingresa la medida del tercer lado: "))

tipo = ""

if s1 == s2 == s3:
    tipo = "equilátero"
elif s1 == s2 or s1 == s3 or s2 == s3:
    tipo = "isósceles"
else:
    tipo = "escaleno"

print("Tu triángulo es {}.".format(tipo))


