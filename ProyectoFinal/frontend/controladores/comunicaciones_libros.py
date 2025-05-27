import requests

class Comunicacion_libros():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/libros'
        self.ventanaPrincipal = ventanaPrincipal
        pass


    def registrar(self, titulo, autor, genero, paginas, año_publicacion):
        try:
            data = {
                'titulo': titulo,
                'autor': autor,
                'genero': genero,
                'paginas': int(paginas),
                'año_publicacion': int(año_publicacion)
            }
            resultado = requests.post(self.url + "/", json=data) 
            return resultado.status_code
        except:
            pass

    def actualizar(self, id, titulo, autor, genero,paginas, año_publicacion):
            libro_id = id
            if libro_id:
                data = {
                    'titulo': titulo,
                    'autor': autor,
                    'genero': genero,
                    'paginas': int(paginas),
                    'año_publicacion': int(año_publicacion)
                }
                resultado = requests.put(self.url + "/" + libro_id + "/", json=data)
                return resultado.status_code
        
    
    
    def registros_existentes(self, titulo, autor, genero, paginas, año_publicacion):
        params = {}
        if titulo != '':
            params['titulo'] = titulo
        if autor != '':
            params['autor'] = autor
        if genero != '':
            params['genero'] = genero
        if paginas != '':
            params['paginas'] = paginas
        if año_publicacion != '':
            params['año_publicacion'] = año_publicacion

        resultado = requests.get(self.url, params=params)
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + id + '/')
        return resultado.status_code
    

