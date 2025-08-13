class Libros:
    def __init__(self, titulo, autor, publicacion, codigo):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.codigo = codigo

    def mostrar_libro(self):
        return f"Titulo:  {self.titulo} - Autor: {self.autor} - Publicacion: {self.publicacion} - Codigo: {self.codigo}"

class Trabajolibros:
    def __init__(self):
        self.lista_libros = []

    def agregar1(self):
        try:
            titulo=input("Ingrese el título del libro: ")
            autor=input("Ingrese el nombre del autor: ")
            publicacion=int(input("Ingrese el año de publicación: "))
            codigo=input("Ingrese el codigo unico del libro: ")
            self.lista_libros.append(Libros(titulo, autor, publicacion, codigo))
        except ValueError:
            print("El valor ingresado no es valido")
    def mostrar1(self):
        if not self.lista_libros:
            print("No hay libros registrados")
        else:
            print("\nLista de Libros registrados:")
            for i, datos in enumerate(self.lista_libros, start=1):
                print(f"{i}. {datos.mostrar_libro()}")
            print()
class Usuarios:
    def __init__(self, nombre, carnet,carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
    def mostrar_usuario(self):
        return f"Nombre: {self.nombre} - Carnet: {self.carnet} - Carrera: {self.carrera}"

class TrabajoUsuario:
    def __init__(self):
        self.lista_usuarios = []

    def agregar2(self):
        try:
            nombre=input("Ingrese el nombre: ")
            carnet=int(input("Ingrese el carnet: "))
            carrera=input("Ingrese el carrera: ")
            self.lista_usuarios.append(Usuarios(nombre,carnet,carrera))
        except ValueError:
            print("El valor ingresado no es valido")
    def mostrar2(self):
        if not self.lista_usuarios:
            print("No hay libros registrados")
        else:
            print("\nLista de usuarios registrados:")
            for i, datos in enumerate(self.lista_usuarios, start=1):
                print(f"{i}. {datos.mostrar_libro()}")
            print()

class Prestamos:
