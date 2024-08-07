class Vehiculo:
    def __init__(self,marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponibilidad = True

    def vender(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El vehículo {self.marca} se ha vendido")
        else: 
            print("El vehiculo no está disponible") 

    def revisar_disponibilidad(self):
        return self.disponibilidad
    
    def obtener_precio(self):
        return self.precio
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
class Carro(Vehiculo):
    def start_engine(self):
        if not self.disponibilidad:
            return f"El motor del coche {self.marca} está en marcha"
        else:
            return f"El coche con la marca {self.marca} no está disponible"
            
    def stop_engine(self):
            if self.disponibilidad:
                return f"El motor del coche {self.marca} se ha detenido"   
            else:
                return f"El coche con la marca {self.marca} no está disponible"    
    
class Bicicleta(Vehiculo):
        def start_engine(self):
            if not self.disponibilidad:
                return f"La bicicleta {self.marca} está en marcha"
            else:
                return f"La bicicleta {self.marca} no está disponible"
            
        def stop_engine(self):
            if self.disponibilidad:
                return f"La bicicleta {self.marca} se ha detenido"   
            else:
                return f"La bicicleta {self.marca} no está disponible"    
            
class Camion(Vehiculo):
        def start_engine(self):
            if not self.disponibilidad:
                return f"El motor del camion {self.marca} está en marcha"
            else:
                return f"El camion con la marca {self.marca} no está disponible"
            
        def stop_engine(self):
            if self.disponibilidad:
                return f"El motor del camion {self.marca} se ha detenido"   
            else:
                return f"El camion con la marca {self.marca} no está disponible"    

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []
    
    def comprar_vehiculo(self, vehiculo:Vehiculo):
        if vehiculo.revisar_disponibilidad():
            vehiculo.disponibilidad = False
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)   
        else:
            print(f"El vehiculo de la marca {vehiculo.marca} no está disponible")

    def consultar_disponibilidad(self, vehiculo:Vehiculo):
        if vehiculo.revisar_disponibilidad():
            disponbilidad
        