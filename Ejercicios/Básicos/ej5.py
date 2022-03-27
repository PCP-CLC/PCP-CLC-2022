# Intente responder a cada pregunta antes de correr el código.
# Corra el código para verificar si sus supuestos son correctos.

valint = 123134
valdouble = 123.23
valstring_double = "2342.23"
valstring_int = "2342"

print(valstring_double * 3) # ¿qué se imprime aquí?, ¿de qué tipo es el valor impreso?
print(float(valstring_double) * 3) # ¿y aquí?

print(valstring_int * 3) # ¿y aquí?
print(float(valstring_int) * 3) # ¿y aquí?

print(str(valint) + " es mucho mayor que " + str(valdouble)) # ¿y aquí?

# Lo anterior tambien se podria imprimir asi:
print(valint, "es mucho mayor que", valdouble)

