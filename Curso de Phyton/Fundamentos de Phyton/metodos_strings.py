"""Existen varios metodos que se pueden usar en los strings como los siguientes"""

# El metodo .upper() coloca todos los caracteres en mayuscula
# El metodo .lower() coloca todos los caracteres en minuscula

TEXT = 'Yo quiero ser un experto en Backend'

print(TEXT.upper())
print(TEXT.lower())

# Es posible contar cuantas veces aparece un caracter dentro de un texto con .count()

print(TEXT.count('a'))

# El metodo swapcase permite intercambiar entre mayusculas y minusculas dentro de una cadena

print(TEXT.swapcase())

# El metodo startswith permite saber si un texto inicia con una palabra

print(TEXT.startswith('Yo'))

# El metodo endswith permite saber si un texto termina con una palabra

print(TEXT.endswith('Backend'))

# El metodo replace() remplaza dos palabras

print(TEXT.replace('Yo', 'Tu'))

# tittle() coloca en mayuscula la primera letra de cada palabra en un texto

print(TEXT.title())

# isdigit verifica si un texto es un digito

print('98'.isdigit())
