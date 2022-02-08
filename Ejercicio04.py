# KATA MODULO 03
# EJERCICIO 01.a
# Programa una lógica condicional que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido. 
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 
# 25 kilómetros por segundo (km/s) merece una advertencia.

careful = 25

dist = float(input("What is the distance of the asteroid? "))

if dist > careful:
    print("Look it up! WARNING! THE ASTEROID IS NEAR TO EARTH!")
else:
    print("All under control. No worries.")