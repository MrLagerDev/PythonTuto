# Variables                                                                         # Las variables no tienen tipado... solo hace falta el nombre de la variable
my_string_variable = "Mi string variable"                                           # Lo correcto es escribir las variables en minusculas separados por una barra baja "_" (snake_case)
print(my_string_variable)                                                           # tipo string🆎

my_int_variable = 5
print(my_int_variable)                                                              #tipo int🔢

my_bool_variable = False
print(my_bool_variable)                                                             #tipo bool✅/❌

# Concatenacion
print(my_string_variable, my_int_variable, my_bool_variable)                        # Concatenacion de varias variables
print("Este es el valor de :",my_bool_variable)                                     # Concatenacion de texto con variable

my_int_variable = str(my_int_variable)                                              # transforma el int en string
print(type(my_int_variable))

# Funciones
print(len(my_string_variable))                                                      # "len" devuelve la cantidad de caracteres en una variable 📏

# Variables en una sola linea ⛔No recomendado abusar de esto⛔
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35                        # se puede crear varias variables seguidas y luego introducir los valores
print("Me llamo", name, surname, "mi edad es:", age, "y mi alias es", alias)

# Inputs                                                                            # Funciona como un Scanner (Java) o un Console.Read (C#)
name = input ("¿Cual es tu nombre? ")                                                # Asigna un valor a "name" a partir de lo que se escriba en consola tras imprimir lo que tiene entre parentesis
age = input ("¿Cuantos años tienes? ")                                               # Asigna un valor a "age" a partir de lo que se escriba en consola tras imprimir lo que tiene entre parentesis

print (name)                                                                        # Devuelve el valor de "name"
print (age)                                                                         # Devuelve el valor de "age"