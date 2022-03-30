#A lo largo del curso realizaremos una pequeña red social.
#Para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#escribiendo el nombre de la red.

#A continuación preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta información en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Examina el código, lee los comentarios e intenta comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco más del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su año de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#¿Cómo lo haremos?, usaremos una variable para guardar el resultado del cálculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuación le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float.
#Usaremos esta información para calcular los centimetros

#Finalmente, escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos será escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Nota que al escribir """ también estamos delimitado un string, pero al hacerlo de esta manera,
# los cambios de línea que ocurran en el código se considerarán como parte del string.

print("Bienvenido a ... ")
print("""

                 _     ___    ___    ___   
                ( )   (  _`\ (  _`\ (  _`\ 
 _ __   __     _| |   | |_) )| ( (_)| |_) )
( '__)/'__`\ /'_` |   | ,__/'| |  _ | ,__/'
| |  (  ___/( (_| |   | |    | (_( )| |    
(_)  `\____)`\__,_)   (_)    (____/'(_)    

""")

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str.
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a la red PCP")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
#¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2022-agno-1
print()

#Tercera interacción. Solicitamos la estatura en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centímetros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con red PCP")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

#Para este laboratorio deberás solicitar más datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc.
#2. Guarda esos datos en variables del tipo que corresponda, y finalmente
#3. Escríbelos en pantalla utilizando print.
#4. Recuerda agregar esta información en el perfil del usuario.
#Puedes agregar todas las líneas que necesites.