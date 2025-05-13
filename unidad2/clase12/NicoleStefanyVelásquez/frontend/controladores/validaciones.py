import re

class Validaciones():
    
    def __init__(self):
        pass
    
    def validar_letras(self,valor):
        patron = re.compile("^[A-Za-zñÑ ]*$") 
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True

    def validar_numeros(self, valor):
        patron = re.compile("^[0-9]*$") 
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True

