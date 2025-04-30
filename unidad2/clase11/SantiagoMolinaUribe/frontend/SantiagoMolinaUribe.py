from tkinter import *
import re
import requests 

texto_validar_id = ""
texto_validar_edificio1 = ""
texto_validar_edificio2 = ""
texto_validar_edificio3 = ""
texto_validar_edificio4 = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title("Universidad")
ventanaPrincipal.config(bg="gray")
ventanaPrincipal.geometry("600x400")

frame = Frame(ventanaPrincipal, width=500, height=500, bg="gray")
frame.pack_propagate(False)
frame.pack()

titulo_label = Label(frame, text="Introduzca el nombre del programa de cada facultad.", bg="gray", fg="black", height=3, font=("Calibri", 15))
titulo_label.grid(row=0, column=0, columnspan=2)

id = StringVar(frame)
id_label = Label(frame, text="ID:", bg="gray", fg="white").grid(row=1, column=0)
id_entry = Entry(frame, textvariable=id)
id_entry.grid(row=1, column=1)
label_Error_id = Label(frame, text="", bg="gray", fg="red")
label_Error_id.grid(row=2, column=0, columnspan=2)

edificio1 = StringVar(frame)
edificio1_label = Label(frame, text="Facultad de Ingenieria:", bg="gray", fg="white").grid(row=3, column=0)
edificio1_entry = Entry(frame, textvariable=edificio1)
edificio1_entry.grid(row=3, column=1)
label_Error_edificio1 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio1.grid(row=4, column=0, columnspan=2)

edificio2 = StringVar(frame)
edificio2_label = Label(frame, text="Facultad de Ciencias de la Salud: ", bg="gray", fg="white").grid(row=5, column=0)
edificio2_entry = Entry(frame, textvariable=edificio2)
edificio2_entry.grid(row=5, column=1)
label_Error_edificio2 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio2.grid(row=6, column=0, columnspan=2)

edificio3 = StringVar(frame)
edificio3_label = Label(frame, text="Facultad de Ciencias de la Educación:", bg="gray", fg="white").grid(row=7, column=0)
edificio3_entry = Entry(frame, textvariable=edificio3)
edificio3_entry.grid(row=7, column=1)
label_Error_edificio3 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio3.grid(row=8, column=0, columnspan=2)

edificio4 = StringVar(frame)
edificio4_label = Label(frame, text="Facultad de Ciencias Economicas, Administrativas y Contables:", bg="gray", fg="white").grid(row=9, column=0)
edificio4_entry = Entry(frame, textvariable=edificio4)
edificio4_entry.grid(row=9, column=1)
label_Error_edificio4 = Label(frame, text="", bg="gray", fg="red")
label_Error_edificio4.grid(row=10, column=0, columnspan=2)

def limpiar_campos():
    id_entry.delete(0, END)
    edificio1_entry.delete(0, END)
    edificio2_entry.delete(0, END)
    edificio3_entry.delete(0, END)
    edificio4_entry.delete(0, END)

def validarLetras(valor):
    patron =  re.compile("^[a-zA-ZñÑ ]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def validarNumeros(valor):
    patron = re.compile("^[0-9]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def evento_presionar_tecla_id(event):
    global texto_validar_id
    global id
    if validarNumeros(id):
        texto_validar_id = ""
    else:
        texto_validar_id = "Solo se permiten números"
    label_Error_id.config(text=texto_validar_id)

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

def guardar():
    data = {
        "edificio1": edificio1_entry.get(),
        "edificio2": edificio2_entry.get(),
        "edificio3": edificio3_entry.get(),
        "edificio4": edificio4_entry.get()
    }
    response = requests.post("http://localhost:8000/api/universidad/", json=data)
    if response.status_code in (200, 201):
        print("Éxito", "Datos guardado")
    limpiar_campos()

def consultar():
    id = id_entry.get()
    if id:
        response = requests.get("http://localhost:8000/api/universidad/" + id + "/")
        if response.status_code == 200:
            data = response.json()
            edificio1_entry.delete(0, END)
            edificio1_entry.insert(0, data['edificio1'])
            edificio2_entry.delete(0, END)
            edificio2_entry.insert(0, data['edificio2'])
            edificio3_entry.delete(0, END)
            edificio3_entry.insert(0, data['edificio3'])
            edificio4_entry.delete(0, END)
            edificio4_entry.insert(0, data['edificio4'])
        else:
            print("Error", "Datos no encontrados")

def actualizar():
    id = id_entry.get()
    if id_entry:
        data = {
            "edificio1": edificio1_entry.get(),
            "edificio2": edificio2_entry.get(),
            "edificio3": edificio3_entry.get(),
            "edificio4": edificio4_entry.get()
        }
        response = requests.put("http://localhost:8000/api/universidad/" + id + "/", json=data)
        if response.status_code == 200:
            print("Éxito", "Datos actualizados")
    limpiar_campos()

def eliminar():
    id = id_entry.get()
    if id:
        response = requests.delete("http://localhost:8000/api/universidad/" + id + "/")
        if response.status_code == 204:
            print("Éxito", "Datos eliminados")
    limpiar_campos()

boton_guardar = Button(frame, text= "Guardar", width=10, bg="gray", fg="white", command= guardar)
boton_guardar.grid(row=11, column=0, columnspan=3)

boton_consultar = Button(frame, text="Consultar", width=10, bg="gray", fg="white", command= consultar)
boton_consultar.grid(row=1, column=2)

boton_actualizar = Button(frame, text="Actualizar", width=10, bg="gray", fg="white", command= actualizar)
boton_actualizar.grid(row=13, column=0, columnspan=3)

boton_eliminar = Button(frame, text="Eliminar", width=10, bg="gray", fg="white", command= eliminar)
boton_eliminar.grid(row=15, column=0, columnspan=3)


id_entry.bind("<KeyRelease>", evento_presionar_tecla_id)
edificio1_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio1)
edificio2_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio2)
edificio3_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio3)
edificio4_entry.bind("<KeyRelease>", evento_presionar_tecla_edificio4)


ventanaPrincipal.mainloop()