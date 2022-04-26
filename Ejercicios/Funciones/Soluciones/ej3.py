def input_valido(dato):
    while True:
        try:  #---------------------------------------------------------- Investigue la instrucción try/except
            dato = float(dato)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número")
            dato = input("Ingrese un entero positivo: ")
            continue
        if dato <= 0:
            print("Su número no es positivo. No se acepta")
            dato = input("Ingrese un entero positivo: ")
            continue
        elif dato != int(dato):
            print("Su número es decimal. No se acepta")
            dato = input("Ingrese un entero positivo: ")
            continue
        else:
            dato = int(dato)
            break

    return dato


def mcd(num1, num2):
    num1 = input_valido(num1)
    num2 = input_valido(num2)
    d = min(num1, num2)
    while num1 % d != 0 or num2 % d != 0:
        d -= 1
    return d




print("Este programa calculará el máximo común divisor entre los números que usted ingrese")

n = input_valido(input("Ingrese un número entero positivo: \n"))
m = input_valido(input("Ingrese otro número entero positivo: \n"))

print(f'El máximo común divisor entre {n} y {m} es {mcd(n,m)}')