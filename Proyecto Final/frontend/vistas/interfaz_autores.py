from tkinter import *
import tkinter as tk
from controladores.comunicaciones_autores import Comunicacion_autores
from controladores.validaciones import Validaciones
from modelos.autores import Autores
from .tabla import Tabla
from tkinter import messagebox

class Interfaz_autores():


    def __init__(self, frame_conteido):
        self.comunicaciones_autores = Comunicacion_autores(frame_conteido)
        self.validaciones = Validaciones()
        self.autores = Autores(frame_conteido)
    
   
    def accion_registrar_boton(self, nombre, nacionalidad, edad):
        resultado = self.comunicaciones_autores.registrar(nombre, nacionalidad, edad)
        if resultado == 201:    
            self.accion_consultar_todo('', '', '')
            messagebox.showinfo("Guardado exitoso", "Se guardó el registro")
        else:   
            messagebox.showerror("Guardado fallido", "No se pudo guardar el registro")
        

    def accion_actualizar_boton(self, id, nombre, nacionalidad, edad):
        resultado = self.comunicaciones_autores.actualizar(id, nombre, nacionalidad, edad)
        if resultado == 200:
            self.accion_consultar_todo('', '', '')
            messagebox.showinfo("Datos actualizados", "Se actualizó el registro")
        else:
            messagebox.showerror("Actualización fallida", "No se pudo actualizar el registro")
    
    def accion_eliminar_boton(self, id):
        resultado = self.comunicaciones_autores.eliminar(id)
        if resultado == 204 or resultado == 200:
            messagebox.showinfo("Eliminación exitosa", "Se eliminó el registro")
            self.accion_consultar_todo('', '', '')         
        else:
            messagebox.showerror("No se pudo eliminar el registro", "No se pudo eliminar el registro")


    def accion_consultar_todo(self, nombre, nacionalidad, edad):
        resultado = self.comunicaciones_autores.registros_existentes(nombre, nacionalidad, edad)
        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('nombre'),
                elemento.get('nacionalidad'),
                elemento.get('edad')
            ))
    
        self.tabla.refrescar(data)
        

    def mostrar_autores(self, frame_contenido, frame_borrar_contenido):
        frame_borrar_contenido()
    
        self.texto_validar_nombre = ""
        self.texto_validar_nacionalidad = ""
        self.texto_validar_edad = ""

        self.frame_autores = Frame(frame_contenido, bg="alice blue")
        self.frame_autores.pack()

        label_seccion_autores = Label(self.frame_autores, text="REGISTRO DE AUTORES", bg="alice blue",fg="turquoise4", font=("Arial", 16,"bold"))
        label_seccion_autores.grid(row=0, column=0, columnspan=2, pady=15)

        labelid = Label(self.frame_autores, text="id",bg='alice blue')
        labelid.grid(row=1, column=0, pady=5)
        entryid = Entry(self.frame_autores, textvariable= self.autores.id, width=30)
        entryid.grid(row=1, column=1, pady=5)

        
        label_nombre = Label(self.frame_autores, text="Nombre", bg="alice blue", fg="black")
        label_nombre.grid(row=2, column=0, pady=5)
        entry_nombre = Entry(self.frame_autores, width=30, textvariable=self.autores.nombre)
        entry_nombre.grid(row=2, column=1, pady=5)
        self.label_error_nombre = Label(self.frame_autores, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_nombre.grid(row=2, column=2, pady=5)

        
        label_nacionalidad = Label(self.frame_autores, text="Nacionalidad", bg="alice blue", fg="black")
        label_nacionalidad.grid(row=4, column=0, pady=5)
        entry_nacionalidad = Entry(self.frame_autores, width=30, textvariable=self.autores.nacionalidad)
        entry_nacionalidad.grid(row=4, column=1, pady=5)
        self.label_error_nacionalidad = Label(self.frame_autores, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_nacionalidad.grid(row=4, column=2, pady=5)

        
        label_edad = Label(self.frame_autores, text="Edad", bg="alice blue", fg="black")
        label_edad.grid(row=6, column=0, pady=5)
        entry_edad = Entry(self.frame_autores, width=30, textvariable=self.autores.edad)
        entry_edad.grid(row=6, column=1, pady=5)
        self.label_error_edad = Label(self.frame_autores, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_edad.grid(row=6, column=2, pady=5)

        boton_guardar_autor = Button(self.frame_autores, text="Registrar", width=17, height=1, border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat", command=lambda: self.accion_registrar_boton(entry_nombre.get(), entry_nacionalidad.get(), entry_edad.get()))
        boton_guardar_autor.grid(row=8, column=0, pady=5)

        boton_registros_autor = Button(self.frame_autores, text="Registros Existentes", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat", command=lambda: self.accion_consultar_todo(entry_nombre.get(), entry_nacionalidad.get(), entry_edad.get()))
        boton_registros_autor.grid(row=8, column=1, pady=5)

        boton_eliminar_autor = Button(self.frame_autores, text="Eliminar", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat", command=lambda: self.accion_eliminar_boton(entryid.get()))
        boton_eliminar_autor.grid(row=9, column=0, pady=5)

        boton_actualizar_autor = Button(self.frame_autores, text="Actualizar", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat", command=lambda: self.accion_actualizar_boton(entryid.get(), entry_nombre.get(), entry_nacionalidad.get(), entry_edad.get()))
        boton_actualizar_autor.grid(row=9, column=1, pady=5)
    
        titulos = ['Id', 'Nombre', 'Nacionalidad', 'Edad']
        columnas = ['id', 'nombre', 'nacionalidad', 'edad']
        data = []
        self.frameTabla = Frame(frame_contenido, bg="alice blue")
        self.tabla = Tabla(self.frameTabla, titulos, columnas, data)
        self.frameTabla.pack()
        self.tabla.tabla.pack()
                
        def evento_validar_nombre(event):
            if self.validaciones.validar_letras(self.autores.nombre):
                self.texto_validar_nombre = ""
            else:
                self.texto_validar_nombre = "Solo se permiten letras"
            self.label_error_nombre.config(text=self.texto_validar_nombre, fg="dark turquoise")

        def evento_validar_nacionalidad(event):
            if self.validaciones.validar_letras(self.autores.nacionalidad):
                self.texto_validar_nacionalidad = ""
            else:
                self.texto_validar_nacionalidad = "Solo se permiten letras"
            self.label_error_nacionalidad.config(text=self.texto_validar_nacionalidad, fg="dark turquoise")

        def evento_validar_edad(event):
            if self.validaciones.validar_numeros(self.autores.edad):
                self.texto_validar_edad = ""
            else:
                self.texto_validar_edad = "Solo se permiten numeros"
            self.label_error_edad.config(text=self.texto_validar_edad, fg="dark turquoise")

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryid.delete(0, END)
                entryid.insert(0, str(valores[0]))
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, str(valores[1]))
                entry_nacionalidad.delete(0, END)
                entry_nacionalidad.insert(0, str(valores[2]))
                entry_edad.delete(0, END)
                entry_edad.insert(0, int(valores[3]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                id_eliminar = self.tabla.tabla.item(i)['values'][0]
                resultado = self.comunicaciones_autores.eliminar(id_eliminar)
                if resultado == 204 or resultado == 200:
                    print(f"Registro con ID {id_eliminar} eliminado correctamente.")
                    self.accion_consultar_todo('', '', '', '')
                else:
                    print(f"No se pudo eliminar el registro con ID {id_eliminar}.")

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        entry_nombre.bind("<KeyRelease>", evento_validar_nombre)
        entry_nacionalidad.bind("<KeyRelease>", evento_validar_nacionalidad)
        entry_edad.bind("<KeyRelease>", evento_validar_edad)

    

