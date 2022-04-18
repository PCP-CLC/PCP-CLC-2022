mensaje = input("Ingrese un mensaje: ")
salto = 3
nuevo_mensaje = ""

for l in mensaje:
    if l >= "a" and l <= "z":
        pos = ord(l) - ord("a")
        pos = (pos + salto) % 26
        nueva_l = chr(pos + ord("a"))
        nuevo_mensaje = nuevo_mensaje + nueva_l
    elif l >= "A" and l <= "Z":
        pos = ord(l) - ord("A")
        pos = (pos + salto) % 26
        nueva_l = chr(pos + ord("A"))
        nuevo_mensaje = nuevo_mensaje + nueva_l
    else:
        nuevo_mensaje = nuevo_mensaje + l

print(f'El mensaje codificado es: {nuevo_mensaje}')