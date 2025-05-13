import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/Libro'
        self.ventanaPrincipal = ventanaPrincipal
        pass


    def guardar(self, titulo, autor, genero, año_publicacion):
        try:
            data = {
                'titulo': titulo,
                'autor': autor,
                'genero': genero,
                'año_publicacion': int(año_publicacion)
            }
            resultado = requests.post(self.url + "/", json=data) 
            return resultado.status_code
        except:
            pass

    def actualizar(self, id, titulo, autor, genero, año_publicacion):
            libro_id = id
            if libro_id:
                data = {
                    'titulo': titulo,
                    'autor': autor,
                    'genero': genero,
                    'año_publicacion': int(año_publicacion)
                }
                resultado = requests.put(self.url + "/" + libro_id + "/", json=data)
                return resultado.status_code
        
    def consultar(self, id):
         response = requests.get(self.url + '/' + str(id))
         if response.status_code == 200:
            return response.json()
         else:
            return None
    
    
    def consultar_todo(self, titulo, autor, genero, año_publicacion):
        params = {}
        if titulo != '':
            params['titulo'] = titulo
        if autor != '':
            params['autor'] = autor
        if genero != '':
            params['genero'] = genero
        if año_publicacion != '':
            params['año_publicacion'] = año_publicacion

        resultado = requests.get(self.url, params=params)
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + id + '/')
        return resultado.status_code
    

