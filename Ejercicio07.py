# KATA MODULO 04
# EJERCICIO 01.a Transformar cadenas

# El texto con el que trabajarás es el siguiente:
# text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""




text = """Interesting facts about the Moon.\nThe Moon is Earth's only satellite.\nThere are several interesting facts about the Moon and how it affects life here on Earth.\nOn average, the Moon moves 4cm away from the Earth every year.\nThis yearly drift is not significant enough to cause immediate effects on Earth.\nThe highest daylight temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:

text_split= text.split('\n')
#print(text)
#print(text_split)

# Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
# Define las palabras pista: average, temperature y distance suenan bien

keyword = ['average','temperature','distance']

# Crea un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente.
# Ciclo for para recorrer la cadena:

#for each_sentence in text_split:        #Recorre las sentencias separadas con split
    #for each_word in keyword:           #Recorre cada palabra clave
        #if each_word in each_sentence:  #Si palabra clave está en sentencia:
           # print(each_sentence)        #Imprime sentencia  


#Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius: Ciclo para cambiar C a Celsius

for each_sentence in text_split:
    for each_letter in each_sentence:
        if each_letter in ' C':
            new_sentence = each_sentence.replace(' C', ' Celsius')

print(new_sentence)
        # if each_word in each_sentence:
 #           print(each_word.replace(" C", "Celsius"))
        
#print(text_split)
