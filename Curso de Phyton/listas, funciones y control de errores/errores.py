# existe una manera de impedir que cuando se presente un error todo el sistema deje de 
# funcionar, y esto es mediante un try catch

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
    print('no se puede dividir entre 0')