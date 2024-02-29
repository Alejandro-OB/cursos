# Al igual que el for hay otro tipo de iteradores que son casi manuales, es decir
# iteran entre un rango a medida que tu le das la orden

my_iter = iter(range(1,4))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# no se debe superar el limite superior del rango ya que va a generar una exception     