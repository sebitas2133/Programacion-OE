from tkinter import *
from controladores.comunicaciones_libros import Comunicacion_libros
from controladores.validaciones import Validaciones
from modelos.libros import Libros
from .tabla import Tabla
from tkinter import messagebox

class Interfaz_libros():

    def __init__(self, frame_contenido):
        self.comunicaciones_libros = Comunicacion_libros(frame_contenido)
        self.validaciones = Validaciones()
        self.libros = Libros(frame_contenido)
        
   
    def accion_registrar_boton(self, titulo, autor, genero, paginas, año_publicacion):
        resultado = self.comunicaciones_libros.registrar(titulo, autor, genero, paginas, año_publicacion)
        if resultado == 201:    
            self.accion_consultar_todo('', '', '', '', '')
            messagebox.showinfo("Guardado exitoso", "Se guardó el registro")
        else:   
            messagebox.showerror("Guardado fallido", "No se pudo guardar el registro")
        

    def accion_actualizar_boton(self, id, titulo, autor, genero, paginas, año_publicacion):
        resultado = self.comunicaciones_libros.actualizar(id, titulo, autor, genero, paginas, año_publicacion)
        if resultado == 200:
            self.accion_consultar_todo('', '', '', '', '')
            messagebox.showinfo("Datos actualizados", "Se actualizó el registro")
        else:
            messagebox.showerror("Actualización fallida", "No se pudo actualizar el registro")
    
    def accion_eliminar_boton(self, id):
        resultado = self.comunicaciones_libros.eliminar(id)
        if resultado == 204 or resultado == 200:
            messagebox.showinfo("Eliminación exitosa", "Se eliminó el registro")
            self.accion_consultar_todo('', '', '', '', '')         
        else:
            messagebox.showerror("No se pudo eliminar el registro", "No se pudo eliminar el registro")


    def accion_consultar_todo(self, titulo, autor, genero, paginas, año_publicacion):
        resultado = self.comunicaciones_libros.registros_existentes(titulo, autor, genero, paginas, año_publicacion)
        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('titulo'),
                elemento.get('autor'),
                elemento.get('genero'),
                elemento.get('paginas'),
                elemento.get('año_publicacion')
            ))
    
        self.tabla.refrescar(data)

    def mostrar_libros(self, frame_contenido, frame_borrar_contenido):
        frame_borrar_contenido()

        self.texto_validar_titulo = ""
        self.texto_validar_autor = ""
        self.texto_validar_genero = ""
        self.texto_validar_paginas = ""
        self.texto_validar_año = ""
 
        self.frame_libros = Frame(frame_contenido, bg="alice blue")
        self.frame_libros.pack()

        label_seccion_libros = Label(self.frame_libros, text="REGISTRO DE LIBROS", bg="alice blue",fg="turquoise4", font=("Arial", 16,"bold"))
        label_seccion_libros.grid(row=0, column=0, columnspan=2, pady=15)

        
        labelid = Label(self.frame_libros, text="id",bg='alice blue')
        labelid.grid(row=1, column=0, pady=5)
        entryid = Entry(self.frame_libros, textvariable=self.libros.id, width=30)         
        entryid.grid(row=1, column=1, pady=5)

      
        label_titulo = Label(self.frame_libros, text="Título", bg="alice blue", fg="black")
        label_titulo.grid(row=2, column=0, pady=5)
        entry_titulo = Entry(self.frame_libros, width=30, textvariable=self.libros.titulo)
        entry_titulo.grid(row=2, column=1, pady=5)
        self.label_error_titulo = Label(self.frame_libros, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_titulo.grid(row=2, column=2, pady=5)

        
        label_autor = Label(self.frame_libros, text="Autor", bg="alice blue", fg="black")
        label_autor.grid(row=4, column=0, pady=5)
        entry_autor = Entry(self.frame_libros, width=30, textvariable=self.libros.autor)
        entry_autor.grid(row=4, column=1, pady=5)
        self.label_error_autor = Label(self.frame_libros, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_autor.grid(row=4, column=2, pady=5)

        
        label_genero = Label(self.frame_libros, text="Género", bg="alice blue", fg="black")
        label_genero.grid(row=6, column=0, pady=5)
        entry_genero = Entry(self.frame_libros, width=30, textvariable=self.libros.genero)
        entry_genero.grid(row=6, column=1, pady=5)
        self.label_error_genero = Label(self.frame_libros, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_genero.grid(row=6, column=2, pady=5)

     
        label_paginas = Label(self.frame_libros, text="Páginas", bg="alice blue", fg="black")
        label_paginas.grid(row=8, column=0, pady=5)
        entry_paginas = Entry(self.frame_libros, width=30, textvariable=self.libros.paginas)
        entry_paginas.grid(row=8, column=1, pady=5)
        self.label_error_paginas = Label(self.frame_libros, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_paginas.grid(row=8, column=2, pady=5)

        
        label_año = Label(self.frame_libros, text="Año de Publicación", bg="alice blue", fg="black")              
        label_año.grid(row=10, column=0, pady=5)
        entry_año = Entry(self.frame_libros, width=30, textvariable=self.libros.año_publicacion)
        entry_año.grid(row=10, column=1, pady=5)
        self.label_error_año = Label(self.frame_libros, text="", bg="alice blue", fg="red",width=20, anchor="w")
        self.label_error_año.grid(row=10, column=2, pady=5)

        boton_guardar_libro = Button(self.frame_libros, text="Registrar", width=17, height=1, border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat",command=lambda: self.accion_registrar_boton(entry_titulo.get(), entry_autor.get(), entry_genero.get(), entry_paginas.get(), entry_año.get()))
        boton_guardar_libro.grid(row=12, column=0, pady=5)

        boton_registros_libros = Button(self.frame_libros, text="Registros Existentes", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat",command=lambda: self.accion_consultar_todo(entry_titulo.get(), entry_autor.get(), entry_genero.get(), entry_paginas.get(), entry_año.get()))
        boton_registros_libros.grid(row=12, column=1, pady=5)

        boton_eliminar_libro = Button(self.frame_libros, text="Eliminar", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat",command=lambda: self.accion_eliminar_boton(entryid.get()))
        boton_eliminar_libro.grid(row=13, column=0, pady=5)

        boton_actualizar_libro = Button(self.frame_libros, text="Actualizar", width=17, height=1,border=1,font=("Arial", 10, "bold"), bg= "dark turquoise", fg="white",relief="flat",command=lambda: self.accion_actualizar_boton(entryid.get(), entry_titulo.get(), entry_autor.get(), entry_genero.get(), entry_paginas.get(), entry_año.get()))
        boton_actualizar_libro.grid(row=13, column=1, pady=5)
        
        titulos = ['Id', 'Titulo', 'Autor', 'Genero', 'Paginas', 'Año de Publicación']
        columnas = ['id', 'titulo', 'autor', 'genero', 'paginas', 'año_publicacion']
        data = []
        self.frameTabla = Frame(frame_contenido, bg="alice blue")
        self.tabla = Tabla(self.frameTabla, titulos, columnas, data)
        self.frameTabla.pack()
        self.tabla.tabla.pack()

        
        def evento_validar_titulo(event):
            if self.validaciones.validar_letras(self.libros.titulo):
                self.texto_validar_titulo = ""
            else:
                self.texto_validar_titulo = "Solo se permiten letras"
            self.label_error_titulo.config(text=self.texto_validar_titulo, fg="dark turquoise")

        def evento_validar_autor(event):
            if self.validaciones.validar_letras(self.libros.autor):
                self.texto_validar_autor = ""
            else:
                self.texto_validar_autor = "Solo se permiten letras"
            self.label_error_autor.config(text=self.texto_validar_autor, fg="dark turquoise")

        def evento_validar_genero(event):
            if self.validaciones.validar_letras(self.libros.genero):
                self.texto_validar_genero = ""
            else:
                self.texto_validar_genero = "Solo se permiten letras"
            self.label_error_genero.config(text=self.texto_validar_genero, fg="dark turquoise")

        def evento_validar_paginas(event):
            if self.validaciones.validar_numeros(self.libros.paginas):
                self.texto_validar_paginas = ""
            else:
                self.texto_validar_paginas = "Solo se permiten numeros"
            self.label_error_paginas.config(text=self.texto_validar_paginas, fg="dark turquoise")

        def evento_validar_año(event):
            if self.validaciones.validar_numeros(self.libros.año_publicacion):
                self.texto_validar_año = ""
            else:
                self.texto_validar_año = "Solo se permiten numeros"
            self.label_error_año.config(text=self.texto_validar_año, fg="dark turquoise")


        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryid.delete(0, END)
                entryid.insert(0, str(valores[0]))
                entry_titulo.delete(0, END)
                entry_titulo.insert(0, str(valores[1]))
                entry_autor.delete(0, END)
                entry_autor.insert(0, str(valores[2]))
                entry_genero.delete(0, END)
                entry_genero.insert(0, str(valores[3]))
                entry_paginas.delete(0, END)
                entry_paginas.insert(0, int(valores[4]))
                entry_año.delete(0, END)
                entry_año.insert(0, int(valores[5]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                id_eliminar = self.tabla.tabla.item(i)['values'][0]
                resultado = self.comunicaciones_libros.eliminar(id_eliminar)
                if resultado == 204 or resultado == 200:
                    print(f"Registro con ID {id_eliminar} eliminado correctamente.")
                    self.accion_consultar_todo('', '', '', '')
                else:
                    print(f"No se pudo eliminar el registro con ID {id_eliminar}.")

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        entry_titulo.bind("<KeyRelease>", evento_validar_titulo)
        entry_autor.bind("<KeyRelease>", evento_validar_autor)
        entry_genero.bind("<KeyRelease>", evento_validar_genero)
        entry_paginas.bind("<KeyRelease>", evento_validar_paginas)
        entry_año.bind("<KeyRelease>", evento_validar_año)