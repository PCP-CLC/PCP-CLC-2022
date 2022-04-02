agno =  int(input("Ingresa un año: "))

es_bis = False

if agno % 400 == 0:
	es_bis = True
elif agno % 100 == 0 and not agno % 400 == 0:
	es_bis = False 
elif agno % 4 == 0 and not agno % 100 == 0 and not agno % 400 == 0:
	es_bis = True 

if es_bis:
	print("Ese año es bisiesto.")
else:
	print("Ese no es un año bisiesto.")