import utils.users_utils as us
import utils.book_utils as bu
import data_store.users_data as ud

# TODO: main: Dani -> agregar funcion de historial,  y de editar libro. Meli -> carteles y prints del sistema en el
#  login , recomendaciones

# DECLARACIÓN DE VARIABLES :
Lista_Usuarios = []
Lista_Contrasenas = []
bibliotecario = 1
cliente = 2
usuario_contra_incorrecto = 3

# PROGRAMA PRINCIPAL :
print("Bienvenido a la biblioteca...")
print("1- Iniciar Sesión.")
print("2- Registrarse.")

numero = input("Ingrese un número : ")
while numero != "1" and numero != "2":
    numero = input("Error. Ingrese un número correcto : ")
if numero == "1":

    usuario = input("Ingrese nombre de usuario:  ")

    iniciar_sesion = us.login_usuario(usuario)
else:
    usuario = input("Ingrese tipo de usuario:  ")
    if usuario == bibliotecario:
        contrasenia_general = input("ingresa la codigo de acceso: ")
        while contrasenia_general != ud.contrasenia_general:
            print("Codigo de acceso incorrecto")
            contrasenia_general = input("ingresa la codigo de acceso: ")

        nombre_usuario = input("Ingrese un nombre de usuario : ")
        contrasena = input("Ingrese la contrasena del usuario: ")

        verificar_contrasena = input("Volvé a ingresar la contrasena : ")
        registrar = us.registrar_usuario(nombre_usuario=nombre_usuario, contrasenia_usuario=contrasena)
        while registrar is False:
            print("Usuario o contraseña incorrecto. ")
            usuario = input("Ingrese un nombre de usuario: ")
            contrasena = input("Ingrese la contrasena del usuario: ")
            verificar_contrasena = input("Volvé a ingresar la contrasena : ")
            registrar = us.registrar_usuario(usuario, contrasena, verificar_contrasena)
        print("Usuario registrado correctamente !")
        iniciar_sesion = us.login_usuario(nombre_usuario, contrasena)

while iniciar_sesion == usuario_contra_incorrecto:
    print("Su usuario o contrasenia es incorrecta")
    usuario = input("Ingrese nombre de usuario:  ")

    iniciar_sesion = us.login_usuario(usuario)

# SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
if iniciar_sesion == cliente:
    print("1- Buscar libros.")
    print("2- Obtener libro.")
    numero = input("Ingresá un número : ")
    while numero != "1" and numero != "2":
        print("1- Buscar libros.")
        print("2- Obtener libro.")
        numero = input("Ingresá un número : ")
    if numero == "1":
        Clave = str(input("Ingrese el campo para realizar la busqueda : "))
        Valor = str(input("Ingrese la valor que desea registrar: "))
        buscar_libros = bu.busqueda_libros(Clave, Valor)
    else:
        ISBN = int(input("Ingrese el ISBN del libro que quiere obtener: "))
        alquilar_libro = bu.obtener_libro(ISBN)

# SI EL USUARIO QUE INICIA SECIÓN ES EL BIBLIOTECARIO
elif iniciar_sesion == bibliotecario:
    # TODO: la variable bilbiotecario no esta definida, o deberia pasarse a un string
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
        if numero == "1":
            titulo = input("Ingrese el titulo : ")
            autor = input("Ingrese el autor : ")
            genero = input("Ingrese el genero : ")
            ISBN = input("Ingrese el ISBN : ")
            editorial = input("Ingrese el editorial : ")
            anio_publicacion = input("Ingrese el anio publicacion : ")
            serie_libros = input("Ingrese el serie_libros : ")
            nro_paginas = input("Ingrese el nro_paginas : ")
            cant_ejemplares = input("Ingrese el la cantidad de ejemplares : ")
            registrar_libros = bu.cargar_libros(
                titulo,
                autor,
                genero,
                ISBN,
                editorial,
                anio_publicacion,
                serie_libros,
                nro_paginas,
                cant_ejemplares,
            )
        elif numero == "2":
            ISBN_editar = int(input("Ingrese el ISBN que quiere editar: "))
            editar = bu.editar_libros(ISBN_editar)
        else:
            libro = input("Ingrese el libro de su consulta")
            libro_buscado = bu.busqueda_libros("titulo", libro)
            if libro_buscado == "disponible":
                print("lo tenemos")
            elif libro_buscado == "en_espera":
                print("Ahora está reservado, pero vuelve")
            else:
                print("No contamos con ese libro en nuestra biblioteca")
