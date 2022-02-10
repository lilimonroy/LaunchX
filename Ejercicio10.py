# KATA MODULO 05
# EJERCICIO 02 Convierte cadenas en números y usa valores absolutos

# Planeta 	Distancia al sol
# Mercurio 	57900000
# Venus 	108200000
# Tierra 	149600000
# Marte 	227900000
# Júpiter 	778600000
# Saturno 	1433500000
# Urano 	2872500000
# Neptuno 	4495100000

# Para crear nuestra aplicación, queremos leer la distancia del sol para dos planetas, y luego mostrar la distancia entre los planetas. 
# Usando input, agrega el código para leer la distancia del sol para cada planeta, considerando 2 planetas.
# Convierte las cadenas de ambos planetas a números enteros

dist_planeta01 = int(input("Enter the distance for the first planet: "))
dist_planeta02 = int(input("Enter the distance for the second planet: "))


# Con los valores almacenados como números, ahora puedes agregar el código para realizar el cálculo, restando el primer planeta del segundo.
# Debido a que el segundo planeta podría ser un número mayor, usarás abs para convertirlo a un valor absoluto. 

dist_planets = abs(dist_planeta01 - dist_planeta02)


# También agregarás el código para mostrar el resultado en millas multiplicando la distancia del kilómetro por 0.621

dist_planets_miles = dist_planets * 0.621

print("The distance in kilometers between planets is",dist_planets)
print("The distance in miles between planets is",dist_planets_miles)

