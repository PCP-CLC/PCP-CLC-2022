a_humano = int(input("Ingresa la edad de tu perro en años humanos: "))

if a_humano <= 2:
    a_perro = a_humano * 10.5
elif a_humano > 2:
    a_perro = 2 * 10.5
    a_perro += (a_humano - 2) * 4

if a_humano < 0:
    print("Ingresa un número positivo.")
else:
    print("Tu perro tiene %a años en años de perro." %(a_perro))