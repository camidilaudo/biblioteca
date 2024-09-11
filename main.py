import utils.users_utils as us
import utils.book_utils as bu
import data_store.users_data as ud
import utils.print_utils as pu

# TODO: main: Dani -> agregar funcion de historial,  y de editar libro. Meli -> carteles y prints del sistema en el
#  login , recomendaciones

# DECLARACIÓN DE VARIABLES :
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
    contrasenia = input("Ingrese la contrasena del usuario: ")

    iniciar_sesion = us.login_usuario(usuario, contrasenia)
else:
    print("1- Biliotecario.")
    print("2- Cliente.")
    usuario = input("Ingrese un número para el tipo de usuario:  ")
    if usuario == bibliotecario:
        contrasena_general = input("Ingrese el código de acceso: ")
        while contrasena_general != ud.contrasenia_general:
            contrasena_general = input("Error. Ingresa el código de acceso correcto: ")

    nombre_usuario = input("Ingrese un nombre de usuario : ")
    contrasenia = input("Ingrese la contrasena del usuario: ")
    verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    while contrasenia != verificar_contrasena:
        print("Error. Las contraseñas no coinciden")
        contrasenia = input("Ingrese la contrasena del usuario: ")
        verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    registrar = us.registrar_usuario(usuario, nombre_usuario, contrasenia)
    while registrar is False:
        print("El usuario ingresado ya existe. Volver a intentar: ")
        usuario = input("Ingrese un nombre de usuario: ")
        registrar = us.registrar_usuario(usuario, contrasenia, verificar_contrasena)
    print("Usuario registrado correctamente !")
    iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

while iniciar_sesion == usuario_contra_incorrecto:
    print("Su usuario o contrasenia es incorrecta")
    usuario = input("Ingrese nombre de usuario:  ")
    contrasenia = input("Ingrese la contrasena del usuario: ")
    iniciar_sesion = us.login_usuario(usuario, contrasenia)

# SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
if iniciar_sesion == cliente:
    print("1- Buscar libros.")
    print("2- Obtener libro.")
    print("3- Recomendaciones.")
    numero = input("Ingresá un número : ")
    while numero != "1" and numero != "2" and numero != "3":
        print("1- Buscar libros.")
        print("2- Obtener un libro.")
        print("3- Recomendaciones.")
        numero = input("Error. Ingresá un número correcto : ")
    if numero == "1":
        Clave = str(input("Ingrese el campo para realizar la busqueda : "))
        Valor = str(input("Ingrese la valor que desea registrar: "))
        buscar_libros = bu.busqueda_libros(Clave, Valor)
    elif numero == "2":
        ISBN = int(input("Ingrese el ISBN del libro que quiere obtener: "))
        alquilar_libro = bu.obtener_libro(ISBN)
    else:
        genero_libro = input("Ingrese un género: ")
        recomentacion_libro = bu.recomendaciones(genero_libro, usuario)
        pu.imprimir_libro(recomentacion_libro)

# SI EL USUARIO QUE INICIA SECIÓN ES EL BIBLIOTECARIO
elif iniciar_sesion == bibliotecario:
    if iniciar_sesion == bibliotecario:
        print("1- Cargar libros.")
        print("2- Editar libro.")
        print("3- Alquilar libro.")
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
            libro = bu.obtener_libro(ISBN=ISBN_editar)
            while libro is None:
                print(
                    "El ISBN es incorrecto o no se encuentra el libro registrado. Por favor pruebe otra vez: "
                )
                ISBN_editar = int(input("Ingrese el ISBN del libro que quiere editar: "))
                indice_editar = input("Ingrese el índice que quiere editar: ")
                valor_editar = input("Ingrese el valor a reemplazar: ")
                encontrar_libro = bu.obtener_libro(ISBN_editar, indice_editar, valor_editar)

            print("Libro encontrado: ")

            pu.imprimir_libro(libro)

            numero = int(input("Ingresá un número para editar : "))
            while 7 < numero or numero < -1:
                print("El numero ingresado es incorrecto.")
                numero = input("Ingresá un número para editar : ")
            if numero != -1:
                nuevo_valor = input("Ingresá el nuevo valor:")
                editar = bu.editar_libros(
                    ISBN=ISBN_editar, indice=numero, valor=nuevo_valor
                )
            print("Libro editado con éxito: ")
            pu.imprimir_libro(libro)
        else:
            titulo = input("Ingrese el nombre del libro que quiere alquilar: ")
            libros = bu.busqueda_libros("titulo", titulo)
            print(f"Estos son los libros que coinciden con tu busqueda: {libros}")
            continuar = int(input("Presione 1 para continuar, 2 si desea realizar otra busqueda o -1 para salir: "))
            while continuar == 2:
                titulo = input("Ingrese el nombre del libro que quiere alquilar: ")
                libros = bu.busqueda_libros("titulo", titulo)
                print(f"Estos son los libros que coinciden con tu busqueda: {libros}")
            if continuar == 1:
                isbn = input("Ingrese el ISBN del libro que quiere alquilar: ")
                cantidad_pedidos = input("Ingrese la cantidad de pedidos: ")
                usuario = input("Ingrese el nombre de ususario que va a alquilarlos: ")
                libro_alquilado = bu.alquilar_libro(isbn, cantidad_pedidos, usuario)
                print(f"El libro se alquilo con exito, quedan {libro_alquilado[1]} unidades disponibles.")
