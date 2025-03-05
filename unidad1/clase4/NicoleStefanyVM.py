from tkinter import *
import re

texto_validar_titulo = ""
texto_validar_autor = ""
texto_validar_genero = ""
texto_validar_año = ""

ventanaPrincipal = Tk()
ventanaPrincipal.title('Interfaz de Libro')
ventanaPrincipal.geometry("400x210")

titulo = StringVar(ventanaPrincipal)
autor = StringVar(ventanaPrincipal)
genero = StringVar(ventanaPrincipal)
año_publicacion = StringVar(ventanaPrincipal)

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


frame = Frame(ventanaPrincipal)
frame.pack()

labelmensaje = Label(frame, text="Hola! Por favor ingresa los siguientes datos del libro:", font=("Times New Roman", 12, "bold"), bg= "light pink", fg= "white")
labelmensaje.grid(row=0, column=0, columnspan=3, pady=5)


labeltitulo =Label(frame, text="Título:").grid(row=1, column=0)
entrytitulo = Entry(frame, textvariable= titulo)
entrytitulo.grid(row=1, column=1)
entrytitulo.bind("<KeyRelease>", evento_presionar_tecla_titulo)
labelValidacionTitulo =Label(frame, text="")
labelValidacionTitulo.grid(row=1, column=2, padx=10)

labelautor =Label(frame, text="Autor:").grid(row=2, column=0)
entryautor = Entry(frame, textvariable= autor)
entryautor.grid(row=2, column=1)
entryautor.bind("<KeyRelease>", evento_presionar_tecla_autor)
labelValidacionAutor=Label(frame, text="")
labelValidacionAutor.grid(row=2, column=2, padx=10)

labelgenero = Label(frame, text="Género:").grid(row=3, column=0)
entrygenero = Entry(frame, textvariable= genero)
entrygenero.grid(row=3, column=1)
entrygenero.bind("<KeyRelease>", evento_presionar_tecla_genero)
labelValidacionGenero =Label(frame, text="")
labelValidacionGenero.grid(row=3, column=2, padx=10)

labelaño_publicacion = Label(frame, text="Año de Publicación:").grid(row=4, column=0)
entryaño_publicacion = Entry(frame, textvariable= año_publicacion)
entryaño_publicacion.grid(row=4, column=1)
entryaño_publicacion.bind("<KeyRelease>", evento_presionar_tecla_año)
labelValidacionAño_Publicacion =Label(frame, text="")
labelValidacionAño_Publicacion.grid(row=4, column=2, padx=10)

boton = Button(frame, text="Guardar", width=9,font=("Times New Roman", 10, "bold"), bg="light pink", fg="white")
boton.grid(row=5, column=0, columnspan=2, pady=10)

ventanaPrincipal.mainloop()