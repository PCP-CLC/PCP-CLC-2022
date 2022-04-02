nLados = int(input("Ingresa la cantidad de lados de tu figura: "))

if nLados == 3:
	print("Eso es un triángulo.")
elif nLados == 4:
	print("Eso es un cuadrado.")
elif nLados == 5:
	print("Eso es un pentágono.")
elif nLados == 6:
	print("Eso es un hexágono.")
elif nLados == 7:
	print("Eso es un heptágono.")
elif nLados == 8:
	print("Eso es un octágono.")
elif nLados == 9:
	print("Eso es un eneágono.")
elif nLados == 10:
	print("Eso es un decágono.")
else:
	print("Ingresa una cantidad que 2 y menor que 11")