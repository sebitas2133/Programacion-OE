from tkinter import ttk


class Tabla():
     
    def __init__(self, frame, titulos, columnas, data):

        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("Treeview", background="#121212", foreground="white", fieldbackground="#121212", borderwidth=0, relief="flat")
        estilo.configure("Treeview.Heading", background="#gray16", foreground="white")

        estilo.map('Treeview', background=[('selected', 'gray')], foreground=[('selected', '#121212')])
    
        self.tabla = ttk.Treeview(frame, columns=columnas, show='headings')
        
        self.tabla.tag_configure('fila_par', background='gray4')
        self.tabla.tag_configure('fila_impar', background='#121212')

        for posicion in range(0, len(columnas)):
            self.tabla.heading(columnas[posicion], text=titulos[posicion])
        for index, elemento in enumerate(data):
            if index % 2 == 0:
                self.tabla.insert(parent='', index='end', values=elemento, tags=('fila_par',))
            else:
                self.tabla.insert(parent='', index='end', values=elemento, tags=('fila_impar',))

    
    def refrescar(self, data):
        self.tabla.delete(*self.tabla.get_children())
        for index, elemento in enumerate(data):
            if index % 2 == 0:
                self.tabla.insert(parent='', index='end', values=elemento, tags=('fila_par',))
            else:
                self.tabla.insert(parent='', index='end', values=elemento, tags=('fila_impar',))