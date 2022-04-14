# Código por Tomás Fuenzalida

from math import sqrt

a = int(input("ingrese el valor de a\n"))
b = int(input("ingrese el valor de b\n"))
c = int(input("ingrese el valor de c\n"))
discr1 = ((b**2)-(4*a*c))
if a == 0:
    print("Los coeficientes no corresponden a una ecuacion cuadratica")
elif discr1 < 0:
    print("no tiene raices en los reales")
elif discr1 == 0:
    print("La solucion es", str(-b/2*a))
elif discr1 > 0:
    print("Los valores ingresados corresponden a una ecuacion cuadratica cuyas raices son:",
          str((-b+sqrt(discr1))/2*a), "y", str((-b-sqrt(discr1))/2*a))
