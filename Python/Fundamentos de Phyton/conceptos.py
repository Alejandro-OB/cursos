##comandos para listas

##len: Longitud de la cadena
new_list = ["uno", 2, 3.14, [1,2,3]]
print(len(new_list))
print(new_list)

##obtener elementos
'''para obtener algún elemento de la lista se debe escribir el nombre de la lista y entre
    corchetes se escribe el index del elemento que se desea obtener
'''
print(new_list[0])

##slicing
'''
    permite obtener un rango de elementos de una lista
'''
print(new_list[:3])

##añadir un nuevo elemento a la lista
'''
 se hace mediante el metodo append, este metodo añade un elemento al final de la lista
'''
new_list.append(False)
print(new_list)

'''
    para agregar un elemento a una posicion especifica de la lista se hace mediante el 
    metodo insert
'''
new_list.insert(1,"nuevo")
print(new_list)

##eliminar elementos de la lista

'''
    se hace mediante el metodo del y se le debe pasar la posicion del elemento a eliminar
'''

del new_list[1]
print(new_list)

'''
    para eliminar la lista se hace así
'''
del new_list
#print(new_list)

## listas de dos dimensiones

'''
 se definen con varias listas dentro de una lista
'''
matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
print(matrix[0][1])

## tuplas

'''
    las tuplas son un tipo de colecciones que son inmutables, es decir, no se pueden modificar
'''

new_tuple = (1,2,4,5)
print(new_tuple)

## diccionarios

''' 
    son colecciones que contienes dos elementos, la clave (key), y el valor (value)
'''

new_dictionary = { 1: "uno", 2:"dos", 3:"tres"}

'''
 para obtener los valores del diccionario se hace mediante la clave
'''

print(new_dictionary[3])

'''
    para eliminar un elemento de un diccionario tambien se puede hacer mediante el 
    metodo del y se le pasa la clave del diccionario
'''
print(new_dictionary)
del new_dictionary[1]
print(new_dictionary)

'''
    se puede obtener tanto los valores, claves, y pares de un diccionario
'''
information = {
        'nombre':'Jose',
        'apellido': 'Ortega',
        'numero': '3127202879',
    }

valores = information.values()
print(valores)

claves = information.keys()
print(claves)

pares = information.items()
print(pares)

contacts = {
    'Jose':{
        'nombre':'Jose',
        'apellido': 'Ortega',
        'numero': '3127202879'
    },
    'Leidy':{
        'nombre':'Leidy',
        'apellido': 'Benavides',
        'numero': '3146095128'
    }
}

print(contacts['Jose'])

# iteradores

'''
    El ciclo for se usa para iterar en colecciones como listas, o diccionarios.
    entre otros, para usar el ciclo for se hace de la siguiente manera: 
    for i in elements: en este caso, "i" es la variable donde se va a almacenar el elemento
    que se ha encontrado actualmente.
'''

elements = [1,2,3,4,5]

for element in elements:
    print(element)

'''
    se puede generar numeros en un rango con el metodo range en el cual si se pasa un solo
    parametro indica que este es el limite máximo e inicia desde 0. si se desea que inicie 
    desde otro valor se debe hacer de la siguiente manera: range(1,4) aqui se crea un rango del 
    1 al 2
'''

for i in range(1,3):
    print("valor de i en el rango: ",i)

'''
    las palabras reservadas break y continue permiten interrumpir el flujo de codigo,
    break ocasiona que el codigo no se siga ejecutando, es decir, que la ejecución termine
    y continue hace que el codigo se siga ejecutando sin tener en cuenta la accion actual
'''

for element in elements:
    if element == 3:
        print('se usa continue')
        continue
    print(element)

for element in elements:
    if element == 3:
        print('se usa break')
        break
    print(element)
    
#iteradores y generadores

'''
    los iteradores son metodos que permiten recorrer una coleccion con ayuda de los metodos
    iter y next, el iter crea el iterador y el next permite obtener la posicion siguiente del
    iterador
'''

print('EJEMPLO ITER\n')

text = 'you only live once'
my_iter = iter(text)

for char in my_iter:
    print(char)

'''
    el generador es una funcion que se debe definir y devuelve ciertos valores gracias
    al metodo yield
'''

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print('EJEMPLO GENERADOR\n')
for number in my_generator():
    print(number) 

print('EJEMPLO Par\n')

def generador_pares(limite):
    n = 0
    while n <= limite:
        yield n
        n += 2

# Ejemplo de uso
limite = 10
pares = generador_pares(limite)
for par in pares:
    print(par)

print('EJEMPLO Impar\n')

def generador_impares(limite):
    n = 1
    while n <= limite:
        yield n
        n += 2

# Ejemplo de uso
limite = 10
impares = generador_impares(limite)
for impar in impares:
    print(impar)


#lambda functions
'''
    son funciones anónimas y rápidas que puedes usar cuando necesitas una función pequeña
    sitaxis: lambda argumentos: expresión
    Ejemplo
'''

doble = lambda x: x * 2
print(doble(5))  
numbers = range(11)
even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

#recursividad 
'''
    La recursividad es una técnica de programación en la que una función se llama a sí misma
    para resolver un problema.
'''