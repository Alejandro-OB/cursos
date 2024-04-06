
"""
listas comprimidas
"""
# Se puede generar listas más cortar que otras
import random

numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

# Lista comprimida

numbers_v2 = [element for element in range(1,11) ]
print(numbers_v2)

# se puede crear listas condicionales 

numbers_v3 = [element * 2 for element in range(1,11) if element % 2 == 0]
print(numbers_v3)


#Dicctionary comprehesion


# Al igual que las listas tambien se pueden generar diccionarios comprimidos

new_dicitonary = {}

for i in range(1,5):
    new_dicitonary[i] = i*2

    print(new_dicitonary)

dict_V2 = {i:i * 2 for i in range(1,5) }
print(dict_V2)

# Generar un diccionario a partir de una lista 

countries = ['col', 'pe', 'mex', 'bol']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

# Para hacer esto mismo en una sola linea se hace así: El país es la llave y el valor es el
# que se genera de manera aleatoria, luego se itera los paices.

population_V2 = {country : random.randint(1,100) for country in countries}
print(population_V2)

# otro ejemplo

names = ['Alejo', 'Santi', 'Leidy', 'José']
ages = [21,10,37, 39]

# Utlizamos la funcion zip para unir dos listas

print(list(zip(names,ages)))

new_dict = {name: age for (name,age) in zip(names,ages)}
print(new_dict)

# En el ejemplo anterior se tiene una clave valor las cuales son name y age respectivamente
# posteriormente se itera en una lista con tuplas la cual se forma gracias zip

# Los diccionarios pueden tener condiciones

result = {country : population for (country, population) in population_V2.items() 
          if population > 20}
print(result)

text = 'Hola, soy Alejandro'
unique = {c : c.upper() for c in text if c in 'aeiou'}
print(unique)

repeat = {c : c.count(c) for c in text if c in 'aeiou'}
print(repeat)
