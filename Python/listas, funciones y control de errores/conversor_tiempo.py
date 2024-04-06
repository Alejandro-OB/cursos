def convertir_a_minutos(minutos, segundos):
    return minutos + segundos / 60

cantidad_tiempos = int(input("Ingrese la cantidad de tiempos a sumar: "))

tiempos_totales = 0

for i in range(cantidad_tiempos):
    minutos = int(input(f"Ingrese los minutos del tiempo {i+1}: "))
    segundos = int(input(f"Ingrese los segundos del tiempo {i+1}: "))
    tiempos_totales += convertir_a_minutos(minutos, segundos)

# Obtener la parte entera de los minutos
minutos_enteros = int(tiempos_totales)

# Obtener la parte decimal y convertirla a segundos
segundos_decimal = (tiempos_totales - minutos_enteros) * 60

print(f"El tiempo total es: {minutos_enteros} minutos y {segundos_decimal:.0f} segundos")

