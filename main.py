import utils.users_utils as us
import utils.book_utils as bu
# DECLARACIÓN DE VARIABLES :
Lista_Usuarios = []
Lista_Contrasenas = []

# PROGRAMA PRINCIPAL :
print("Bienvenido a la biblioteca...")
print("1- Iniciar Sesión.")
print("2- Registrarse.")

numero = input("Ingrese un número : ")
while numero != "1" and numero != "2":
    numero = input("Error. Ingrese un número correcto : ")
if numero == "1":

    usuario = input("Ingrese tipo de usuario: ")

    iniciar_sesion = us.login_usuario(usuario)
else:
    registrar = us.registrar_usuario()

# SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
if iniciar_sesion == "cliente":
    print("1- Buscar libros.")
    print("2- Obtener libro.")
    numero = input("Ingresá un número : ")
    while numero != "1" and numero != "2":
        print("1- Buscar libros.")
        print("2- Obtener libro.")
        numero = input("Ingresá un número : ")
    if numero == "1":
        #TODO: la clave y el valor la tiene que pasar el usuario por teclado
        buscar_libros = bu.busqueda_libros(Clave, Valor)
    else:
        # TODO: el ISBN lo tiene que pasar el usuario por teclado
        alquilar_libro = bu.obtener_libro(ISBN)

# SI EL USUARIO QUE INICIA SECIÓN ES EL BIBLIOTECARIO
else:
    #TODO: la variable bilbiotecario no esta definida, o deberia pasarse a un string
    if iniciar_sesion == bibliotecario:
        print("1- Cargar libros.")
        print("2- Editar libro.")
        print("3- Cambiar Status.")
        numero = input("Ingresá un número : ")
        while numero != "1" and numero != "2" and numero != "3":
            print("1- Cargar libros.")
            print("2- Editar libro.")
            print("3- Cambiar Status.")
            numero = input("ERROR. Ingresá un número : ")
        #TODO: los datos de registrar_libro, editar_libro y status_libro deberia pasarlos por teclado el usuario
        if numero == "1":
            registrar_libros = cargar_libros(titulo, autor, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas, cant_ejemplares)
        elif numero == "2":
            ISBN_editar = int(input("Ingrese el ISBN que quiere editar: "))
            editar = editar_libros(titulo, autor, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas, cant_ejemplares, ISBN_editar)
        else: 
            libro = input("Ingrese el libro de su consulta")
            libro_buscado = estatus_libros(libro)
            if libro_buscado == "disponible":
                print("lo tenemos")
            elif libro_buscado == "en_espera":
                print("Ahora está reservado, pero vuelve")
            else:
                print("No contamos con ese libro en nuestra biblioteca")
