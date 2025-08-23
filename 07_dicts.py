###Diccionarios###

my_dict = dict()                                                            # Formas de crear diccionarios
my_other_dict = {}                                                          # Formas de crear diccionarios

print(type(my_dict))                                                        # Devuelve "dict"
print(type(my_other_dict))                                                  # Devuelve "dict"

my_other_dict = {"Nombre":"Brais","Apellido":"Moure","Edad":35, 1:"Python"}             # Los diccionarios se componen de relaciones Clave : Valor (☝️🤓 Al construirlo de esta manera ya no se convierte en set)

my_dict = {                                                                 # Otra forma de formatear un diccionario mas visual
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes": {"Python", "Swift", "Kotlin"}                               # Un diccionario puede tener un set dentro, este seguira desordenado
    }

print (my_other_dict)                                                       # Devuelve "{'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}"
print (my_dict)                                                             # Devuelve "{'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Kotlin', 'Python'}}"

print(len(my_other_dict))                                                   # Devuelve 4 (☝️🤓En los diccionarios Clave y Valor cuentan como una sola unidad)
print(len(my_dict))                                                         # Devuelve 4 (☝️🤓 el set entero cuenta como un Valor asi que sigue siendo 4)

print(my_dict["Nombre"])                                                    # Devuelve "Brais" (El valor asociado a la clave "Nombre")

my_dict["Nombre"] = "Pedro"                                                 # El valor se puede editar
print(my_dict["Nombre"])                                                    # Devuelve "Pedro"

my_dict["Calle"] = "Calle MoureDev"                                         # Se pueden añadir Claves y Valores asi
print(my_dict)                                                              # Devuelve "{'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Python', 'Swift', 'Kotlin'}, 'Calle': 'Calle MoureDev'}"

del my_dict["Calle"]                                                        # Forma de eliminar una clave (☝️🤓Si no especificaramos entre corchetes eliminaria todo el diccionario)
print (my_dict)                                                             # Devuelve "{'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Kotlin', 'Python'}}" (El campo de "Calle ha desaparecido")

print("Moure" in my_dict)                                                   # Devuelve "False"
print("Apellido" in my_dict)                                                # Devuelve "True" (☝️🤓 Solo se puede buscar de esta manera las claves, no los valores)

print(my_dict.items())                                                      # Devuelve "dict_items([('Nombre', 'Pedro'), ('Apellido', 'Moure'), ('Edad', 35), ('Lenguajes', {'Python', 'Swift', 'Kotlin'})])" (Devuelve Claves con su Valor)
print(my_dict.keys())                                                       # Devuelve "dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes'])" (Devuelve solo las Claves)
print(my_dict.values())                                                     # Devuelve "dict_values(['Pedro', 'Moure', 35, {'Python', 'Swift', 'Kotlin'}])" (Devuelve solo los Valores)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))                          # .fromkeys sirve para crear un nuevo diccionario sin valores
print(my_new_dict)                                                          # Devuelve "{'Nombre': None, 1: None}"

my_list = ["Nombre", 1, "Piso"]                                             # Creacion de lista
my_other_new_dict = dict.fromkeys(my_list)                                  # ☝️🤓 Tambien sirve para copiar las claves a partir de una lista
print(my_other_new_dict)                                                    # Devuelve "{'Nombre': None, 1: None, 'Piso': None}" (El contenido de la lista son Claves en este diccionario)
my_other_new_dict = dict.fromkeys(my_dict)                                  # Funciona tambien con otros diccionarios
print(my_other_new_dict)                                                    # Devuelve "{'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None}" (Ha sustituido las Claves que tenia antes por las nuevas)

my_other_new_dict = dict.fromkeys(my_dict,("Brais", "Moure"))               # Introduce el mismo valor a todas las claves
print(my_other_new_dict)                                                    # Devuelve "{'Nombre': ('Brais', 'Moure'), 'Apellido': ('Brais', 'Moure'), 'Edad': ('Brais', 'Moure'), 'Lenguajes': ('Brais', 'Moure')}" (Ahora todos los valores son "Brais", "Moure")

### Nota propia ###                                                         # A partir de aqui se le va la pinza y empieza a mezclar conceptos y a hacerlo lo mas rebuscado posible.
