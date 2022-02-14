# KATA MODULO 07
# EJERCICIO 02 Creación de un ciclo "for"

# Escribe tu ciclo for para iterar en una lista de planetas

planets = []

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

for eachPlanet in planets:
    print(eachPlanet)
