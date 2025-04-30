from tkinter import *
import re
import requests

texto_validar_titulo = ""
texto_validar_autor = ""
texto_validar_genero = ""
texto_validar_año = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title('Interfaz de Libro')
ventanaPrincipal.geometry("500x340")
ventanaPrincipal.config(bg='alice blue')

titulo = StringVar(ventanaPrincipal)
autor = StringVar(ventanaPrincipal)
genero = StringVar(ventanaPrincipal)
año_publicacion = StringVar(ventanaPrincipal)
id = StringVar(ventanaPrincipal)

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$") 
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def validar_numeros(valor):
    patron = re.compile("^[0-9]*$") 
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True


def evento_presionar_tecla_titulo(event):
    global titulo
    global texto_validar_titulo

    if validar_letras(titulo):
        texto_validar_titulo = ""
    else:
        texto_validar_titulo = "Solo se permite letras"
    labelValidacionTitulo.config(text = texto_validar_titulo, fg="blue")

def evento_presionar_tecla_autor(event):
    global autor
    global texto_validar_autor

    if validar_letras(autor):
        texto_validar_autor= ""
    else:
        texto_validar_autor = "Solo se permite letras"
    labelValidacionAutor.config(text = texto_validar_autor, fg="blue")

def evento_presionar_tecla_genero(event):
    global genero
    global texto_validar_genero

    if validar_letras(genero):
        texto_validar_genero= ""
    else:
        texto_validar_genero = "Solo se permite letras"
    labelValidacionGenero.config(text = texto_validar_genero, fg="blue")

def evento_presionar_tecla_año(event):
    global año_publicacion
    global texto_validar_año

    if validar_numeros(año_publicacion):
        texto_validar_año= ""
    else:
        texto_validar_año = "Solo se permite numeros"
    labelValidacionAño_Publicacion.config(text = texto_validar_año, fg="blue")

def limpiar_campos():
    entryid.delete(0, END)
    entrytitulo.delete(0, END)
    entryautor.delete(0, END)
    entrygenero.delete(0, END)
    entryaño_publicacion.delete(0, END)

def b_guardar():
    data = {
        "titulo": entrytitulo.get(),
        "autor": entryautor.get(),
        "genero": entrygenero.get(),
        "año_publicacion": entryaño_publicacion.get()
    }
    response = requests.post("http://127.0.0.1:8000/api/Libro/", json=data)
    if response.status_code in (200, 201):
        print("Éxito. Libro guardado")
    limpiar_campos()

def b_consultar():
    libro_id = entryid.get()
    if libro_id:
        response = requests.get( "http://127.0.0.1:8000/api/Libro/"+ libro_id + "/")
        if response.status_code == 200:
            data = response.json()
            entrytitulo.delete(0, END)
            entrytitulo.insert(0, data['titulo'])
            entryautor.delete(0, END)
            entryautor.insert(0, data['autor'])
            entrygenero.delete(0, END)
            entrygenero.insert(0, data['genero'])
            entryaño_publicacion.delete(0, END)
            entryaño_publicacion.insert(0, data['año_publicacion'])
        else:
            print("Error.","Libro no encontrado")

def b_actualizar():
    libro_id = entryid.get()
    if libro_id:
        data = {
            "titulo": entrytitulo.get(),
            "autor": entryautor.get(),
            "genero": entrygenero.get(),
            "año_publicacion": entryaño_publicacion.get()
        }
        response = requests.put("http://127.0.0.1:8000/api/Libro/" + libro_id + "/", json=data)
        if response.status_code == 200:
            print("Éxito. Libro actualizado")
    limpiar_campos()

def b_eliminar():
    libro_id = entryid.get()
    if libro_id:
        response = requests.delete("http://127.0.0.1:8000/api/Libro/" + libro_id + "/")
        if response.status_code == 204:
            print("Éxito. Libro eliminado")
    limpiar_campos()

frame = Frame(ventanaPrincipal,bg='alice blue')
frame.pack()

labelmensaje = Label(frame, text="Hola! Por favor ingresa los siguientes datos del libro:", font=("Times New Roman", 12, "bold"), bg= "PaleVioletRed2", fg= "white")
labelmensaje.grid(row=0, column=0, columnspan=4, pady=5)

labelid = Label(frame, text="id",bg='alice blue')
labelid.grid(row=1, column=0,sticky='we')
entryid = Entry(frame, textvariable= id, width=15)
entryid.grid(row=1, column=1, sticky='w')

labeltitulo =Label(frame, text="Título",bg='alice blue').grid(row=2, column=0,sticky='we')
entrytitulo = Entry(frame, textvariable= titulo,width=30)
entrytitulo.grid(row=2, column=1,sticky='w')
entrytitulo.bind("<KeyRelease>", evento_presionar_tecla_titulo)
labelValidacionTitulo =Label(frame, text="",bg='alice blue')
labelValidacionTitulo.grid(row=2, column=2, padx=10)

labelautor =Label(frame, text="Autor",bg='alice blue').grid(row=3, column=0,sticky='we')
entryautor = Entry(frame, textvariable= autor,width=30)
entryautor.grid(row=3, column=1,sticky='w')
entryautor.bind("<KeyRelease>", evento_presionar_tecla_autor)
labelValidacionAutor=Label(frame, text="",bg='alice blue')
labelValidacionAutor.grid(row=3, column=2, padx=10)

labelgenero = Label(frame, text="Género",bg='alice blue').grid(row=4, column=0,sticky='we')
entrygenero = Entry(frame, textvariable= genero,width=30)
entrygenero.grid(row=4, column=1,sticky='w')
entrygenero.bind("<KeyRelease>", evento_presionar_tecla_genero)
labelValidacionGenero =Label(frame, text="",bg='alice blue')
labelValidacionGenero.grid(row=4, column=2, padx=10)

labelaño_publicacion = Label(frame, text="Año de Publicación",bg='alice blue').grid(row=5, column=0,sticky='we')
entryaño_publicacion = Entry(frame, textvariable= año_publicacion,width=30)
entryaño_publicacion.grid(row=5, column=1,sticky='w')
entryaño_publicacion.bind("<KeyRelease>", evento_presionar_tecla_año)
labelValidacionAño_Publicacion =Label(frame, text="",bg='alice blue')
labelValidacionAño_Publicacion.grid(row=5, column=2, padx=10)

botonguardar= Button(frame, text="Guardar", width=9,font=("Arial", 10, "bold"), bg="PaleVioletRed2", fg="white",relief="flat", command=b_guardar)
botonguardar.grid(row=6, column=1, pady=3, padx=5, sticky="we")

boton_consultar = Button(frame, text="Consultar", width=9,font=("Arial", 10, "bold"), bg="PaleVioletRed2", fg="white",relief="flat", command=b_consultar)
boton_consultar.grid(row=1, column=1, padx=5, sticky='e')

boton_actualizar = Button(frame, text="Actualizar", width=9,font=("Arial", 10, "bold"), bg="PaleVioletRed2", fg="white",relief="flat", command=b_actualizar)
boton_actualizar.grid(row=7, column=1, pady=3, padx=5, sticky="we")

boton_eliminar = Button(frame, text="Eliminar", width=9,font=("Arial", 10, "bold"), bg="PaleVioletRed2", fg="white",relief="flat", command=b_eliminar)
boton_eliminar.grid(row=8, column=1, pady=3, padx=5, sticky="we")

ventanaPrincipal.mainloop()