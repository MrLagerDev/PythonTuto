# strings
my_line_string = "Este es mi string\ncon salto de linea"                    # \n = salto de linea
print (my_line_string)                                                     

my_tab_string = "\tEste es mi string con tabulacion"                        # \t = tabulacion
print (my_tab_string)

my_scape_string = "\\tEste es un string\\nescapado"                         #\ anula la funcion de lo que tiene detras y permite su escritura
print (my_scape_string)

# Formateo                                                                  

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es: %s, mi apellido es: %s y tengo %d años" %(name, surname, age))                # Funciona parecido a el "printf" de Java (%s = string, %d = int, %f = double)
print("Mi nombre es: {}, mi apellido es: {} y tengo {} años".format(name, surname, age))           # Este es una mezcla del "printf" de Java y el "($" de C#
print(f"Mi nombre es: {name}, mi apellido es: {surname} y tengo {age} años")                       # Exactamente igual que el "($"" de C#

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language                                                 # Divide la palabra entre sus letras designadas por los caracteres
print(a)                                                                    # Imprime "p"
print(b)                                                                    # Imprime "y"

# Division

language_slice = language[1:3]                                              # Asignando el 2º y 4º caracter a "language_slice" (el array empieza por 0)
print(language_slice)                                                       # Imprime "yt"

language_slice = language[1:]                                               # Al no haber un segundo valor asignado imprime el resto de la palabra
print(language_slice)                                                       # Imprime "ython"

language_slice = language[-2]                                               # Imprime el caracter que esta en segundo lugar empezando desde el final (en este caso no empieza por 0)
print(language_slice)                                                       # Imprime "o"

# Reverse 

reversed_language = language[::-1]                                          # Imprime la cadena de caracteres al reves
print(reversed_language)                                                    # Imprime nohtyp

# Funciones

print(language.capitalize())                                                # ☝️🤓capitalize() hace que la primera letra sea mayuscula, en este caso "Python"
print(language.upper())                                                     # ☝️🤓upper() convierte toda la cadena en mayusculas, en este caso "PYTHON"
print(language.count("t"))                                                  # ☝️🤓count() devuelve el numero de veces que se repite una letra dentro de una cadena, en este caso "t" se repite 1 vez
print(language.isnumeric())                                                 # ☝️🤓isnumeric() devuelve "true" o "false" dependiendo de su la variable es un numero o no, en este caso devuelve "false"
print("1".isnumeric())                                                      # ☝️🤓En este caso devuelve "true"
print(language.lower())                                                     # ☝️🤓convierte todas las letras de la cadena en minusculas, en este caso imprime "python"
print(language.upper().isupper())                                           # ☝️🤓isupper() devuelve "true" o "false" dependiendo de si todas las letras de la cadena son mayusculas, en este caso "true"
print(language.startswith("py"))                                            # ☝️🤓startswith() devuelve "true" o "false" dependiendo de si la cadena de caracteres empieza por las letras introducidas entre parentesis