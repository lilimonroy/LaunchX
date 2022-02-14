# KATA MODULO 09
# EJERCICIO 01 Trabajar con argumentos en funciones
# En este ejercicio, construirás un informe de combustible que requiere 
# información de varias ubicaciones de combustible en todo el cohete.

# Comienza por crear una función que necesite tres lecturas de combustible y devuelva un informe:
# Función para leer 3 tanques de combustible y muestre el promedio


def main_report(tanque01,tanque02,tanque03):
    print(" Tank 01: ",str(tanque01),"\n","Tank 02: ",str(tanque02),"\n","Tank 03: ",str(tanque03),"\n")
    return report_average(80, 70, 85)


def report_average(tanque01,tanque02,tanque03):
    average = round((tanque01 + tanque02 + tanque03)/3,3)
    return "The average of three lectures is "+ str(average)

    

# Ahora que hemos definido la función de informes, vamos a comprobarlo. Para esta misión, los tanques no están llenos:
# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))

print(main_report(80, 70, 85))