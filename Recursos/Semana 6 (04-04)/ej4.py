# El siguiente código pide un número al usuario y lo clasifica según su valor del siguiente modo:
#  0 <= x <= 20 --- bajo
#  20 < x <= 40 --- medio bajo
#  40 < x <= 60 --- medio
#  60 < x <= 80 --- medio alto
#  80 < x <= 100 --- alto
#  100 < x --- Inválido
#  x < 0 --- Inválido

# Complete el programa para que se cumpla lo anterior

num = input("Ingrese un número: ")
if 0 <= num <= 100:
    if num <= 20:
        print("bajo")
    else:
        if num <= 40:
            print("medio bajo")

else:
    print("El número ingresado no es válido.")