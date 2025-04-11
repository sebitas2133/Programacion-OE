import requests
from tkinter import messagebox

def guardar(nombre, ingrediente_principal, calorias, peso):
    datos = {
        "nombre": nombre,
        "ingrediente_principal": ingrediente_principal,
        "calorias": calorias,
        "peso": peso,
    }
    respuesta = requests.post("http://127.0.0.1:8000/api/Comida/", json=datos)

    if respuesta.status_code == 201:
        messagebox.showinfo("Exito", "Guardado exitoso")
        print("Guardado exitoso")
    else:
        messagebox.showerror("Error", "Error al guardar los datos")
        print("Error al guardar los datos")
