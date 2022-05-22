def buscar_c(s, c):
    i = 0
    while i < len(s):
        if s[i] == c:
            return i
        i += 1
    return -1

s = "Hola, ¿qué tal?"
print(s)

#usando función buscar_c()

c = ','
pos = buscar_c(s, c)
print("'" + c + "' está en la posición " + str(pos))

c = 'z'
pos = buscar_c(s, c)
print("'" + c + "' está en la posición " + str(pos))


#usando método find()

c = ','
pos = s.find(c)
print("'" + c + "' está en la posición " + str(pos))

c = 'z'
pos = s.find(c)
print("'" + c + "' está en la posición " + str(pos))
