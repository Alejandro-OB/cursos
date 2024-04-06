"""
En Python, los módulos son archivos que contienen código Python reutilizable.
Estos módulos pueden incluir funciones, variables y clases que pueden ser importadas
y utilizadas en otros programas de Python.
Los módulos permiten organizar el código de una manera más estructurada y modular,
lo que facilita la reutilización y la mantenibilidad del código.
"""
# Algunos de los modulos de phyton son

import sys

#print(sys.path) # me da información sobre el sistema operativo

text = 'mi numero de celular es 3146044312 y mi numero favorito es el 15'

import re

result = re.findall('[0-9]+', text) # se usan las expresiones regulares oara obtener solo los datos que sean numeros
print(result)

import time
timestap = time.time()
print(timestap) # imprime la hora en formato unix 

# Para ver la hora en un formato lejible se hace así
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers) # Devuelve la frecuencia de un elemento particular en una lista
print(counter)

# un archivo .py también es un modulo y se puede imprtar desde otro 
# por ejemplo 

import mod
keys, values = mod.get_population()
print(keys,values)

country = input('Ingrese el pais => ')
data = [
    {
        'Country' : 'Colombia',
        'population': 300
},
{
    'Country' : 'Bolivia',
    'population' : 500

}]

print(mod.population_by_country(data,country))

