from tkinter import *
import tkinter as tk
from controladores.comunicacion import Comunicacion
from controladores.validaciones import Validaciones
from modelos.libro import Libro
from .tabla import Tabla
from tkinter import messagebox

class Interfaz():

    def __init__(self):
        titulos = ['Id', 'Titulo', 'Autor', 'Genero', 'Año Publicacion']
        columnas = ['id', 'titulo', 'autor', 'genero', 'año_publicacion']
        data = []
        self.ventanaPrincipal = Tk()
        self.frameTabla = Frame(self.ventanaPrincipal)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.validaciones = Validaciones()
        self.tabla = Tabla(self.frameTabla, titulos, columnas, data)
        self.libro = Libro(self.ventanaPrincipal)

    def accion_guardar_boton(self, titulo, autor, genero, año_publicacion):
        resultado = self.comunicacion.guardar(titulo, autor, genero, año_publicacion)
        
        if resultado == 201:    
            self.accion_consultar_todo('', '', '', '')
            messagebox.showinfo("Guardado exitoso", "Se guardó el registro")
        else:   
            messagebox.showerror("Guardado fallido", "No se pudo guardar el registro")
        

    def accion_actualizar_boton(self, id, titulo, autor, genero, año_publicacion):
        resultado = self.comunicacion.actualizar(id, titulo, autor, genero, año_publicacion)
        if resultado == 200:
            self.accion_consultar_todo('', '', '', '')
            messagebox.showinfo("Datos actualizados", "Se actualizó el registro")
        else:
            messagebox.showerror("Actualización fallida", "No se pudo actualizar el registro")
    
    def accion_eliminar_boton(self, id):
        resultado = self.comunicacion.eliminar(id)
        if resultado == 204 or resultado == 200:
            messagebox.showinfo("Eliminación exitosa", "Se eliminó el registro")
            self.accion_consultar_todo('', '', '', '')         
        else:
            messagebox.showerror("No se pudo eliminar el registro", "No se pudo eliminar el registro")


    def accion_consultar_boton(self, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            self.tabla.refrescar([])
            data = [(resultado.get('id'),
                    resultado.get('titulo'),
                    resultado.get('autor'),
                    resultado.get('genero'),
                    resultado.get('año_publicacion'))]
            self.tabla.refrescar(data)
            messagebox.showinfo("Se encontró el registro", "Se encontró el registro")
        else:
            messagebox.showerror("No se encontró el registro", "No se encontró el registro")


    def accion_consultar_todo(self, titulo, autor, genero, año_publicacion):
        resultado = self.comunicacion.consultar_todo(titulo, autor, genero, año_publicacion)
        if isinstance(resultado, dict):
            resultado = [resultado]

        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('titulo'),
                elemento.get('autor'),
                elemento.get('genero'),
                elemento.get('año_publicacion')
            ))
    
        self.tabla.refrescar(data)
        


    def mostrar_interfaz(self):

        self.texto_validar_titulo = ""
        self.texto_validar_autor = ""
        self.texto_validar_genero = ""
        self.texto_validar_año = ""

        self.ventanaPrincipal.title("Interfaz Libros")
        self.ventanaPrincipal.config(bg='alice blue')
        self.ventanaPrincipal.geometry("1200x600")

        self.frame = Frame(self.ventanaPrincipal, width=600, height=500, bg="alice blue")
        self.frame.pack_propagate(False)
        self.frame.pack()

        self.frameTabla.pack()
        
        labelmensaje = Label(self.frame, text="Hola! Por favor ingresa los siguientes datos del libro:", font=("Times New Roman", 14, "bold"), bg= "alice blue", fg= "dark turquoise")
        labelmensaje.grid(row=0, column=0, columnspan=4, pady=5)
        
        labelid = Label(self.frame, text="id",bg='alice blue')
        labelid.grid(row=1, column=0,sticky='we')
        entryid = Entry(self.frame, textvariable= self.libro.id, width=30)
        entryid.grid(row=1, column=1, sticky='w')

        boton_consultar = Button(self.frame, text="Consultar", width=9,font=("Arial", 10, "bold"), bg="dark turquoise", fg="white",relief="flat", command=lambda: self.accion_consultar_boton(entryid.get()))
        boton_consultar.grid(row=1, column=2, pady=3, padx=5, sticky='we')

        labeltitulo =Label(self.frame, text="Título",bg='alice blue').grid(row=2, column=0,sticky='we')
        entrytitulo = Entry(self.frame, textvariable= self.libro.titulo,width=30)
        entrytitulo.grid(row=2, column=1,sticky='w')
        self.labelValidacionTitulo =Label(self.frame, text="",bg='alice blue')
        self.labelValidacionTitulo.grid(row=2, column=2, pady=2, columnspan=2)

        labelautor =Label(self.frame, text="Autor",bg='alice blue').grid(row=4, column=0,sticky='we')
        entryautor = Entry(self.frame, textvariable= self.libro.autor,width=30)
        entryautor.grid(row=4, column=1,sticky='w')
        self.labelValidacionAutor=Label(self.frame, text="",bg='alice blue')
        self.labelValidacionAutor.grid(row=4, column=2, columnspan=2, pady=2)

        labelgenero = Label(self.frame, text="Género",bg='alice blue').grid(row=6, column=0,sticky='we')
        entrygenero = Entry(self.frame, textvariable= self.libro.genero,width=30)
        entrygenero.grid(row=6, column=1,sticky='w')
        self.labelValidacionGenero =Label(self.frame, text="",bg='alice blue')
        self.labelValidacionGenero.grid(row=6, column=2, columnspan=2, pady=2)

        labelaño_publicacion = Label(self.frame, text="Año de Publicación",bg='alice blue').grid(row=8, column=0,sticky='we')
        entryaño_publicacion = Entry(self.frame, textvariable= self.libro.año_publicacion,width=30)
        entryaño_publicacion.grid(row=8, column=1,sticky='w')
        self.labelValidacionAño_Publicacion =Label(self.frame, text="",bg='alice blue')
        self.labelValidacionAño_Publicacion.grid(row=8, column=2, columnspan=2, pady=2)

        boton_guardar = Button(self.frame, text="Guardar",width=9,font=("Arial", 10, "bold"), bg="dark turquoise", fg="white",relief="flat",command=lambda: self.accion_guardar_boton(entrytitulo.get(), entryautor.get(), entrygenero.get(), entryaño_publicacion.get()))
        boton_guardar.grid(row=10, column=1, pady=3, padx=5, sticky="we")

        boton_actualizar = Button(self.frame, text="Actualizar", width=9,font=("Arial", 10, "bold"), bg="dark turquoise", fg="white",relief="flat", command=lambda: self.accion_actualizar_boton(entryid.get(), entrytitulo.get(), entryautor.get(), entrygenero.get(), entryaño_publicacion.get()))
        boton_actualizar.grid(row=11, column=1, pady=3, padx=5, sticky="we")

        boton_consultar_todo = Button(self.frame, text="Consultar todo", width=11,font=("Arial", 10, "bold"), bg="dark turquoise", fg="white",relief="flat",command=lambda: self.accion_consultar_todo('', '', '',''))
        boton_consultar_todo.grid(row=13, column=1, pady=3, padx=5, sticky="we")

        boton_eliminar = Button(self.frame, text="Eliminar", width=9,font=("Arial", 10, "bold"), bg="dark turquoise", fg="white",relief="flat", command=lambda: self.accion_eliminar_boton(entryid.get()))
        boton_eliminar.grid(row=12, column=1, pady=3, padx=5, sticky="we")

        self.tabla.tabla.grid(row=14, column=0, columnspan=4, pady=5, padx=5, sticky='nsew')

        def evento_presionar_tecla_titulo(event):
            if self.validaciones.validar_letras(self.libro.titulo):
                self.texto_validar_titulo = ""
            else:
                self.texto_validar_titulo = "Solo se permiten letras"
            self.labelValidacionTitulo.config(text=self.texto_validar_titulo, fg="dark turquoise")

        def evento_presionar_tecla_autor(event):
            if self.validaciones.validar_letras(self.libro.autor):
                self.texto_validar_autor = ""
            else:
                self.texto_validar_autor = "Solo se permiten letras"
            self.labelValidacionAutor.config(text=self.texto_validar_autor, fg="dark turquoise")

        def evento_presionar_tecla_genero(event):
            if self.validaciones.validar_letras(self.libro.genero):
                self.texto_validar_genero = ""
            else:
                self.texto_validar_genero = "Solo se permiten letras"
            self.labelValidacionGenero.config(text=self.texto_validar_genero, fg="dark turquoise")
        

        def evento_presionar_tecla_año(event):
            if self.validaciones.validar_numeros(self.libro.año_publicacion):
                self.texto_validar_año = ""
            else:
                self.texto_validar_año = "Solo se permiten numeros"
            self.labelValidacionAño_Publicacion.config(text=self.texto_validar_año, fg="dark turquoise")

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryid.delete(0, END)
                entryid.insert(0, str(valores[0]))
                entrytitulo.delete(0, END)
                entrytitulo.insert(0, str(valores[1]))
                entryautor.delete(0, END)
                entryautor.insert(0, str(valores[2]))
                entrygenero.delete(0, END)
                entrygenero.insert(0, str(valores[3]))
                entryaño_publicacion.delete(0, END)
                entryaño_publicacion.insert(0, int(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                id_eliminar = self.tabla.tabla.item(i)['values'][0]
                resultado = self.comunicacion.eliminar(id_eliminar)
                if resultado == 204 or resultado == 200:
                    print(f"Registro con ID {id_eliminar} eliminado correctamente.")
                    self.accion_consultar_todo('', '', '', '')
                else:
                    print(f"No se pudo eliminar el registro con ID {id_eliminar}.")


        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        entrytitulo.bind("<KeyRelease>", evento_presionar_tecla_titulo)
        entryautor.bind("<KeyRelease>", evento_presionar_tecla_autor)
        entrygenero.bind("<KeyRelease>", evento_presionar_tecla_genero)
        entryaño_publicacion.bind("<KeyRelease>", evento_presionar_tecla_año)

        self.ventanaPrincipal.mainloop()
