# KATA MODULO 06
# EJERCICIO 02 Trabajando con datos de una lista

# Lista de planetas

from matplotlib.pyplot import flag, title


#planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

planets = []

# Solicitamos el nombre de un planeta *Pista:  input()* Pídale al usuario que use una letra mayúscula para comenzar el nombre del planeta.

newPlanet = input("Enter the name of the planet: ")
newPlanet = newPlanet.title()
planets.append(newPlanet)
flag = True
while flag == True:
    response = input("Do you wanna enter a new planet on the list? [yes|no] ")
    response = response.lower()
    if response == "yes":
        newPlanet = input("Enter the name of another planet: ")
        newPlanet = newPlanet.title()
        planets.append(newPlanet)
        flag = True
    elif response == "no":
        flag = False
    else:
        print("Error in your input")

print(planets)


# Busca el planeta en la lista

index_newPlanet = planets.index(newPlanet)
print(index_newPlanet)

# Muestra los planetas más cercanos al sol

planets_nearSun = planets[0:index_newPlanet+1]
print(planets_nearSun)

# Muestra los planetas más lejanos al sol

planets_farSun = planets[::-1]
print(planets_farSun)