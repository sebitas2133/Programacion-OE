from tkinter import *

class Libros():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.titulo = StringVar(ventanaPrincipal)
        self.autor = StringVar(ventanaPrincipal)
        self.genero = StringVar(ventanaPrincipal)
        self.paginas = StringVar(ventanaPrincipal)
        self.año_publicacion = StringVar(ventanaPrincipal)
        self.id = StringVar(ventanaPrincipal)