"""Listas y Tuplas en phyton"""

# Para declarar una lista en Phyton es tan fácil como escribir el contenido de la
# lista dentro de corchetes

numbers = [1,2,3,4]

print(type(numbers))

numbers[0] = 5 # Forma de actualizar una posición en una lista
print(numbers)

# Para agregar elementos al final de las listas se usa append
numbers.append(700)
print(numbers)

# El metodo insert tambien se usa para agregar elementos a una lista, en este metodo es 
# necesario pasar dos para metros que son la posicion y el elemento
numbers.insert(3,'hola')
print(numbers)

# Es psoble fusionar los elementos de dos listas

strings = ['como', 'estas', 'tu']

fusion = numbers + strings

print(fusion)

# .index() obtiene el identificador de una lista

index = fusion.index('tu')
print(index)

# .remove() elimina un elemto de una lista
strings.remove('estas')
print(strings)

# pop() si no tiene parametro elimina el ultimo elemento de la lista
# pero con un parametro elimina el elemento de esa posición

numbers.pop(2)
print(numbers)

# clear() limpia una lista

fusion.clear()
print(fusion)
