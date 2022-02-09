# KATA MODULO 04
# EJERCICIO 2 Formateando Cadenas

#En lugar de reemplazar las variables en una cadena larga como parte de un párrafo, utiliza la información para presentarla en un formato tabular. El resultado debería verse así:

#Gravity Facts about Ganymede
#-------------------------------------------------------------------------------
#Planet Name: Mars
#Gravity on Ganymede: 1.4300000000000002 m/s2

# Datos con los que vas a trabajar
#name = "Moon"
#gravity = 0.00162 # in kms
#planet = "Earth"

#Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir.
# Creamos el título

textTitle = "gravity: the planet and its moon."

#print(textTitle)
newTitle = textTitle.title()
print(newTitle)

# Ahora crea una plantilla de cadena multilínea para contener el resto de la información. En lugar de usar kilómetros, 
# debes convertir la distancia a metros multiplicando por 1,000.
# Creamos la plantilla
#Finalmente, usa ambas variables para unir el título y los hechos.
# Unión de ambas cadenas

planet = input("Name Planet ")
satelit = input ("Name Satelit ")
gravity = float(input("Reference Gravity: "))
print("--------------------------------------------------------------------------------")
print("Planet Name:",planet)
gravitySatelit = gravity * 1000
print("Gravity on",satelit, ":",str(gravitySatelit),"m2")





