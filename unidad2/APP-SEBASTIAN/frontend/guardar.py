import requests

def guardar(nombre, ingrediente_principal, calorias, peso):
    datos = {
        "nombre": nombre,
        "ingrediente_principal": ingrediente_principal,
        "calorias": calorias,
        "peso": peso,
    }
    respuesta = requests.post("http://127.0.0.1:8000/api/Comida/", json=datos)

    if respuesta.status_code == 201:
        print("Guardado exitoso")
    else:
        print("Error al guardar")
