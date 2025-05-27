from tkinter import *

class Autores():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.nombre = StringVar(ventanaPrincipal)
        self.nacionalidad = StringVar(ventanaPrincipal)
        self.edad = StringVar(ventanaPrincipal)
        self.id = StringVar(ventanaPrincipal)