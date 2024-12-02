# Sistema de Gestión para una Biblioteca
Trabajo Practico Obligatorio Algoritmos I - UADE  
Autores: Barrón, Melina -  Di Laudo, Camila - Melián, Daniela | Equipo 8

# 🎯 Objetivo
Crear un sistema de gestión para bibliotecas que permita realizar un control del estado de los libros, realizar acciones sobre los mismos y un posterior seguimiento del comportamiento de los usuarios de la misma. 

# 🗺️ Arquitectura 
![Diagrama de Arquitectura](./Diagrama-TPO.drawio.png)

# 🐍 Funciones

### Barron, Melina
 - recomendar_libros  
 - login_usuario  
 - cambiar_status_usuario
 - borrar_libro
 - ver_propio_historial
    
### Di Laudo, Camila  
 - registrar_usuarios  
 - editar_libros 
 - main
### Melian, Daniela  
  - busqueda_libros  
 - cargar_libros  
 - obtener_libros
 - agregar_libro_historial  

## 🚀 Getting Started

### Pre - requisitos

> #### Python 
>
> - Ingresar a la sección Descargas de [Python](https://www.python.org/downloads/).
> - Descargar la última versión o >= to 3.8.0.
> - Instalar Python y setear las variables de entorno.
> - Verificar que se haya instalado correctamenete con *python --version* desde cualquier consola/terminal (PowerShell, CMD, bash).
> ```
> PS C:\Users\you_user> python --version
> Python 3.8.0
> ```
#### Entorno virtual de Python
>
> Los entornos virtuales de Python son útiles para evitar conflictos entre distintos proyectos que pueden utilizar distintas versiones de librerías.
> - Ubicado desde una consola en la raíz del proyecto, ejecutar el siguiente comando:
> ```
> python -m venv .venv
> ```
> - Al finalizar, se debería haber creado una carpeta con nombre " v" la raíz del proyecto.
> - Para acitvar el entorno virtual, ejecutar el siguiente comando:
> -- En Linux bash/zsh -> ``` $ source .venv/bin/activate ```
> -- En Windows cmd.exe -> ``` .\.venv\Scripts\activate.bat ```
> -- En Windows PowerShell -> ``` .\.venv\Scripts\Activate.ps1 ```
> - Para indagar más sobre el tema, ingresar a la siguiente url [venv](https://docs.python.org/3/library/venv.html).


### Instalación

>
> #### Python Libs
> - Es necesario instalar en el proyecto los módulos/librerías que se usan como dependencias desde el archivo *requirements.txt*, luego de activar el virtual enviroment vas a ejecutar el siguiente comando:
> ```
> (.venv) PS C:\Users\you_user\you_workspace\biblioteca> pip install -r requirements.txt
> ```
> - Finalizada la instalación, se puede verificar la instalación de los módulos con el comando *pip freeze* y se debe observar lo siguente:
> ```
> (.venv) PS C:\Users\you_user\you_workspace\biblioteca> pip freeze
> ...
> black==24.8.0
> colorama==0.4.6
> pytest==8.3.4
> pytest-html==4.1.1
> pytest-metadata==3.1.1
> ...
>```

### Ejecucion

>
> #### Python Libs
> - Desde la terminal: Activar el venv y ejecutar el siguiente comando 
> ```
> (.venv) PS C:\Users\you_user\you_workspace\biblioteca> pytest .\tests\ --html=report.html --self-contained-html --tb=long --log-level=DEBUG -v
> ```
> - Desde pycharm: Botón derecho sobre cualquier archivo de test y elegir la opción "Run"


