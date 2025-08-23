# Operadores aritmeticos

print(5 + 3)                                                # Devuelve el resultado de la suma: 8
print(5 - 3)                                                # Devuelve el resultado de la resta: 2
print(5 * 3)                                                # Devuelve el resultado de la multiplicacion: 15
print(5 ** 3)                                               # Devuelve el resultado de un numero elevado a otro: 125
print(5 / 3)                                                # Devuelve el cociente de la division: 1.66666666
print(5 // 3)                                               # Devuelve el cociente de la division redondeando hacia abajo: 1
print(5 % 3)                                                # Devuelve el resto de la division: 2

print ("Hola" + " " + "Mundo")                              # Concatena texto, tambien se puede hacer separando textos con comas ","
#print ("Hola" + 5)                                         # En este caso da error al sumar un string a un int
print ("Hola " + str(5))                                    # Aqui se se combinan porque conviertes 5 que es un int en string
print ("Hola " * 5)                                         # Repite la palabra el numero de veces por la que lo multiplicas

# Operadores Comparativos (<, >, <=, >=, ==, !=)            # Funciona exactamente igual que en Java y C# 

# Operadores logicos
print (3 > 4 and "Hola" > "Python")                         # ⚠️A diferencia de Java o C# en el que seria "&&" aqui es "and"⚠️
print (3 > 4 or "Hola" > "Python")                          # ⚠️A diferencia de Java o C# en el que seria "||" aqui es "or"⚠️
print (not (3 > 4))                                         # ⚠️A diferencia de Java o C# en el que seria "!" aqui es "not"⚠️

