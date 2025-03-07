from tkinter import *
import re

texto_validar_edificio1 = ""
texto_validar_edificio2 = ""
texto_validar_edificio3 = ""
texto_validar_edificio4 = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title("Universidad")
ventanaPrincipal.config(bg="gray")
ventanaPrincipal.geometry("500x300")


frame = Frame(ventanaPrincipal, width=500, height=500, bg="gray")
frame.pack_propagate(False)
frame.pack()

titulo_label = Label(frame, text="Introduzca el nombre del programa de cada facultad.", bg="gray", fg="black", height=3, font=("Calibri", 15))
titulo_label.grid(row=0, column=0, columnspan=2)

edificio1 = StringVar(frame)
edificio1_label = Label(frame, text="Facultad de Ingenieria:", bg="gray", fg="white").grid(row=1, column=0)
edificio1_entry = Entry(frame, textvariable=edificio1)
edificio1_entry.grid(row=1, column=1)
label_Error_edificio1 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio1.grid(row=2, column=0, columnspan=2)

edificio2 = StringVar(frame)
edificio2_label = Label(frame, text="Facultad de Ciencias de la Salud: ", bg="gray", fg="white").grid(row=3, column=0)
edificio2_enty = Entry(frame, textvariable=edificio2)
edificio2_enty.grid(row=3, column=1)
label_Error_edificio2 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio2.grid(row=4, column=0, columnspan=2)

edificio3 = StringVar(frame)
edificio3_label = Label(frame, text="Facultad de Ciencias de la Educación:", bg="gray", fg="white").grid(row=5, column=0)
edificio3_entry = Entry(frame, textvariable=edificio3)
edificio3_entry.grid(row=5, column=1)
label_Error_edificio3 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio3.grid(row=6, column=0, columnspan=2)

edificio4 = StringVar(frame)
edificio4_label = Label(frame, text="Facultad de Ciencias Economicas, Administrativas y Contables:", bg="gray", fg="white").grid(row=7, column=0)
edificio4_entry = Entry(frame, textvariable=edificio4)
edificio4_entry.grid(row=7, column=1)
label_Error_edificio4 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio4.grid(row=8, column=0, columnspan=2)


boton = Button(frame, text="Guardar", width=10, bg="gray", fg="white")
boton.grid(row=9, column=0, columnspan=2)

def validarLetras(valor):
    patron =  re.compile("^[a-zA-ZñÑ ]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def evento_presionar_tecla_edificio1(event):
    global texto_validar_edificio1
    global edificio1
    if validarLetras(edificio1):
        texto_validar_edificio1 = ""
    else:
        texto_validar_edificio1 = "Solo se permiten letras"
    label_Error_edificio1.config(text=texto_validar_edificio1)

def evento_presionar_tecla_edificio2(event):
    global texto_validar_edificio2
    global edificio2
    if validarLetras(edificio2):
        texto_validar_edificio2 = ""
    else:
        texto_validar_edificio2 = "Solo se permiten letras"
    label_Error_edificio2.config(text=texto_validar_edificio2)

def evento_presionar_tecla_edificio3(event):
    global texto_validar_edificio3
    global edificio3
    if validarLetras(edificio3):
        texto_validar_edificio3 = ""
    else:
        texto_validar_edificio3 = "Solo se permiten letras"
    label_Error_edificio3.config(text=texto_validar_edificio3)

def evento_presionar_tecla_edificio4(event):
    global texto_validar_edificio4
    global edificio4
    if validarLetras(edificio4):
        texto_validar_edificio4 = ""
    else:
        texto_validar_edificio4 = "Solo se permiten letras"
    label_Error_edificio4.config(text=texto_validar_edificio4)

edificio1_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio1)
edificio2_enty.bind("<KeyRelease>", evento_presionar_tecla_edificio2)
edificio3_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio3)
edificio4_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio4)


ventanaPrincipal.mainloop()
