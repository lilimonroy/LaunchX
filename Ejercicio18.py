# KATA MODULO 09
# EJERCICIO 02 Trabajo con argumentos de palabra clave
# Función con un informe preciso de la misión. 
# Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def report_mision(time_preLaunch,time_takeoff,destiny,tank_extern,tank_intern):
    
    print ("The destiny of our mission is",destiny,"\nThe time of the flight is",str(time_takeoff),"\nThe pre-Lunnch is programmed to",str(time_preLaunch),"\nSTATE OF TANKS\nExtern Tank",str(tank_extern),"\nIntern Tank",str(tank_intern))
    return "End of report"

print(report_mision("14:30",8,"Mars",152,182))