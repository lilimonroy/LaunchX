# KATA MODULO 05
# EJERCICIO 01 Utilizar operadores aritméticos

# Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas. Comenzaremos usando dos distancias de planetas: 
# Tierra (149.597.870 km) y Júpiter (778.547.200 km).
# Crear variables para almacenar las dos distancias

from turtle import distance


dist_earth = 149597870 
dist_jupyter = 778547200

# Con los valores obtenidos, es el momento de añadir el código para realizar la operación. 
# Restarás el primer planeta del segundo para determinar la distancia en kilómetros.

dist_planets = abs(dist_earth - dist_jupyter)

# A continuación, puedes convertir la distancia del kilómetro en millas multiplicándola por 0.621.

dist_planets_miles = dist_planets * 0.621 

print("The distance between The Earth and Jupyter in miles is", str(dist_planets_miles), "and in kilometers is",str(dist_planets))