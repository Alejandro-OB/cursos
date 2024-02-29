
"""TUPLAS"""

# Las tuplas son un tipo de listas inmutables
# Las declaraciones de las tuplas se realizan con parentesis

numbers = (1,2,3,4,5,5)
print(type(numbers))

# para saber las posiciones de los elentos se realiza de la misma manera que las listas

# count() cuenta cuantas veces se repite un elemento

print(numbers.count(5))

# se puede transformar una tupla en una lista

my_list = list(numbers)

my_list[0] = 0
print(my_list)

# tambien se puede pasar de lista a tupla

my_tuple = tuple(my_list)
print(my_tuple)
