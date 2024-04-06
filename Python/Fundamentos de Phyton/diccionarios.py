"""Declaración de diccionarios"""
person = {

    'name' : 'Alejandro',
    'last_name' : 'Ortega',
    'langs' : ['Phyton', 'Java'],
    'age' : 21
}

person['name'] = 'José'
person['age'] -= 1
person['langs'].append('Rust')

# Eliminación de elementos, se hace mediante la llave

del person['last_name']
person.pop('age')

print(person)

# Se puede obtener los items, claves y valores dentro de un diccionario

print('Items')
print(person.items())

print('Keys')
print(person.keys())

print('Values')
print(person.values())
