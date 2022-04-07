# Elif
#------------------------------------------------

# Ejemplo 0
# A veces nos encontraremos con situaciones
# que involucran más de una condición para la
# toma de decisiones.
#
# llueve = True
# temperatura = int(input("Ingresa la temperatura: \n"))
# if temperatura < 18:
#     if llueve:
#         print("Llevaré paraguas y abrigo")
#     else:
#         print("Solo llevaré abrigo")
# else:
#     print("No necesito paraguas ni abrigo")


#------------------------------------------------

# Ejemplo 1

# Si aumentamos la cantidad de condiciones
# Seguramente tendremos muchos if anillados
# Y esto puede ser poco práctico o legible.

llueve = True
temperatura = int(input("Ingresa la temperatura: \n"))
if temperatura < 18 and llueve:
    print("Llevaré paraguas y abrigo")
elif temperatura < 18 and not llueve:
    print("Solo llevaré abrigo")
else:
    print("No necesito paraguas ni abrigo")

# Además, es importante que reordenemos las condiciones
# comenzando con la más sencilla o la que
# excluya más casos, de esta manera nuestro
# programa se ejecutará más rápido