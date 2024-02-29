
"""Indexing y slicing"""

# Indexing son los identificadores de las posiciones en las que se encuentran
# los caracteres

TEXT = 'Ella sabe Python'
print(TEXT[3])

# Para obtener la ultima posición del texto se puede calcular el tamaño del texto -1

SIZE = len(TEXT) - 1
print(TEXT[SIZE])

# Otra forma más útil de saber el último caracter o la posición se puede hacer
# utilizando el identificador -1

print(TEXT[-1])

# Slicing es obtener un rango de caracteres

print(TEXT[:4])

# También se puede dar saltos en un intervalo

print(TEXT[10:16:2]) # el ultimo valor son los saltos
