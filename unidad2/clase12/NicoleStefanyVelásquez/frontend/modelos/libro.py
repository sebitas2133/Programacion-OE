from tkinter import *

class Libro():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.titulo = StringVar(ventanaPrincipal)
        self.autor = StringVar(ventanaPrincipal)
        self.genero = StringVar(ventanaPrincipal)
        self.año_publicacion = StringVar(ventanaPrincipal)
        self.id = StringVar(ventanaPrincipal)