
"""Anotaciones sobre phyton"""

# En phyton se puede hacer operaciones dentro de
# un print
print(7+5)

# Las variables en phyton se declaran sin ningun identificador
MY_NAME = "Alejandro"
print(MY_NAME)

# Para pedir texto por consola se utiliza imput

MY_NAME = input("Cuál es tu nombre?")
print("usando input el valor de la variable es: ",MY_NAME)
LAST_NAME = "Ortega"
AGE = 21

# Se puede concatenar variables de tres maneras diferentes:

TEMPLATE = "Hola mi nombre es " + MY_NAME + " mi apellido es " + LAST_NAME
print("V1", TEMPLATE)

TEMPLATE = "Hola mi nombre es {} y mi apellido es {} ".format( MY_NAME ,LAST_NAME)
print("V2", TEMPLATE)

TEMPLATE = f"Hola, mi nombre es {MY_NAME} y mi apellido es {LAST_NAME}"
print("V3", TEMPLATE)

# Para incrementar o decremetar un valor se hace así:

LIVES = 10

LIVES -= 5
LIVES += 3
print(LIVES)

# Para hacer transformaciones de tipo de datos se hace así

MY_AGE = input("Cual es tu edad ")
MY_AGE = int(MY_AGE)
MY_AGE += 10
print(f'Tu edad en 10 años será: {MY_AGE}')
