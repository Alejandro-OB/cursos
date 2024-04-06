""" En phyton puede ocurrir un error al comparar flotantes por ejemplo """

X = 3.3
Y= 2.2 + 1.1
print(Y)
print( X == Y)

# En este caso aunque "y" tiene el valor de 3.3 va a tener más decimales que lo haran
# diferente a 3.3

# para solucionar esto se puede hacer así

Y_str = format(Y, ".2g") #se establece el formato de la variable Y a string con dos decimales
print(Y_str)
print(Y_str == str(X))

#Condicionales

pet = input("Cuál es tu mascota favorita? ")

if pet == 'perro':
    print("Genial, tienes buen gusto")
elif pet == 'gato':
    print(" Espero tengas suerte")
elif pet == 'pez':
    print ("Eres los maximo")
else:
    print("No tienes ninguna mascota interesante")

# Como saber si un número es par e impar
number = int(input("Ingresa el número para verificar si es par o no: "))

if number % 2 == 0:
    print(f"El número {number} es par")
else:
    print(f"El numero {number} es impar")

# El operador in nos permite buscar un subtexto dentro de otro texto

TEXT = 'A mi me gusta escuchar música'
print('música' in TEXT) # Arroja True debido a que "música" si se encuentra dentro del texto

# El método len() permite saber los caracteres de un string

SIZE = len('amor')
print(SIZE)
