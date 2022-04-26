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


input_valido(input("Ingrese un número entero positivo"))
