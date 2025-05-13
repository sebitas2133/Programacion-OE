import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/Comida'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, nombre, ingrediente_principal, calorias, peso):
        try:

            data = {
                "nombre": nombre,
                "ingrediente_principal": ingrediente_principal,
                "calorias": calorias,
                "peso": peso
            }
            resultado = requests.post(self.url + "/", json=data) 
            return resultado.status_code
        except:
            pass

    def actualizar(self, id, nombre, ingrediente_principal, calorias, peso):
        comida_id = id
        if comida_id:
            data = {
                "nombre": nombre,
                "ingrediente_principal": ingrediente_principal,
                "calorias": int(calorias),
                "peso": int(peso)
            }
            response = requests.put(self.url + "/" + comida_id + "/", json=data)
            return response.status_code

    def consultar(self, id):
        response = requests.get(self.url + '/' + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    
    def consultar_todo(self, nombre, ingrediente_principal, calorias, peso):
        params = {}
        if calorias != '':
            params['calorias'] = calorias
        if nombre != '':
            params['nombre'] = nombre
        if ingrediente_principal != '':
            params['ingrediente_principal'] = ingrediente_principal
        if peso != '':
            params['peso'] = peso

        resultado = requests.get(self.url, params=params)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id) + '/')
        return resultado.status_code
    



