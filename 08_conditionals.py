###Condicionales###                                         # Funciona parecido a Java pero con sus diferencias
###Nota###                                                  # Es bastante parecido en general a como funciona en Java, así que no me voy a extender demasiado

my_condition = True

if my_condition:                                            # En python las condiciones no tienen parentesis, y en vez de llaves se usa ":"
    print("El booleano es \"True\"")                        # Es muy importante tener en cuenta las tabulaciones, si el texto esta a la misma altura del if no entra dentro del condicional

print("La ejecución continua")                              # Salir de un if es tan sencillo como quitar la tabulacion

my_condition = False

if my_condition:
    print("El booleano es \"True\"")                        # Esta condicion no se da asi que no entra dentro del condicional

print("La ejecución continua")                              # Esta fuera del if

my_condition = 5 * 2

if my_condition == 10:
    print("El valor de la condicion es 10")
else:                                                       # Else para que haga en caso de que no se de la condición
    print("El valor de la condicion no es 10")
print("La ejecución continua") 

if my_condition >= 10:
    print("La condicion es igual o mayor que 10")
else:
    print("La condicion es menor a 10")
print("La ejecución continua")                               # Esta fuera del if

my_condition = 25

if my_condition > 10 and my_condition < 20:                 # Ha de cumplir ambas condiciones para cumplir la condicion asignada (Funciona como el && de Java)
    print("La condicion es igual o mayor que 10 y menor que 20")
elif my_condition == 1:                                     # Funciona como else if de Java
    print("La condicion es igual a 1")
elif my_condition == 25:                                    # Funciona como else if de Java
    print("La condicion es igual a 25")
else:
    print("La condicion es menor a 10 o mayor o igual a 20")
print("La ejecución continua")                              # Esta fuera del if

#if not my_condition                                        # Funciona como if(!my_condition) de Java
#if my_condition == "x" or my_condition =="y"               # Funciona como if(my_condition == "x" || my_condition == "y") de Java