# La función de un map es hacer transformaciones,
# ejecuta una función para cada uno de estos elementos y el elemento se envía a otra
# función como parametro y vamos a tener el mismo número de elementos que había en un principio

numbers = [1,2,3,4]

# Para hacer una transformación a esta listas existen dos maneras

numbers_V2 = []
for i in numbers:
    numbers_V2.append(i * 2)

print(numbers)
print(numbers_V2)

# Ahora usando el map

numbers_V3 = list(map(lambda i : i * 2, numbers))
print('version 3: ', numbers_V3)

# Los parametros del map son la función y los iterables
# Otro ejemplo de map

numbers1 = [1,2,3,4]
numbers2 = [5,6,7]

sum_numbers = list(map(lambda x,y : x + y, numbers1,numbers2))
print(sum_numbers)

# se puede usar diccionarios y map

items = [
    {
        'product': 'camisa',
        'price' : 100
},
{
    'product' : 'pantalones',
    'price' : 300

},
{
    'product' : 'pantalones 2',
    'price' : 200
}
]

# se busca obtener una lista solo de precios

prices = list(map(lambda item : item['price'],items))
print(prices)

# también se puede agregar nuevos elementos a los diccionarios

def add_taxes(item):
    item['taxes'] = item['price']*.19
    return item
new_items = list(map(add_taxes,items))
print(new_items)