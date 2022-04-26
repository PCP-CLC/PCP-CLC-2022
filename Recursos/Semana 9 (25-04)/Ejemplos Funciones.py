

def obtenerdigito(num, posicion):
    digito = num//10**(posicion)%10
    return digito

def capicua(num):
    if obtenerdigito(num,0) == obtenerdigito(num, 3) and obtenerdigito(num,1) == obtenerdigito(num,2):
        print(f'{num} es capicua')
    else:
        print(f'{num} NO es capicua')
    return

capicua(int(input("Ingrese un numero de 4 cifras: ")))