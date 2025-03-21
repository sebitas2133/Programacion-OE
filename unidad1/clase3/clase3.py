from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

ventanaPrincipal = Tk()
ventanaPrincipal.title("Prueba de eventos")

def action_click(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def presionar_tecla(event):
    print("pressed", repr(event.char))

def el_usuario_quiere_salir():
    if askyesno("Salir", "¿Está seguro que desea salir?"):
        ventanaPrincipal.destroy()

frame = Frame(ventanaPrincipal, width=500, height=500)
frame.bind("<Button-1>", action_click)
frame.bind("<Key>", presionar_tecla)
frame.pack()

ventanaPrincipal.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)
ventanaPrincipal.mainloop()