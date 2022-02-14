# KATA MODULO 07
# EJERCICIO 01
#

# Declara dos variables


planets = []


# Comenzando con las variables que acabas de crear, crearás un ciclo while. 
# El ciclo while se ejecutará mientras el new_planet no sea igual a la palabra 'done'.
# Dentro del ciclo, comprobarás si la variable new_planet contiene un valor, 
# que debería ser el nombre de un planeta. Esta es una forma rápida de ver si el usuario ha introducido un valor. 
# Si lo han hecho, tu código agregará (append) ese valor a la variable planets.

# Finalmente, usarás input para solicitar al usuario que ingrese un nuevo nombre de planeta o que 
# escriba done si ha terminado de ingresar nombres de planeta. Almacenará el valor de input en la variable new_planet.

# Escribe el ciclo while solicitado

flagPlanetlanet = True
while  flagPlanetlanet == True:
    newPlanet = input("Enter the name of the planet: ")
    if newPlanet == "done":
        flagPlanetlanet = False
        break     
    else:
        newPlanet = newPlanet.title()
        planets.append(newPlanet)
        flagPlanetlanet = True

print(planets)

