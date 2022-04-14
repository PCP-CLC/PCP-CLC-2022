# Código por Matías Alfaro

print('Bienvenido a tu simulador de cajero automatico online favorito :D')
monto = int(input('Ingrese dinero a retirar: '))
var20 = 0
var10 = 0
var5 = 0
var2 = 0
var1 = 0

while monto >= 20000:
    monto -= 20000
    var20 += 1
while monto >= 10000 and monto < 20000:
    monto -= 10000
    var10 += 1
while monto >= 5000 and monto < 10000:
    monto -= 5000
    var5 += 1
while monto >= 2000 and monto < 5000:
    monto -= 2000
    var2 += 1
while monto >= 1000 and monto < 2000:
    monto -= 1000
    var1 += 1
print('--------------------------------')

print(var20, 'de 20.000')
print(var10, 'de 10.000')
print(var5,  'de 5.000')
print(var2,  'de 2.000')
print(var1,  'de 1.000')
