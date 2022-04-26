animales = "rana"

def estrofa(animal1, animal2):
    global animales #------------------por qué se usa global aquí? que pasaría si no estuviese? Invesitgue
    animales = animal1 + " a la " + animales
    print(f'La {animales}\n'
          f'Que estaba sentada cantando debajo del agua\n'
          f'Cuando la {animal1} salió a cantar\n'
          f'Vino la {animal2} y la hizo callar\n')
    animales = animal1 + " a la " + animales


print("Estaba la rana sentada\n"
        "Cantando debajo del agua\n"
        "Cuando la rana salió a cantar\n"
        "Vino la mosca y la hizo callar\n")

estrofa("mosca", "araña")
estrofa("araña", "rata")
estrofa("rata", "gata")
estrofa("gata", "perra")

