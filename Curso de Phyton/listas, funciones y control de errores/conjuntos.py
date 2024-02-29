"""Conjuntos"""

# Los conjutos no tienen un orden, se pueden editar y no tienen duplicados

set_countries = {'Col', 'Mex', 'Bol'}
print(type(set_countries))

# Es posible convertir otros elementos a conjuntos, como listas, strings etc

numbers = [1,2,1,3,3,4]

set_from_numbers = set(numbers)
print(set_from_numbers)

unique_numbers = list(set_from_numbers)
print(unique_numbers)

# Para añadir un elemento a un conjunto se usa .add() el parametro es el elemento a agregar

set_countries.add('pe')
print(set_countries)

# Para actualizar los elementos se puede usar update

set_countries.update({'Arg', 'Ecu'})
print(set_countries)

# Eliminar un elemento y descartarlo

set_countries.remove('pe')
print(set_countries)

set_countries.discard('ar')
print(set_countries)

#"""Operaciones entre conjuntos"""

# Union

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
print(set_c)

print(set_a | set_b)

# Intercepcion

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# diferencia

print(set_a.difference(set_b))
print(set_a - set_b)

# diferencia simétrica

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
