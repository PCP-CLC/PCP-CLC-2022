mes = input("Ingresa el nombre de un mes: ").lower()

if mes == "septiembre" or mes == "abril" or mes == "junio" or mes == "noviembre":
	print("{} tiene 30 días." .format(mes))
elif mes == "febrero":
	print("febrero puede tener 28 o 29 días.")
else:
	print("{} tiene 31 días." .format(mes))