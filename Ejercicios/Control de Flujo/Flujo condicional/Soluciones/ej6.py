agno = int(input("Ingrsa un año d.C: "))

if agno < 2000 or agno > 2011:
    while agno < 2000:
        agno += 12
    while agno > 2011:
        agno -= 12

if agno == 2000:
    signo = "Dragón"
elif agno == 2001:
    signo = "Serpiente"
elif agno == 2002:
    signo = "Caballo"
elif agno == 2003:
    signo = "Oveja"
elif agno == 2004:
    signo = "Mono"
elif agno == 2005:
    signo = "Gallo"
elif agno == 2006:
    signo = "Perro"
elif agno == 2007:
    signo = "Cerdo"
elif agno == 2008:
    signo = "RRata"
elif agno == 2009:
    signo = "Buey"
elif agno == 2010:
    signo = "Tigre"
elif agno == 2011:
    signo = "Liebre"

print("Eres un {}!".format(signo))
