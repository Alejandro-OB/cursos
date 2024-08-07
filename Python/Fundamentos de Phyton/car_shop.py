class Carro:
    def __init__(self, marca,modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.diponibilidad = True
    
    def vender(self):
        if self.diponibilidad:
            self.diponibilidad = False
            print(f"El coche marca {self.marca} {self.modelo} se ha vendido")
        else:
            print(f"El coche marca {self.marca} {self.modelo} no está disponible")

    def revisar_disponibilidad(self):
        return self.diponibilidad
    
    def obtener_precio(self):
        return self.precio
    
class Clientes:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_comprados = []

    def comprar_carro(self,carro):
        if carro.revisar_disponibilidad():
            carro.vender()
            self.carros_comprados.append(carro)
        else:
            print(f"Lo sentimos, el auto no está disponible en este momento")

    def consultar_carro(self, carro):
        disponibilidad = "disponible" if carro.revisar_disponibilidad() else "no dispoible"
        print(f"El carro {carro.marca} {carro.modelo} está {disponibilidad} y cuesta {carro.precio}")

class Consecionario:
    def __init__(self):
        self.inventario = []
        self.clientes   = []
    
    def agregar_carro(self, carro):
        self.inventario.append(carro)
        print(f"El coche marca {carro.marca} {carro.modelo} se ha registrado")
    
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El coche marca {cliente.nombre} se ha registrado")

    def mostrar_disponibilidad(self):
        print("Coches disponibles")
        for carro in self.inventario:
            if carro.revisar_disponibilidad():
                print(f"- {carro.marca} por {carro.precio}")
        
#instanciar carros

carro1 = Carro("Toyota", "Coralla", 29000)
carro2 = Carro("Honda","Accord", 38000)
carro3 = Carro("Ford", "Mustang", 55000)

#instanciar cliente
cliente = Clientes("Juan")
#instanciar tienda

consecionario= Consecionario()
consecionario.agregar_carro(carro1)
consecionario.agregar_carro(carro2)
consecionario.agregar_carro(carro3)
consecionario.registrar_cliente(cliente)

#mostrar coches disponibles
consecionario.mostrar_disponibilidad()

#cliente consulta un coche
cliente.consultar_carro(carro1)

#cliente compra coche
cliente.comprar_carro(carro2)


#mostrar coches disponibles
consecionario.mostrar_disponibilidad()
