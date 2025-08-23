### Funciones ###

def my_function ():                                                         # Creacion de una funcion (es necesario poner def al principio)
    print("Esto es una funcion")

my_function()                                                               # Para llamar a la funcion funciona igual que en Java y C#

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)                                                        # Devuelve 12
sum_two_values(54754, 71231)                                                # Devuelve 125985
sum_two_values("5", "7")                                                    # Devuelve 57 (😤 no esta tipado y hay que tener cuidado con los datos que introduces😤)
sum_two_values(1.4, 5.2)                                                    # Devuelve 6.6

def sum_two_values(first_number: int, second_number: int):                  # ¿Y si especificamos el tipo de dato que queremos? 🤔
    print(first_number + second_number)

sum_two_values(5, 7)                                                        # Devuelve 12 🙂
sum_two_values(54754, 71231)                                                # Devuelve 125985 😃
sum_two_values("5", "7")                                                    # Devuelve 57 (😭Le da igual😭)
sum_two_values(1.4, 5.2)                                                    # Devuelve 6.6 😭

def sum_two_values_with_return(first_value, second_value):                  # Tambien se pueden hacer funciones que devuelvan algo
    return first_value + second_value

print(sum_two_values_with_return(10, 5))                                     # Devuelve 15

def print_name(name, surname):
    print(f"Mi nombre es {name} y mi apellido es {surname}")                # Concatenacion con (f"")

print_name ("Brais", "Moure")                                               # Asignacion de valores que se le pasaran a la funcion

print_name(surname = "Moure", name = "Brais")                               # Forma de asignar los datos que pide y de reorganizarlos si quieres, en este caso he puesto antes el apellido y despues el nombre

#print_name(input("Escribe tu nombre "), input("Escribe tu apellido "))     # Esto no lo explica el, pero tenia curiosidad de ver si se podia hacer 

def print_name_with_default(name, surname, alias = "Sin alias"):            # Se ha asignado por defecto "Sin alias" en alias, si el usuario no rellena el dato requerido en alias, automaticamente escribira el por defecto
    print(f"Me llamo {name} mi apellido es {surname} y mi alias es {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")                       # Devuelve "Me llamo Brais mi apellido es Moure y mi alias es MoureDev"
print_name_with_default("Brail", "Moure")                                   # Devuelve "Me llamo Brais mi apellido es Moure y mi alias es Sin alias" (Solo se ha introducido nombre y apellido)

def print_texts(*text):                                                     # Al escribir "*" antes del nombre del dato que quieres introducir, permites que no haya limite
    print(text)

print_texts ("Hola", "Python", "MoureDev")                                  # Devuelve "('Hola', 'Python', 'MoureDev')" gracias a el "*"

def print_texts(*texts):                                                    # Ahora puede iterar    
    for text in texts:
        print(text)

print_texts ("Hola", "Python", "MoureDev")                                  # Devuelve  #Hola
                                                                                        #Python
                                                                                        #MoureDev          

def print_upper_texts(*texts):                                              # Función que imprime los textos en mayusculas
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")                             # Devuelve  #HOLA
                                                                                        #PYTHON
                                                                                        #MOUREDEV
