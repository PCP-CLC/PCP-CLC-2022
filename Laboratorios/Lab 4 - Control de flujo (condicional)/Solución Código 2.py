# Código por Vicente Celedon

numero = int(input("Ingrese número de 4 dígitos: "))

if numero > 9999 or numero < 1000:
    print("El número ingresado no tiene 4 dígitos. ")
else:
    digito4 = numero // 1000
    digito3 = (numero - (digito4 * 1000))//100
    digito2 = (numero - (digito4 * 1000) - (digito3 * 100))//10
    digito1 = (numero - (digito4 * 1000) - (digito3 * 100) - (digito2 * 10 ))
    if digito1 == digito4 and digito2 == digito3 :
        print("El número",numero," es un número capicúa y de cuatro dígitos!")
    else:
        print("El número ingresado tiene cuatro dígitos, pero no es capicúa. ")