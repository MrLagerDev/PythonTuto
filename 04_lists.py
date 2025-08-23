# Listas                                            # ⚠️listas != arrays⚠️

my_list = list()                                    # Diferentes formas de crear listas
my_other_list = []                                  # Diferentes formas de crear listas

print(len(my_list))                                 # Devuelve un 0 porque no hay elementos en la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)                                      # Devuelve el contenido de la lista
print(len(my_list))                                 # Devuelve la cantidad de elementos que hay en una lista, en este caso "7"

my_other_list = [35, 1.77, "Brais", "Moure"]        # En las listas se puede guardar diferentes tipos de datos (int, double, string, etc.)
print(type(my_other_list))                          # Devuelve "List" como tipo

print(my_other_list[1])                             # Devuelve el elemento localizado en la posicion escrita entre corchetes (empieza por 0), en este caso "1.77"
print(my_other_list[-1])                            # Devuelve el elemento localizado en la posicion escrita entre corchetes empezando por el final (empieza por 1), en este caso "Moure"

print(my_other_list.count("Brais"))                 # Devuelve la cantidad de veces que el valor (puesto entre parentesis) aparece en la lista, en este caso "1"
print(my_list.count(30))                            # Devuelve la cantidad de veces que el valor (puesto entre parentesis) aparece en la lista, en este caso "2"

age, height, name, surname = my_other_list          # Estamos asignando los elementos dentro de una lista a las variables que queramos ⚠️Importante escribirlas en el mismo orden que en la lista⚠️
print(name)                                         # Imprime el valor dentro de la lista que haga referencia a la variable name, en este caso "Brais" 

print(my_list + my_other_list)                      # Concatena ambas listas

my_other_list.append("MoureDev")                    # append() añade un nuevo valor a la lista, siempre al final de esta.
print(my_other_list)                                # Imprime "[35, 1.77, 'Brais', 'Moure', 'MoureDev']" ("MoureDev" ha sido añadido a la lista)

my_other_list.insert (1, "Azul")                    # insert() inserta un valor en la lista, empujando el valor que estuviera anteriormente en esa posicion ((indice, valor))
print(my_other_list)                                # Imprime "[35, 'Azul', 1.77, 'Brais', 'Moure', 'MoureDev']" ("1.77" ha sido empujado por "Azul" en la lista y "Azul ahora ocupa su lugar")

my_other_list.remove("Azul")                        # remove() elimina un valor de la lista
print(my_other_list)                                # Imprime "[35, 1.77, 'Brais', 'Moure', 'MoureDev']" (el valor "Azul" se ha eliminado de la lista)

my_list.remove(30)                                  # Elimina el primer elemento que coincide con lo que esta puesto entre parentesis
print(my_list)                                      # Imprime "[35, 24, 62, 52, 30, 17]" (my_list antes tenia 2 elementos "30", ahora solo tiene 1)

my_list.pop()                                       # pop() elimina el ultimo elemento de una lista y adquiere su valor
print(my_list)                                      # Imprime "[35, 24, 62, 52, 30]"" (el "17" del final de la lista ha sido eliminado)
print(my_list.pop())                                # Ahora pop es igual que el valor que ha eliminado, en este caso imprime "30" (porque 17 ya fue eliminado)
print(my_list)                                      # Imprime "[35, 24, 62, 52]"" (pop() ha eliminado el 30 y ha obtenido su valor)
print(my_list.pop(2))                               # Imprime 62 (que es el valor que estaba en el indice escrito entre parentesis) y lo elimina de la lista
print(my_list)                                      # Imprime "[35, 24, 52]" el valor que pop() ha "capturado" ya no esta en la lista

#my_pop_element = my_list.pop()                     # El valor eliminado por pop() tambien se puede guardar en una variable (para evitar perder ese valor cuando se haga otro pop())
#print(my_pop_element)                              # Imprimiria el valor asignado a esta variable

del my_list[2]                                      # del elimina un elemento de la lista en la posicion del numero introducido entre los corchetes (a diferencia de pop() no guarda ningun valor)
print(my_list)                                      # Imprime "[35, 24]" (el numero en la posicion 2 ha sido eliminado)
                                                    # ⚠️DIFERENCIA ENTRE del Y remove()⚠️: remove() elimina el elemento que coincida con lo que hay entre parentesis, del elimina el elemento que hay en una posición

my_new_list = my_list.copy()                        # copy() copia el contenido de una variable en el momento del copy (⚠️si hiciera "my_new_list" = "my_list", cualquier cambio a "my_list" afectaria a "my_new_list"⚠️)

my_list.clear()                                     # clear() vacia todos los valores de la lista
print(my_list)                                      # Imprime "[]" (todos los valores de la lista han sido borrados)
print(my_new_list)                                  # Imprime "[35, 24]" (mantiene los valores aunque modifiques "my_list")

my_new_list.reverse()                               # reverse() invierte el orden de los valores dentro de la lista
print(my_new_list)                                  # Imprime "[24, 35]" (la lista ha sido invertida)

my_new_list.append(80)                              #introduzco datos aleatorios porque me he quedado solo con 2 valores en la lista 😅
my_new_list.append(90)
my_new_list.append (30)
my_new_list.append(50)
print(my_new_list)                                  # Imprime "[24, 35, 80, 90, 30, 50]" (se han introducido nuevos datos con append())
my_new_list.sort()                                  # sort() ordena los elementos de la lista de forma ascendente (en caso de strings los ordena por orden alfabetico)
print(my_new_list)                                  # Imprime "[24, 30, 35, 50, 80, 90]" (la lista se ha ordenado)

# ⛔Esto puede ser problematico⛔
my_list = "Hola Python"                             # Se puede asignar un string a la variable, lo que cambia la variable de "list" a "str"
print(my_list)                                      # Devuelve "Hola Python"
print(type(my_list))                                # El tipo a cambiado a "str"