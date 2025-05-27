import requests
import time
import threading


URL_AUTORES = "http://127.0.0.1:8000/api/autores/"
URL_LIBROS = "http://127.0.0.1:8000/api/libros/"

def generar_respaldo_autores():
    try:
        response = requests.get(URL_AUTORES)
        response.raise_for_status()
        autores = response.json()

        with open("backend/Respaldos/respaldo_autores.txt", "w", encoding="utf-8") as archivo:
            for autor in autores:
                archivo.write(f"ID: {autor['id']}\n")
                archivo.write(f"Nombre: {autor['nombre']}\n")
                archivo.write(f"Nacionalidad: {autor['nacionalidad']}\n")
                archivo.write(f"Edad: {autor['edad']}\n\n")
        print(f"[✔] respaldo_autores.txt actualizado")
    except Exception as e:
        print(f"[❌] Error al generar respaldo de autores: {e}")

def generar_respaldo_libros():
    try:
        response = requests.get(URL_LIBROS)
        response.raise_for_status()
        libros = response.json()

        with open("backend/Respaldos/respaldo_libros.txt", "w", encoding="utf-8") as archivo:
            for libro in libros:
                archivo.write(f"ID: {libro['id']}\n")
                archivo.write(f"Título: {libro['titulo']}\n")
                archivo.write(f"Autor: {libro['autor']}\n")
                archivo.write(f"Género: {libro['genero']}\n")
                archivo.write(f"Páginas: {libro['paginas']}\n")
                archivo.write(f"Año: {libro['año_publicacion']}\n\n")
        print(f"[✔] respaldo_libros.txt actualizado")
    except Exception as e:
        print(f"[❌] Error al generar respaldo de libros: {e}")

def respaldo_periodico():
    while True:
        print("\n[⏱] Generando respaldo automático...")
        generar_respaldo_autores()
        generar_respaldo_libros()
        time.sleep(60) 

def iniciar_respaldo():
    respaldo_thread = threading.Thread(target=respaldo_periodico, daemon=True)
    respaldo_thread.start()
    print("🔄 Respaldos automáticos en segundo plano cada 60 segundos.")

