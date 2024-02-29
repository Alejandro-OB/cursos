"""Funciones"""

def suma(a, b):

    ''' Funcion para sumar'''
    c= a + b
    print(c)

suma(8,5)
suma(10,90)

# Dentro de una función se puede tener otra función
# Las funciones pueden retornar un valor


def sum_with_range(a : int,b : int):
    '''Esta es mi función'''
    count = 0
    for x in range(a,b):
        count += x
    return count

print(sum_with_range(1,10))

# Las funciones pueden retornar varios valores no solamente uno

def find_volume(length : int , width : int, depth: int):

    '''Función para calcular el volumen'''
    return length * width * depth, width, 'Hola'

result, ancho, text = find_volume(10,6,7)
print(result)
print(ancho)
print(text)

#Lamda functions

#  Las funciones lambda son una forma más versatil de escribir funciones
# estas pueden ser almacenadas en variables
# se definen de la siguiente manera: se escribe la palabra lambda seguido a esta
# se colocan los parametros de entrada y después de dos puntos ':' los valores que 
# va a retornar

# Por ejemplo

# una función normal se escribiría así

def increment(x):
    return x+1

result = increment(10)
print(result)

# Ahora como lambda function se escribiría de esta manera

incrementV2 = lambda x: x + 1
print(incrementV2(20))

# Estas funciones también pueden recibir dos valores

full_name = lambda name, lastname: f'My fullname is {name.title()} {lastname.title()}'
result=full_name('alejandro', 'ortega benavides')
print(result)

# Existen funciones de orden superior, es decir, que pueden tener como parametro
# otras funciones

def high_order_function(x , func):
    return x + func(x)

result = high_order_function(2, increment)
print(result)

# se puede simplificar este ejercicio usando lambdas

incrementV3 = lambda x : x + 1
high_order_func = lambda x, func : x + func(x)
result = high_order_func(10,incrementV3)
print(result)