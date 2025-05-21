from tkinter import *


class Comida():
    
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = StringVar(ventanaPrincipal)
        self.nombre = StringVar(ventanaPrincipal)
        self.ingrediente_principal = StringVar(ventanaPrincipal)
        self.calorias = StringVar(ventanaPrincipal)
        self.peso = StringVar(ventanaPrincipal)
        