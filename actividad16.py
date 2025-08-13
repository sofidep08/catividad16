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

    def agregar(self):
        try:
            titulo=input("Ingrese el título del libro: ")
            autor=input("Ingrese el nombre del autor: ")
            publicacion=int(input("Ingrese el año de publicación: "))
            codigo=input("Ingrese el codigo unico del libro: ")
            self.lista_libros.append(Libros(titulo, autor, publicacion, codigo))
        except ValueError:
            print("El valor ingresado no es valido")
    def mostrar(self):
        if not self.lista_libros:
            print("No hay libros registrados")
        else:
            print("\nLista de estudiantes:")
            for i, datos in enumerate(self.lista_libros, start=1):
                print(f"{i}. {datos.mostrar_libro()}")
            print()
class usuarios:
    def __init__(self, nombre, carnet,carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
    def mostrar_usuario(self):
        return f"Nombre: {self.nombre} - Carnet: {self.carnet} - Carrera: {self.carrera}"