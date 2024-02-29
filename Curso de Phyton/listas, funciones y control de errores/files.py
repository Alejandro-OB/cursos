# Se puede acceder a un archivo o leerlo en phyton mediante el metodo read
# sin embargo, este metodo tiene un gran consumo de memoria por tal razon simpre se debe
# cerrar con un close

"""
file = open('./text.txt')
print(file.read())
file.close()
"""

# una manera de evitar el alto consumo de memoria es utilizando una lectura linea por linea
# que se puede hacer mediante un for

"""
for line in file:
    print(line)
file.close()
"""
# para evitar estar cerrando el archivo se puede utilizar la estructura with
# asi como se puede leer un arcivo tambien se puede escribir, para esto, se debe
# dar permisos de lectura y escritura para que no se sobreescriba el archivo

with open('./text.txt','r+') as file:
    for line in file:
        print(line)
    file.write('una nueva linea') 

