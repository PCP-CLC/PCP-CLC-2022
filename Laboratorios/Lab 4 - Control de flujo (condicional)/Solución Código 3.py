# Código por Trinidad Borgoño

print("Bienvenido al Banco La Cruz!")
print("Ingrese los siguientes datos para adquirir un credito:")
i= int(input("Ingreso mensual en pesos: $"))
n= int(input("Año de nacimiento:"))
h= int(input("Cantidad de hijos:"))
c= int(input("Cantidad de años que lleva con nosotros:"))
e= input("Estado civil (casado/soltero):")
v= input("Vive en la ciudad o campo:")
d= 2022-n
if (c>10 and h>=2) or (e=="casado" and h>3 and 45<d and d<55) or (i>2500000 and e=="soltero" and v=="cuidad") or (i>3500000 and c>5) or (v=="campo" and e=="casado" and h<2):
    print("Tu crédito a sido APROBADO")
else:
    print("Tu crédito a sido RECHAZADO")

