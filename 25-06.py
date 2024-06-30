# Longitu de string
# Funcion Len


string= "    "
print(len(string))

#Rebanar un string
# Funcion SLICING (PARA "REBANAR UNA PARTE DE LA CADENA")
# EL INICIO VA SER EL INDICE DEL PRIMER CARACTER DE LA CADENA QUE QUEREMOS REBANAR
#FIN VA SER EL INDICE DEL ULTIMO CARACTER NO INCLUIDO DE LA CADENA QUE QUE QUEREMOS REBANAR
#PASO: NOS INDICA CADA CUANTO CARACTERES VAMOS A SELECCIONAR ENTRE LAS POSCIONES DE INICIO Y DE FIN 

saludo= "Hola. como estas?"
saludo[0:3:1]
print(saludo[0:3:1])
print(saludo[0:3:2])


palabra ="pithon"
print(palabra)
print(palabra[1])
palabra = palabra[0:1] +"y" + palabra[2:]   
print(palabra)


# LISTA Y TUPLAS
mi_lista = [-11,20,3,41]
print(mi_lista)
otra_lista = ["hola","como","estas","?"]
variable_1 =" una variable"
listita = [1, -10, 132.5, "un string", variable_1]
print(listita)

print(listita[0])
print(listita[1])
print(listita[:-2])
## concatenar
print(listita + [otra_lista, "algo random"])

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16])
      
numeros = [0,2,4,5,10,20]
numeros[3] = 8
print(numeros)


letras =["a", "b", "c", "d", "e", "f"]
letras[:3] = ["A", "B", "C"]
print(letras)

# FUNCION APPEND - AGREGO UN ITEM AL FINAL DE LA LISTA - se escribe mi_lista.append(item_a_agregar)

numeros = [0,2,4,5,10,20]
numeros.append(21)
print(numeros)

print(len(numeros))    #Me cuenta los items ( son los caracteres que sepra la coma) que tiene la lista , incluido el agregado por append 
    # FUNCION POP
    # LA FUNCION POOP ES CONTRARIO A PEND, ELIMINA EL ULTIMO ITEM DE UNA LISTA.pop.() 
equipos =   [1, 2, 3, 4]
equipos.pop(2)
print(equipos)

 # FUNCION COUNT.cuenta repeticion- se ESCRIBE la_lista:a_contar
numeros_varios = [1, 2, 3, 4,20,20,20,6,2,5]
print(numeros_varios.count(20))


#INDEX
#Busca el item y nos devuelve en que indice esta- SE ESCRIBE la_lista.index(lo_que_queresmos_buscar)

numeros_varios = [1, 2, 3, 4,20,20,20,6,2,5]
print(numeros_varios.index(5))


## tuplas
# tuplas similares a las listas, la GRAN diferencia es que la tuplas son INMUTABLES
# SE DEclaran con parentecis- mi_tupla(1,2,3,4,5)
mi_tupla = (1,2,3,4,5)
print(mi_tupla)
tupla = (1,)
print(tupla)
otra_tupla = (1,5,-100, "cadena", "otra cadena/string", mi_tupla)
print(otra_tupla)


