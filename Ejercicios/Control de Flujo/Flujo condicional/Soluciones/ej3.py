a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

if a > b:
    aux = a
    a = b
    b = aux
if a > c:
    aux = a
    a = c
    c = aux
if b > c:
    aux = b
    b = c
    c = aux

print(a,b,c)