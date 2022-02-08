# KATA MODULO 03
# EJERCICIO 01.c
# Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán a medida que entren en la atmósfera de la Tierra.
# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
# También discutimos en el ejercicio anterior que:
# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) 
# merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver 
# desde la Tierra.
# Usando toda esta información, escribe un programa que emita la advertencia o información correcta a la gente de la Tierra, según la velocidad 
# y el tamaño de un asteroide. 


asteroid_size = float(input("What is the size of the asteroid? "))

if (asteroid_size > 25 and asteroid_size < 1000):
        print("DANGEROUS!!! You can see the asteroid in the sky aproaching to Earth!!!")
elif asteroid_size <= 25:
    print("The world is save! Don't worry")
else:
    print("Danger!!! The asteroid is so big. Wait for instructions.")

asteroid_veloc = float(input("What is the velocity of the asteroid? "))
if asteroid_veloc >=20:
        print("Be careful! Probably you can see the asteroid in your region. Look at the sky!")
else:
        print("The asteroid it won't appears in your region'sky")