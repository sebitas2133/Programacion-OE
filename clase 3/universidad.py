from tkinter import Frame, Tk, Label, Entry, Button


ventanaPrincipal = Tk()
ventanaPrincipal.title("Universidad")

frame= Frame(ventanaPrincipal, width=500 , height=500)
frame.pack_propagate(False)
frame.pack()

edificio1 = Label(frame, text= "Facultad de ingenieria")
edificio1.pack(anchor="center", pady= 5)
edificio1 = Entry(frame)
edificio1.pack(anchor="center", pady= 5)

edificio2 = Label(frame, text= "Facultad de Medicina")
edificio2.pack(anchor="center", pady= 5)
edificio2 = Entry(frame)
edificio2.pack(anchor="center", pady= 5)

edificio3 = Label(frame, text= "Facultad de Educacion")
edificio3.pack(anchor="center", pady= 5)
edificio3 = Entry(frame)
edificio3.pack(anchor="center", pady= 5)

edificio4 = Label(frame, text= "Edificio administrativo")
edificio4.pack(anchor="center", pady= 5)
edificio4 = Entry(frame)
edificio4.pack(anchor="center", pady= 5)

boton = Button(frame, text= "Guardar")
boton.pack(anchor="center", pady=20)

ventanaPrincipal.mainloop()
