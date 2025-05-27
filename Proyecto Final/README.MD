# Proyecto Final POE
Este proyecto es una aplicación desarrollada en Python. Utiliza Django exclusivamente como backend para gestionar la base de datos, mientras que la interfaz de usuario es una aplicación de escritorio que se ejecuta localmente desde el archivo principal ubicado en la carpeta `frontend`.

## Requisitos del sistema
- Python 3.10 o superior
- Visual Studio Code (con la extensión Python instalada)
- pip (administrador de paquetes de Python)
- SQLite (incluido con Python)

## Instrucciones de instalación
1. Clona o descarga el proyecto y ábrelo en Visual Studio Code.

2. Instala las dependencias necesarias:

   pip install -r requirements.txt

3. Aplica las migraciones para configurar la base de datos:

   python manage.py migrate

4. Inicia el servidor de Django para que la interfaz pueda comunicarse con el backend:

   python manage.py runserver

## Cómo ejecutar la aplicación
Una vez configurada la base de datos y con el servidor Django corriendo, ejecuta la aplicación de escritorio desde el archivo principal:

   cd frontend  
   python main.py

Esto abrirá la interfaz gráfica del sistema, conectada al backend Django que gestiona el almacenamiento de datos.

## Notas adicionales
- No es necesario acceder a través del navegador.  
- El backend Django funciona en segundo plano para procesar y almacenar los datos ingresados desde la interfaz.  
- Asegúrate de que la base de datos esté correctamente migrada antes de ejecutar la interfaz.  
- El servidor Django debe estar activo para que la interfaz funcione correctamente.
