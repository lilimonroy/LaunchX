# KATA MODULO 03
# EJERCICIO 01.b
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
# a veces produce un rayo de luz que se puede ver desde la Tierra. 
# Escribe la lógica condicional que usa declaraciones if, else, y elif para alertar a las personas 
# de todo el mundo que deben buscar un asteroide en el cielo. ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

asteroid = 20

dist = float(input("What is the distance of the asteroid? "))

if dist >= asteroid:
    print("Wonderful! The asteroid will be sighted in your region")
else:
    print("Sad! Your region will not be able to see the asteroid in the sky.")
