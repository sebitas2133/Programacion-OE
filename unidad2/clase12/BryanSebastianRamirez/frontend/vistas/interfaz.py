import tkinter as tk
from controladores.comunicacion import Comunicacion
from controladores.validaciones import Validaciones
from modelos.Comida import Comida
from .tablas import Tabla
from tkinter import * 
from tkinter import messagebox


class Interfaz():

    def __init__(self):
        titulos = ['Identificador', 'Nombre', 'Ingrediente Principal', 'Calorias', 'Peso']
        columnas = ['id', 'nombre', 'ingrediente_principal', 'calorias', 'peso']
        data = []
        self.VentanaPrincipal = tk.Tk()
        self.frameTabla = Frame(self.VentanaPrincipal)
        self.comunicacion = Comunicacion(self.VentanaPrincipal)
        self.validaciones = Validaciones()
        self.tabla = Tabla(self.frameTabla, titulos, columnas, data)
        self.comida = Comida(self.VentanaPrincipal)
        pass

    def accion_guardar_boton(self, nombre, ingrediente_principal, calorias, peso):
        resultado = self.comunicacion.guardar(nombre, ingrediente_principal, calorias, peso)

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
                    resultado.get('nombre'),
                    resultado.get('ingrediente_principal'),
                    resultado.get('calorias'),
                    resultado.get('peso'))]
            self.tabla.refrescar(data)
            messagebox.showinfo("Consulta exitosa", "Se encontró el registro")
        else:
            messagebox.showerror("Consulta fallida", "No se encontró el registro")

    def accion_consultar_todo(self, nombre, ingrediente_principal, calorias, peso):
        resultado = self.comunicacion.consultar_todo(nombre, ingrediente_principal, calorias, peso)


        if isinstance(resultado, dict):
            resultado = [resultado]

        data = []
        for elemento in resultado:
            data.append((
                elemento.get('id'),
                elemento.get('nombre'),
                elemento.get('ingrediente_principal'),
                elemento.get('calorias'),
                elemento.get('peso')
            ))
    
        self.tabla.refrescar(data)
        
    
    def accion_actualizar_boton(self, id, nombre, ingrediente_principal, calorias, peso):
        resultado = self.comunicacion.actualizar(id, nombre, ingrediente_principal, calorias, peso)

        if resultado == 200:
            self.accion_consultar_todo('', '', '', '')
            messagebox.showinfo("Actualización exitosa", "Se actualizó el registro")
        else:
            messagebox.showerror("Actualización fallida", "No se pudo actualizar el registro")
    
    def accion_eliminar_boton(self, id, id_entry, nombre_entry, ingrediente_principal_enty, calorias_entry, peso_entry):
        if id == '':
            print("No se ha especificado un ID para eliminar.")
        else:
            resultado = self.comunicacion.eliminar(id)
            if resultado == 204 or resultado == 200:
                self.accion_consultar_todo('', '', '', '')
                id_entry.delete(0, tk.END)
                nombre_entry.delete(0, tk.END)
                ingrediente_principal_enty.delete(0, tk.END)
                calorias_entry.delete(0, tk.END)
                peso_entry.delete(0, tk.END)
                messagebox.showinfo("Eliminación exitosa", "Se eliminó el registro")
                
            else:
                messagebox.showerror("Eliminación fallida", "No se pudo eliminar el registro")

        
    
    def mostrar_interfaz(self):

        self.texto_validar_nombre = ""
        self.texto_validar_ingrediente_principal = ""
        self.texto_validar_calorias = ""
        self.texto_validar_peso = ""

        self.VentanaPrincipal.title("Comida")
        self.VentanaPrincipal.geometry("1010x800")
        self.VentanaPrincipal.config(bg="#121212")

        self.frame = Frame(self.VentanaPrincipal, width=600, height=500, bg="#121212")
        self.frame.pack_propagate(False)
        self.frame.pack()

        self.frameTabla.pack()

        titulo_label = Label(self.frame, text="INTRODUZCA LOS SIGUIENTES REQUERIMIENTOS", bg="#121212", fg="#39ff14", height=3, font=("Helvetica", 11, "bold"))
        titulo_label.grid(row=0, column=0, columnspan=3)

        id_label = Label(self.frame, text="ID:", bg="#121212", fg="#39ff14")
        id_label.grid(row=1, column=0, pady=5)
        id_entry = Entry(self.frame, textvariable=self.comida.id)
        id_entry.grid(row=1, column=1, pady=5)

        BotonConsultar = Button(self.frame, text="Consultar", bg="#222222", fg="#39ff14", width=10,
                                activebackground="#39ff14",
                                relief="flat",
                                command=lambda: self.accion_consultar_boton( id_entry.get()))
        BotonConsultar.grid(row=1, column=2, pady=5)

        
        nombre_label = Label(self.frame, text="Nombre:", bg="#121212", fg="#39ff14").grid(row=2, column=0)
        nombre_entry = Entry(self.frame, textvariable=self.comida.nombre)
        nombre_entry.grid(row=2, column=1)
        label_Error_nombre = Label(self.frame, text="", bg="#121212", fg="#39ff14")
        label_Error_nombre.grid(row=2, column=2, pady=2, columnspan=2)

        ingrediente_principal_label = Label(self.frame, text="Ingrediente principal: ", bg="#121212", fg="#39ff14").grid(row=4, column=0)
        ingrediente_principal_enty = Entry(self.frame,  textvariable=self.comida.ingrediente_principal)
        ingrediente_principal_enty.grid(row=4, column=1)
        label_Error_ingrediente_principal = Label(self.frame, text="", bg="#121212", fg="#39ff14")
        label_Error_ingrediente_principal.grid(row=4, column=2, columnspan=2, pady=2)

        calorias_label = Label(self.frame, text="Calorias:", bg="#121212", fg="#39ff14").grid(row=6, column=0)
        calorias_entry = Entry(self.frame, textvariable=self.comida.calorias)
        calorias_entry.grid(row=6, column=1)
        label_Error_calorias = Label(self.frame, text="", bg="#121212", fg="#39ff14")
        label_Error_calorias.grid(row=6, column=2, columnspan=2, pady=2)

        peso_label = Label(self.frame, text="Peso (g):", bg="#121212", fg="#39ff14").grid(row=8, column=0,)
        peso_entry = Entry(self.frame, textvariable=self.comida.peso)
        peso_entry.grid(row=8, column=1)
        label_Error_peso = Label(self.frame, text="", bg="#121212", fg="#39ff14")
        label_Error_peso.grid(row=8, column=2, columnspan=2, pady=2)


        BotonGuardar = Button(self.frame, text="Guardar", bg="#222222", fg="#39ff14", width=10,
                            activebackground="#39ff14",
                            relief="flat",
                            command= lambda: self.accion_guardar_boton(nombre_entry.get(), ingrediente_principal_enty.get(), calorias_entry.get(), peso_entry.get()))

        BotonGuardar.grid(row=10, column=0, columnspan=3, pady=5)

        BotonActualizar = Button(self.frame, text="Actualizar", bg="#222222", fg="#39ff14", width=10,
                                activebackground="#39ff14",
                                relief="flat", 
                                command=lambda: self.accion_actualizar_boton(id_entry.get(), nombre_entry.get(), ingrediente_principal_enty.get(), calorias_entry.get(), peso_entry.get()))

        BotonActualizar.grid(row=11, column=0, columnspan=3, pady=5)

        BotonEliminar = Button(self.frame, text="Eliminar", bg="#222222", fg="#39ff14", width=10,
                                activebackground="#39ff14",
                                relief="flat", 
                                command=lambda: self.accion_eliminar_boton(id_entry.get(), id_entry, nombre_entry, ingrediente_principal_enty, calorias_entry, peso_entry))

        BotonEliminar.grid(row=12, column=0, columnspan=3, pady=5)

        BontonConsultarTodos = Button(self.frame, text="Consultar todos", bg="#222222", fg="#39ff14", width=12,
                                activebackground="#39ff14",
                                relief="flat",
                                command=lambda: self.accion_consultar_todo('', '', '',''))

        BontonConsultarTodos.grid(row=13, column=0, columnspan=3, pady=5)
        self.tabla.tabla.grid(row=14, column=0, columnspan=3)


        def evento_presionar_tecla_nombre(event):
            if self.validaciones.validarLetras(self.comida.nombre):
                self.texto_validar_nombre = ""
            else:
                self.texto_validar_nombre = "<- Solo se permiten letras"
            label_Error_nombre.config(text=self.texto_validar_nombre)

        
        def evento_presionar_tecla_ingrediente(event):
            if self.validaciones.validarLetras(self.comida.ingrediente_principal):
                self.texto_validar_ingrediente_principal = ""
            else:
                self.texto_validar_ingrediente_principal = "<- Solo se permiten letras"
            label_Error_ingrediente_principal.config(text=self.texto_validar_ingrediente_principal)

        def evento_presionar_tecla_calorias(event):
            if self.validaciones.validarNumeros(self.comida.calorias):
                self.texto_validar_calorias = ""
            else:
                self.texto_validar_calorias = "<- Solo se permiten numeros"
            label_Error_calorias.config(text=self.texto_validar_calorias)

        def evento_presionar_tecla_peso(event):
            if self.validaciones.validarNumeros(self.comida.peso):
                self.texto_validar_peso = ""
            else:
                self.texto_validar_peso = "<- Solo se permiten numeros"
            label_Error_peso.config(text=self.texto_validar_peso)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                id_entry.delete(0, tk.END)
                id_entry.insert(0, str(valores[0]))
                nombre_entry.delete(0, tk.END)
                nombre_entry.insert(0, str(valores[1]))
                ingrediente_principal_enty.delete(0, tk.END)
                ingrediente_principal_enty.insert(0, str(valores[2]))
                calorias_entry.delete(0, tk.END)
                calorias_entry.insert(0, str(valores[3]))
                peso_entry.delete(0, tk.END)
                peso_entry.insert(0, str(valores[4]))

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

        nombre_entry.bind("<KeyRelease>", evento_presionar_tecla_nombre)
        ingrediente_principal_enty.bind("<KeyRelease>", evento_presionar_tecla_ingrediente)
        calorias_entry.bind("<KeyRelease>", evento_presionar_tecla_calorias)
        peso_entry.bind("<KeyRelease>", evento_presionar_tecla_peso)

        self.VentanaPrincipal.mainloop()
