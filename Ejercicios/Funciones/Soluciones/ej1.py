print("Este porgrama calculará el Máximo común divisor entre los números que usted ingrese")
n = int(input("Ingrese un número entero positivo:\n"))
m = int(input("Ingrese otro número entero positivo:\n"))


def mcd(num1, num2):
    d = min(num1, num2)
    while num1 % d != 0 or num2 % d != 0:
        d -= 1
    return d


print(f'El Máximo común divisor entre {n} y {m} es {mcd(m,n)}')
