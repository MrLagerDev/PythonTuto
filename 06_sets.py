###Sets###

my_set = set()                                                  # Creacion de un set
my_other_set ={}                                                # Creacion de un "set"

print(type(my_set))                                             # Imprime set
print(type(my_other_set))                                       # Imprime dict 🤔

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))                                       # Imprime set 👏
                                                                # ☝️🤓 una variable "X = {}" es dictionary hasta que rellenas las llaves, en ese momento pasa a ser set

print(len(my_other_set))                                        # Devuelve la cantidad de elementos en el set, en este caso "3"

my_other_set.add("MoureDev")
print(my_other_set)                                             # Imprime "{'MoureDev', 35, 'Moure', 'Brais'}" (☝️🤓un set no es una estructura ordenada)
my_other_set.add("MoureDev")
print(my_other_set)                                             # Devuelve lo mismo que antes (☝️🤓Un set no admite repetidos)

print("Moure" in my_other_set)                                  # Devuelve true (☝️🤓 Esto sirve para comprobar si un elemento existe dentro de un set)
print("Mouri" in my_other_set)                                  # Devuelve false (☝️🤓 Esto sirve para comprobar si un elemento existe dentro de un set)

my_other_set.remove("Moure")                                    # Sirve para eliminar un valor dentro del set
print(my_other_set)                                             # Devuelve "{'MoureDev', 35, 'Brais'}" (Se ha eliminado "Moure" del set)

my_other_set.clear()                                            # Vacia el set de valores
print(my_other_set)                                             # Devuelve "set()"
print(len(my_other_set))                                        # Devuelve "0" (El set ha sido vaciado)

del my_other_set                                                # Elimina la variable
#print(my_other_set)                                            # ERROR: my_other_set ya no existe

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)                                                  # Devuelve "['Brais', 35, 'Moure']" (☝️🤓 Las listas pueden contener sets)
print(my_list[0])                                               # Devuelve el elemento en posicion 0 de la lista (⚠️Los elementos seran posicionados de forma desordenada y pasaran a ser fijos al crear la lista⚠️)

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)                         # Se pueden unir diferentes sets en uno con el ".union"
print(my_new_set)                                               # Devuelve "{'Python', 35, 'Swift', 'Kotlin', 'Moure', 'Brais'}" (ambos sets estan mezclados de forma desordenada)
print(my_new_set.union(my_new_set).union(my_set))               # Devuelve "{35, 'Python', 'Kotlin', 'Swift', 'Brais', 'Moure'}" (no acepta repetidos)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))           # Devuelve "{'Swift', 'C#', 35, 'Kotlin', 'JavaScript', 'Python', 'Brais', 'Moure'}"(☝️🤓 Se pueden integrar mas valores dentro de un set con .union, sin necesidad de establecer un set para esos nuevos valores)
                                                                                        # ☝️🤓Al haber hecho el .union dentro del print solo tendra esos valores añadidos en la impresion, despues volvera a tener los valores de antes

print(my_new_set.difference(my_set))                            # Devuelve "{'Kotlin', 'Python', 'Swift'}" .difference elimina los elementos que se encuentran en el set entre parentesis