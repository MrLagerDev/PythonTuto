### Tuplas ###

my_tuple = tuple()                                          # Diferentes formas de definir una tupla
my_other_tuple = ()                                         # Diferentes formas de definir una tupla

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")            # Designamos valores a la tupla
my_other_tuple = (35, 60, 30)                               # Designamos valores a la otra tupla

print(my_tuple)                                             # Imprime "(35, 1.77, 'Brais', 'Moure', 'Brais')"
print(type(my_tuple))                                       # Imprime 'tuple'

print(my_tuple[0])                                          # Imprime el valor localizado en la posicion entre corchetes, en este caso 35
print(my_tuple[-1])                                         # Imprime el valor localizado en la posicion entre corchetes contando desde el final, en este caso "Moure"
                                                            # ☝️🤓 Funciona exactamente como las listas

print(my_tuple.count("Brais"))                              # count() devuelve la cantidad de valores dentro de la tupla que coincidan con el valor que hay entre parentesis
print(my_tuple.index("Moure"))                              # index() devuelve el lugar del primer elemento dentro de la tupla cuyo valor coincida con el valor puesto entre parentesis

# my_tuple[1] = 1.80                                        # Intentamos modificar el valor dentro de la tupla de 1.77 a 1.80
                                                            # Esto da error
                                                            # ☝️🤓 A diferencia de las listas, las tuplas son INMUTABLES

print(my_tuple + my_other_tuple)                            # Imprime la concatenacion de ambas tuplas: "(35, 1.77, 'Brais', 'Moure', 35, 60, 30)" (funciona igual que las listas)
my_sum_tuple = (my_tuple + my_other_tuple)                  # Creamos una nueva tupla cuyo valor es la concatenacion de ambas tuplas
print(my_sum_tuple)                                         # Imprime "(35, 1.77, 'Brais', 'Moure', 35, 60, 30)"

# Si queremos hacer que una tupla sea modificable tiene que convertirse en lista

my_tuple = list(my_tuple)                                   # Modificamos el tipo de tupla a lista
print(type(my_tuple))                                       # Imprime "list"

my_tuple[4] = "MoureDev"                                    # Ahora se puede modificar uno de los valores dentro my_tuple
my_tuple.insert(1, "Azul")                                  # Ahora se puede insertar dentro de my_tuple
print(my_tuple)                                             # Imprime "[35, 'Azul', 1.77, 'Brais', 'Moure', 'MoureDev']"

my_tuple = tuple(my_tuple)                                  # Volvemos a convertir my_tuple en una tupla
print(my_tuple)                                             # Imprime "[35, 'Azul', 1.77, 'Brais', 'Moure', 'MoureDev']"
print(type(my_tuple))                                       # Devuelve "tuple"

del my_tuple                                                # Se puede eliminar my_tuple totalmente, a diferencia de clear() en las listas.
#print(my_tuple)                                            # ERROR NameError: name 'my_tuple' is not defined (my_tuple ya no existe)