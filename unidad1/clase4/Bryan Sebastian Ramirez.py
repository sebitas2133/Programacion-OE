from tkinter import *
import re

texto_validar_nombre = ""
texto_validar_ingrediente_principal = ""
texto_validar_calorias = ""
texto_validar_peso = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title("Comida")

frame = Frame(ventanaPrincipal, width=500, height=500)
frame.pack_propagate(False)
frame.pack()

nombre = StringVar(frame)
nombre_label = Label(frame, text="Nombre")
nombre_entry = Entry(frame, textvariable=nombre)
label_Error_nombre = Label(frame, text="")

ingrediente_principal = StringVar(frame)
ingrediente_principal_label = Label(frame, text="Ingrediente principal")
ingrediente_principal_enty = Entry(frame, textvariable=ingrediente_principal)
label_Error_ingrediente_principal = Label(frame, text="")

calorias = StringVar(frame)
calorias_label = Label(frame, text="Calorias")
calorias_entry = Entry(frame, textvariable=calorias)
label_Error_calorias = Label(frame, text="")

peso = StringVar(frame)
peso_label = Label(frame, text="Peso (g)")
peso_entry = Entry(frame, textvariable=peso)
label_Error_peso = Label(frame, text="")


boton = Button(frame, text="Guardar")

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

nombre_label.pack()
nombre_entry.bind("<KeyRelease>", evento_presionar_tecla_nombre)
nombre_entry.pack()
label_Error_nombre.pack()

ingrediente_principal_label.pack()
ingrediente_principal_enty.bind("<KeyRelease>", evento_presionar_tecla_ingrediente)
ingrediente_principal_enty.pack()
label_Error_ingrediente_principal.pack()

calorias_label.pack()
calorias_entry.bind("<KeyRelease>", evento_presionar_tecla_calorias)
calorias_entry.pack()
label_Error_calorias.pack()

peso_label.pack()
peso_entry.bind("<KeyRelease>", evento_presionar_tecla_peso)
peso_entry.pack()
label_Error_peso.pack()

boton.pack()

ventanaPrincipal.mainloop()