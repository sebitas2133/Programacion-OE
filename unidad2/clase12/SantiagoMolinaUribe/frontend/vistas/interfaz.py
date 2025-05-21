import tkinter as tk
from controladores.comunicacion import Comunicacion
from controladores.validaciones import Validaciones
from modelos.universidad import Universidad
from .tablas import Tabla
from tkinter import * 
from tkinter import messagebox


class Interfaz():

    def __init__(self):
        titulos = ['Id', 'Facultad de Ingenieria', 'Facultad de Ciencias De La Salud', 'Facultad de Educación', 'Facultad de Ciencias Contables']
        columnas = ['id', 'edificio1', 'edificio2', 'edificio3', 'edificio4']
        data = []
        self.VentanaPrincipal = tk.Tk()
        self.frameTabla = Frame(self.VentanaPrincipal)
        self.comunicacion = Comunicacion(self.VentanaPrincipal)
        self.validaciones = Validaciones()
        self.tabla = Tabla(self.frameTabla, titulos, columnas, data)
        self.universidad = Universidad(self.VentanaPrincipal)
        pass

    def accion_guardar_boton(self, edificio1, edificio2, edificio3, edificio4):
        resultado = self.comunicacion.guardar(edificio1, edificio2, edificio3, edificio4)

        if resultado == 201:    
            self.accion_consultar_todo('', '', '', '')
            messagebox.showinfo("Guardado exitoso", "Se guardó el registro")
        else:   
            messagebox.showerror("Guardado fallido", "No se pudo guardar el registro")
        

    def accion_consultar_boton(self, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            self.tabla.refrescar([])
            data = [(resultado.get('id'),
                    resultado.get('edificio1'),
                    resultado.get('edificio2'),
                    resultado.get('edificio3'),
                    resultado.get('edificio4'))]
            self.tabla.refrescar(data)
            messagebox.showinfo("Consulta exitosa", "Se encontró el registro")
        else:
            messagebox.showerror("Consulta fallida", "No se encontró el registro")

    def accion_consultar_todo(self, edificio1, edificio2, edificio3, edificio4):
        resultado = self.comunicacion.consultar_todo(edificio1, edificio2, edificio3, edificio4)


        if isinstance(resultado, dict):
            resultado = [resultado]

        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('edificio1'),
                elemento.get('edificio2'),
                elemento.get('edificio3'),
                elemento.get('edificio4')
            ))
    
        self.tabla.refrescar(data)
        
    
    def accion_actualizar_boton(self, id, edificio1, edificio2, edificio3, edificio4):
        resultado = self.comunicacion.actualizar(id, edificio1, edificio2, edificio3, edificio4)

        if resultado == 200:
            self.accion_consultar_todo('', '', '', '')
            messagebox.showinfo("Actualización exitosa", "Se actualizó el registro")
        else:
            messagebox.showerror("Actualización fallida", "No se pudo actualizar el registro")
    
    def accion_eliminar_boton(self, id, id_entry, edificio1_entry, edificio2_enty, edificio3_entry, edificio4_entry):
        if id == '':
            print("No se ha especificado un ID para eliminar.")
        else:
            resultado = self.comunicacion.eliminar(id)
            if resultado == 204 or resultado == 200:
                self.accion_consultar_todo('', '', '', '')
                id_entry.delete(0, tk.END)
                edificio1_entry.delete(0, tk.END)
                edificio2_enty.delete(0, tk.END)
                edificio3_entry.delete(0, tk.END)
                edificio4_entry.delete(0, tk.END)
                messagebox.showinfo("Eliminación exitosa", "Se eliminó el registro")
                
            else:
                messagebox.showerror("Eliminación fallida", "No se pudo eliminar el registro")

        
    
    def mostrar_interfaz(self):

        self.texto_validar_edificio1 = ""
        self.texto_validar_edificio2 = ""
        self.texto_validar_edificio3 = ""
        self.texto_validar_edificio4 = ""

        self.VentanaPrincipal.title("Universidad")
        self.VentanaPrincipal.geometry("1010x800")
        self.VentanaPrincipal.config(bg="white")

        self.frame = Frame(self.VentanaPrincipal, width=600, height=500, bg="white")
        self.frame.pack_propagate(False)
        self.frame.pack()

        self.frameTabla.pack()

        titulo_label = Label(self.frame, text="INTRODUZCA EL PROGRAMA CORRESPONDIENTE A LA FACULTAD", bg="white", fg="black", height=3, font=("Helvetica", 11, "bold"))
        titulo_label.grid(row=0, column=0, columnspan=3)

       
        id_label = Label(self.frame, text="ID:", bg="white", fg="black")
        id_label.grid(row=1, column=0, pady=5)
        id_entry = Entry(self.frame, textvariable=self.universidad.id)
        id_entry.grid(row=1, column=1, pady=5)

        BotonConsultar = Button(self.frame, text="Consultar", bg="black", fg="white", width=10,
                                activebackground="gray",
                                relief="flat",
                                command=lambda: self.accion_consultar_boton( id_entry.get()))
        BotonConsultar.grid(row=1, column=2, pady=5)

        self.edificio1 = StringVar(self.frame)
        edificio1_label = Label(self.frame, text="Facultad de Ingenieria:", bg="white", fg="black").grid(row=2, column=0)
        edificio1_entry = Entry(self.frame, textvariable=self.universidad.edificio1)
        edificio1_entry.grid(row=2, column=1)
        label_Error_edificio1 = Label(self.frame, text="", bg="white", fg="red")
        label_Error_edificio1.grid(row=2, column=2, pady=2, columnspan=2)

        self.edificio2 = StringVar(self.frame)
        edificio2_label = Label(self.frame, text="Facultad de Ciencias De La Salud: ", bg="white", fg="black").grid(row=4, column=0)
        edificio2_enty = Entry(self.frame,  textvariable=self.universidad.edificio2)
        edificio2_enty.grid(row=4, column=1)
        label_Error_edificio2 = Label(self.frame, text="", bg="white", fg="red")
        label_Error_edificio2.grid(row=4, column=2, columnspan=2, pady=2)

        self.edificio3 = StringVar(self.frame)
        edificio3_label = Label(self.frame, text="Facultad de Educación:", bg="white", fg="black").grid(row=6, column=0)
        edificio3_entry = Entry(self.frame, textvariable=self.universidad.edificio3)
        edificio3_entry.grid(row=6, column=1)
        label_Error_edificio3 = Label(self.frame, text="", bg="white", fg="red")
        label_Error_edificio3.grid(row=6, column=2, columnspan=2, pady=2)

        self.edificio4 = StringVar(self.frame)
        edificio4_label = Label(self.frame, text="Facultad de Ciencias Contables:", bg="white", fg="black").grid(row=8, column=0,)
        edificio4_entry = Entry(self.frame, textvariable=self.universidad.edificio4)
        edificio4_entry.grid(row=8, column=1)
        label_Error_edificio4 = Label(self.frame, text="", bg="white", fg="red")
        label_Error_edificio4.grid(row=8, column=2, columnspan=2, pady=2)


        BotonGuardar = Button(self.frame, text="Guardar", bg="black", fg="white", width=10,
                            activebackground="gray",
                            relief="flat",
                            command= lambda: self.accion_guardar_boton(edificio1_entry.get(), edificio2_enty.get(), edificio3_entry.get(), edificio4_entry.get()))

        BotonGuardar.grid(row=10, column=0, columnspan=3, pady=5)

        BotonActualizar = Button(self.frame, text="Actualizar", bg="black", fg="white", width=10,
                                activebackground="gray",
                                relief="flat", 
                                command=lambda: self.accion_actualizar_boton(id_entry.get(), edificio1_entry.get(), edificio2_enty.get(), edificio3_entry.get(), edificio4_entry.get()))

        BotonActualizar.grid(row=11, column=0, columnspan=3, pady=5)

        BotonEliminar = Button(self.frame, text="Eliminar", bg="black", fg="white", width=10,
                                activebackground="gray",
                                relief="flat", 
                                command=lambda: self.accion_eliminar_boton(id_entry.get(), id_entry, edificio1_entry, edificio2_enty, edificio3_entry, edificio4_entry))

        BotonEliminar.grid(row=12, column=0, columnspan=3, pady=5)

        BontonConsultarTodos = Button(self.frame, text="Consultar todos", bg="black", fg="white", width=12,
                                activebackground="gray",
                                relief="flat",
                                command=lambda: self.accion_consultar_todo('', '', '',''))

        BontonConsultarTodos.grid(row=13, column=0, columnspan=3, pady=5)
        self.tabla.tabla.grid(row=14, column=0, columnspan=3)

      

        def evento_presionar_tecla_edificio1(event):
            if self.validaciones.validarLetras(self.universidad.edificio1):
                self.texto_validar_edificio1 = ""
            else:
                self.texto_validar_edificio1 = "Solo se permiten letras"
            label_Error_edificio1.config(text=self.texto_validar_edificio1)

        
        def evento_presionar_tecla_edificio2(event):
            if self.validaciones.validarLetras(self.universidad.edificio2):
                self.texto_validar_edificio2 = ""
            else:
                self.texto_validar_edificio2 = "Solo se permiten letras"
            label_Error_edificio2.config(text=self.texto_validar_edificio2)

        def evento_presionar_tecla_edificio3(event):
            if self.validaciones.validarLetras(self.universidad.edificio3):
                self.texto_validar_edificio3 = ""
            else:
                self.texto_validar_edificio3 = "Solo se permiten letras"
            label_Error_edificio3.config(text=self.texto_validar_edificio3)

        def evento_presionar_tecla_edificio4(event):
            if self.validaciones.validarLetras(self.universidad.edificio4):
                self.texto_validar_edificio4 = ""
            else:
                self.texto_validar_edificio4 = "Solo se permiten letras"
            label_Error_edificio4.config(text=self.texto_validar_edificio4)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                id_entry.delete(0, tk.END)
                id_entry.insert(0, str(valores[0]))
                edificio1_entry.delete(0, tk.END)
                edificio1_entry.insert(0, str(valores[1]))
                edificio2_enty.delete(0, tk.END)
                edificio2_enty.insert(0, str(valores[2]))
                edificio3_entry.delete(0, tk.END)
                edificio3_entry.insert(0, str(valores[3]))
                edificio4_entry.delete(0, tk.END)
                edificio4_entry.insert(0, str(valores[4]))

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

        edificio1_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio1)
        edificio2_enty.bind("<KeyRelease>", evento_presionar_tecla_edificio2)
        edificio3_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio3)
        edificio4_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio4)

        self.VentanaPrincipal.mainloop()
