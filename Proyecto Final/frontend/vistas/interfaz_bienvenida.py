from tkinter import *
from vistas.interfaz_autores import Interfaz_autores
from vistas.interfaz_libros import Interfaz_libros


class Interfaz_bienvenida():

    def __init__(self): 
        self.ventanaPrincipal = Tk()
        self.frameTabla = Frame(self.ventanaPrincipal) 
        self.frame_contenido = Frame(self.ventanaPrincipal, width=90, bg="alice blue")
        self.autores = Interfaz_autores(self.frame_contenido)
        self.libros = Interfaz_libros(self.frame_contenido)

    def mostrar_mensaje_guardando(self):

        self.label_guardando.config(text="Guardando...")
        self.ventanaPrincipal.after(2000, lambda: self.label_guardando.config(text=""))
        self.ventanaPrincipal.after(59000, self.mostrar_mensaje_guardando)

    def mostrar_bienvenida(self):

        def frame_borrar_contenido():
            for widget in self.frame_contenido.winfo_children():
                widget.destroy()
        
        self.ventanaPrincipal.title("Gestión de Autores y Libros")
        self.ventanaPrincipal.geometry("1380x680")

        self.frame_opciones = Frame(self.ventanaPrincipal, bg="pale turquoise", width=90)
        self.frame_opciones.pack(side=LEFT, fill=Y)

        self.frame_contenido = Frame(self.ventanaPrincipal, width=90, bg="alice blue")
        self.frame_contenido.pack(side=RIGHT, fill=BOTH, expand=True)

        label_bienvenida = Label(self.frame_contenido, text="¡Bienvenid@, elige la opción \nque deseas registrar!", bg="alice blue", fg="turquoise4", font=("Arial", 25, "bold"))
        label_bienvenida.pack(pady=190)

        boton_autores = Button(self.frame_opciones, text="Autores", width=13, height=2, bg="turquoise4", fg="white", font=("Arial", 10,"bold"), border=0,command=lambda: self.autores.mostrar_autores(self.frame_contenido, frame_borrar_contenido))
        boton_autores.grid(row=0, column=0, pady=5, padx=5)

        boton_libros = Button(self.frame_opciones, text="Libros", width=13, height=2, bg="turquoise4", fg="white", font=("Arial", 10,"bold"), border=0, command=lambda: self.libros.mostrar_libros(self.frame_contenido, frame_borrar_contenido))
        boton_libros.grid(row=1, column=0, pady=5, padx=5)

        self.label_guardando = Label(self.frame_opciones, text="", bg="pale turquoise", fg="turquoise4", font=("Arial", 10, "italic"))
        self.label_guardando.grid(row=2, column=0, pady=542, sticky="s")
       
        self.mostrar_mensaje_guardando()
