# KATA MODULO 08
# EJERCICIO 02: Programación dinámica con diccionarios

# Calcularás tanto el número total de lunas en el sistema solar como el número promedio de lunas que tiene un planeta.
# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

totalMoons = 0
totalPlanets = 0
for planet,moons in planet_moons.items():
    totalMoons = (totalMoons + moons)
    totalPlanets = len(planet_moons)
    averageMoons = round(totalMoons/totalPlanets,2)
print("There is ",str(totalMoons), "moons in the solar system")

# Finalmente calcule el promedio dividiendo total_moons por planets e imprimiendo los resultados.

print("The average of moons in the solar system is",str(averageMoons))