import vistas.interfaz_bienvenida as Interfaz_bienvenida
import controladores.respaldos

if __name__ == "__main__":
    interfaz_bienvenida = Interfaz_bienvenida.Interfaz_bienvenida()
    interfaz_bienvenida.mostrar_bienvenida()
    controladores.respaldos.iniciar_respaldo()
    interfaz_bienvenida.ventanaPrincipal.mainloop()
    