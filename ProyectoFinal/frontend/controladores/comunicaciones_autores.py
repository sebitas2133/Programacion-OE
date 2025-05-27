import requests

class Comunicacion_autores():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/autores'
        self.ventanaPrincipal = ventanaPrincipal
        pass


    def registrar(self, nombre,nacionalidad, edad):
        try:
            data = {
                'nombre': nombre,
                'nacionalidad': nacionalidad,
                'edad': int(edad)
            }
            resultado = requests.post(self.url + "/", json=data) 
            return resultado.status_code
        except:
            pass

    def actualizar(self, id, nombre, nacionalidad, edad):
            autor_id = id
            if autor_id:
                data = {
                    'nombre': nombre,
                    'nacionalidad': nacionalidad,
                    'edad': int(edad)
                }
                resultado = requests.put(self.url + "/" + autor_id + "/", json=data)
                return resultado.status_code
        
    
    
    def registros_existentes(self, nombre, nacionalidad, edad):
        params = {}
        if nombre != '':
            params['nombre'] = nombre
        if nacionalidad != '':
            params['nacionalidad'] = nacionalidad
        if edad != '':
            params['edad'] = edad

        resultado = requests.get(self.url, params=params)
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + id + '/')
        return resultado.status_code
    

