"""Existen varios loops que puedo utilizar"""

# while me permite ejecutar una acción mientras el parametro de esta sea verdadero

COUNTER = 0
while COUNTER < 10:
    COUNTER += 1
    print(COUNTER)

# se puede interrumpir o continuar con el ciclo usando break o continue

COUNTER = 0
while COUNTER < 20:
    COUNTER += 1
    if COUNTER > 15:
        break
    print(COUNTER)

COUNTER = 0
while COUNTER < 20:
    COUNTER += 1
    if COUNTER < 15:
        continue
    print(COUNTER)

# También existe el ciclo for el cual itera entre un
    # rango o un conjunto de elementos

for element in range(10):
    print(element)

#se puede empezar en 1 y terminar en 10 de la siguiente manera

for element in range(1, 11):
    print(element)

# se puede iterar en una lista, tupla o diccionario

my_list = [1,2,3,4]

for number in my_list:
    print (number)

my_tuple = ('Juan', 'José', 'Carlos')
for nombre in my_tuple:
    print(nombre)

my_dictionary = {
    'Name' : 'Juan' ,
    'Age' : 40
}

for key in my_dictionary:
    print(key, '=>', my_dictionary[key])


people = [
    {
        'name' : 'José',
        'age' : 39
    },
    {
        'name' : 'Alejandro',
        'age' : 21
    }
]

for person in people:
    print('name =>',person['name'])
