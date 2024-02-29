# Otra de las funciones más usadas en phyton es reduce el cual reduce los elementos de una 
# lista a un solo valor
# Para usar reduce se debe importarlo

import functools

numbers = [1,2,3,4]

def accum(counter,item):
    print('counter ',counter)
    print('item ',item)
    return counter + item

result = functools.reduce(accum,numbers)
print(result)