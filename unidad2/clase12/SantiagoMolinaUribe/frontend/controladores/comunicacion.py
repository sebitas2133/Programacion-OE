import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/universidad/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, edificio1, edificio2, edificio3, edificio4):
        try:

            data = {
                "edificio1": edificio1,
                "edificio2": edificio2,
                "edificio3": edificio3,
                "edificio4": edificio4
            }
            resultado = requests.post(self.url, json=data) 
            return resultado.status_code
        except:
            pass

    def actualizar(self, id, edificio1, edificio2, edificio3, edificio4):
        universidad_id = id
        if universidad_id:
            data = {
                "edificio1": edificio1,
                "edificio2": edificio2,
                "edificio3": edificio3,
                "edificio4": edificio4
            }
            response = requests.put(self.url + universidad_id + "/", json=data)
            return response.status_code

    def consultar(self, id):
        response = requests.get(self.url + str(id))
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    
    def consultar_todo(self, edificio1, edificio2, edificio3, edificio4):
        params = {}
        if edificio1 != '':
            params['edificio1'] = edificio1
        if edificio2 != '':
            params['edificio2'] = edificio2
        if edificio3 != '':
            params['edificio3'] = edificio3
        if edificio4 != '':
            params['edificio4'] = edificio4

        resultado = requests.get(self.url, params=params)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url  + str(id) + '/')
        return resultado.status_code