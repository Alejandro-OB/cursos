class Libro:
    def __init__(self, titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True   
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"el libro {self.titulo} ha sido prestado\n")
        else:
            self.disponible = False
            print("El libro no está disponible\n")
    
    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto\n")

class Usuario:
    def __init__(self,nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    
    def Prestar_Libro(self, Libro):
        if Libro.disponible:
            Libro.prestar()
            self.libros_prestados.append(Libro)
        else:
            print(f"El libro {Libro.titulo} no está disponible")

    def Regresar_Libro(self, Libro):
        if Libro in self.libros_prestados:
            Libro.devolver()
            self.libros_prestados.remove(Libro)
            #print(f"El libro {Libro.titulo} ha sido regresado")
        else:
            print(f"El libro {Libro.titulo} no está en la lista de libros prestados")

class Libreria:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def añadir_libros (self, Libro):
        self.libros.append(Libro)
        print(f"El libro {Libro.titulo} ha sido agregado\n")
    
    def registrar_usuarios (self, Usuario):
        self.usuarios.append(Usuario)
        print(f"El usuario {Usuario.nombre} ha sido registrado\n")
    
    def mostrar_libros_disponibles (self):
        print(f"Libros disponibles")
        for Libro in self.libros:
            if Libro.disponible:
                print(f"{Libro.titulo} por {Libro.autor}\n")


libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez")
libro2 = Libro("En Agosto nos vemos", "Gabriel Garcia Marquez")

usuario1 = Usuario("Alejandro",1004415163)

biblioteca = Libreria()
biblioteca.añadir_libros(libro1)
biblioteca.añadir_libros(libro2)
biblioteca.registrar_usuarios(usuario1)


biblioteca.mostrar_libros_disponibles()

usuario1.Prestar_Libro(libro1)
#usuario1.Prestar_Libro(libro2)

biblioteca.mostrar_libros_disponibles()

usuario1.Regresar_Libro(libro1)

biblioteca.mostrar_libros_disponibles()