### Bucles ###

# While #
my_condition = 0

while my_condition < 10:                            # Mientras my_condition < 10 va a ejecutar el codigo dentro del bucle en el momento que sea = a 10 saldra del bucle y continuara
    print(my_condition)                             # Imprimira el valor que tenga my_condition en cada iteración
    my_condition +=1                                # Le suma 1 a my_condition por cada iteración (☝️🤓 En python no existe el ++)
else:
    print("my_condition es mayor o igual a 10")     # En python a diferencia de otros lenguajes se puede poner un else en los bucles

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:                          # En el momento que se da la condicion del if para el bucle, realiza la accion del if y despues continua el bucle
        print("my_condition es 15")
        #break                                      # La forma de salir del bucle a partir de un if es con un break
        #continue                                   # La forma de continuar con la siguiente iteracion del bucle
    
    print (my_condition)
print("Salida del while")

# For #
my_list = [35, 24, 62, 52, 30, 17]                                                  # Creacion de una lista
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")                                    # Creacion de una tupla
my_set = {"Brais", "Moure", 35}                                                     # Creacion de un set
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python" }            # Creacopm de im diccionario

for element in my_list:                                                             # element se usa para iterar sobre los elementos de una lista
    print(element)
print("-----------salida de la lista--------------------------")                                    ### Salida de la lista ###
                                                                                    #35
                                                                                    #24
                                                                                    #62
                                                                                    #52
                                                                                    #30
                                                                                    #17
                                                                                    #☝️🤓 Imprime los valores de la lista ☝️🤓#

for element in my_tuple:                                                            # element se usa para iterar sobre los elementos de una tupla
    print(element)
print("-----------salida de la tupla--------------------------")                                    ### Salida de la tupla ###
                                                                                    #35
                                                                                    #1.77
                                                                                    #Brais
                                                                                    #Moure
                                                                                    #Brais    
                                                                                    #☝️🤓 Imprime los valores de la tupla ☝️🤓#              

for element in my_set:                                                              # element se usa para iterar sobre los elementos de un set
    print(element)
print("-----------salida de el set--------------------------")                                      ### Salida del set ###
                                                                                    #Moure
                                                                                    #35
                                                                                    #Brais
                                                                                    #☝️🤓 Imprime el contenido del set de manera desordenada ☝️🤓#

for element in my_dict:                                                             # element se usa para iterar sobre los elementos de un dict
    print(element)
print("-----------salida de el dict--------------------------")                                     ### Salida del dict ###
                                                                                    #Nombre
                                                                                    #Apellido
                                                                                    #Edad
                                                                                    #1
                                                                                    #☝️🤓 Ha imprimido las Claves, no los Valores ☝️🤓#