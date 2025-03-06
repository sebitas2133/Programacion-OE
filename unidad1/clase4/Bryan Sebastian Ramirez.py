from tkinter import *
import re

texto_validar_nombre = ""
texto_validar_ingrediente_principal = ""
texto_validar_calorias = ""
texto_validar_peso = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title("Comida")
ventanaPrincipal.geometry("450x300")
ventanaPrincipal.config(bg="#1E1E1E")

frame = Frame(ventanaPrincipal, width=500, height=500, bg="#1E1E1E")
frame.pack_propagate(False)
frame.pack()

titulo_label = Label(frame, text="INTRODUZCA LOS SIGUIENTES REQUERIMIENTOS", bg="#1E1E1E", fg="white", height=3, font=("Helvetica", 11, "bold"))
titulo_label.grid(row=0, column=0, columnspan=2)


nombre = StringVar(frame)
nombre_label = Label(frame, text="Nombre:", bg="#1E1E1E", fg="white").grid(row=1, column=0)
nombre_entry = Entry(frame, textvariable=nombre)
nombre_entry.grid(row=1, column=1)
label_Error_nombre = Label(frame, text="", bg="#1E1E1E", fg="white")
label_Error_nombre.grid(row=2, column=0, columnspan=2)

ingrediente_principal = StringVar(frame)
ingrediente_principal_label = Label(frame, text="Ingrediente principal: ", bg="#1E1E1E", fg="white").grid(row=3, column=0)
ingrediente_principal_enty = Entry(frame, textvariable=ingrediente_principal)
ingrediente_principal_enty.grid(row=3, column=1)
label_Error_ingrediente_principal = Label(frame, text="", bg="#1E1E1E", fg="white")
label_Error_ingrediente_principal.grid(row=4, column=0, columnspan=2)

calorias = StringVar(frame)
calorias_label = Label(frame, text="Calorias:", bg="#1E1E1E", fg="white").grid(row=5, column=0)
calorias_entry = Entry(frame, textvariable=calorias)
calorias_entry.grid(row=5, column=1)
label_Error_calorias = Label(frame, text="", bg="#1E1E1E", fg="white")
label_Error_calorias.grid(row=6, column=0, columnspan=2)

peso = StringVar(frame)
peso_label = Label(frame, text="Peso (g):", bg="#1E1E1E", fg="white").grid(row=7, column=0)
peso_entry = Entry(frame, textvariable=peso)
peso_entry.grid(row=7, column=1)
label_Error_peso = Label(frame, text="", bg="#1E1E1E", fg="white")
label_Error_peso.grid(row=8, column=0, columnspan=2)


boton = Button(frame, text="Guardar", bg="black", fg="white", width=10,
             activebackground="#1E1E1E",
             activeforeground="white", bd = 0.5).grid(row=9, column=0, columnspan=2)

def validarLetras(valor):
    patron =  re.compile("^[a-zA-ZnÑ ]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True
 
def validarNumeros(valor):
    patron =  re.compile("^[0-9]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def evento_presionar_tecla_nombre(event):
    global texto_validar_nombre
    global nombre
    if validarLetras(nombre):
        texto_validar_nombre = ""
    else:
        texto_validar_nombre = "Solo se permiten letras"
    label_Error_nombre.config(text=texto_validar_nombre)

def evento_presionar_tecla_ingrediente(event):
    global texto_validar_ingrediente_principal
    global ingrediente_principal
    if validarLetras(ingrediente_principal):
        texto_validar_ingrediente_principal = ""
    else:
        texto_validar_ingrediente_principal = "Solo se permiten letras"
    label_Error_ingrediente_principal.config(text=texto_validar_ingrediente_principal)

def evento_presionar_tecla_calorias(event):
    global texto_validar_calorias
    global calorias
    if validarNumeros(calorias):
        texto_validar_calorias = ""
    else:
        texto_validar_calorias = "Solo se permiten numeros"
    label_Error_calorias.config(text=texto_validar_calorias)

def evento_presionar_tecla_peso(event):
    global texto_validar_peso
    global peso
    if validarNumeros(peso):
        texto_validar_peso = ""
    else:
        texto_validar_peso = "Solo se permiten numeros"
    label_Error_peso.config(text=texto_validar_peso)

nombre_entry.bind("<KeyRelease>", evento_presionar_tecla_nombre)
ingrediente_principal_enty.bind("<KeyRelease>", evento_presionar_tecla_ingrediente)
calorias_entry.bind("<KeyRelease>", evento_presionar_tecla_calorias)
peso_entry.bind("<KeyRelease>", evento_presionar_tecla_peso)


ventanaPrincipal.mainloop()