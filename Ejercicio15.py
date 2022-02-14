# KATA MODULO 08
# EJERCICIO 01 Crear y modificar un diccionario de Python
# Agrega el código para crear un nuevo diccionario denominado 'planet'. Rellena con la siguiente información:

# name: Mars
# moons: 2

# Crea un diccionario llamado planet con los datos propuestos
# Para recuperar valores, puede utilizar el método get o corchetes ([ ]) con el nombre de la clave que desea recuperar.

# Muestra el nombre del planeta y el número de lunas que tiene.


planet = {'name':'Mars', 'moons':'2'}

print("The planet " + planet.get('name') + " has " + planet['moons'] + " moons")

planet['circunferencia (km)'] = {'polar': '6752','equatorial':'6792'}

# Imprime el nombre del planeta con su circunferencia polar.

print(planet.get('name') + ' ' + planet['circunferencia (km)']['polar'])

print(planet)