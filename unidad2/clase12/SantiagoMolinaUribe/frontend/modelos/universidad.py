from tkinter import *


class Universidad():
    
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = StringVar(ventanaPrincipal)
        self.edificio1 = StringVar(ventanaPrincipal)
        self.edificio2 = StringVar(ventanaPrincipal)
        self.edificio3 = StringVar(ventanaPrincipal)
        self.edificio4 = StringVar(ventanaPrincipal)