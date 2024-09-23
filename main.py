import utils.users_utils as us
import utils.book_utils as bu
import data_store.users_data as ud
import utils.print_utils as pu
import data_store.books_data as bd
import constantes as c


# PROGRAMA PRINCIPAL :
def main():
    print("Bienvenido a la biblioteca...")
    print("1- Iniciar Sesión.")
    print("2- Registrarse.")

    # Ingresar al sistema como usuario pre - existente
    numero = int(input("Ingrese un número : "))
    while numero not in c.tipos_usuario:
        numero = int(input("Error. Ingrese un número correcto : "))
    if numero == 1:

        usuario = input("Ingrese nombre de usuario:  ")
        contrasenia = input("Ingrese la contrasena del usuario: ")

        iniciar_sesion = us.login_usuario(usuario, contrasenia)

    # Ingresar al sistema creando un nuevo usuario
    else:
        print("1- Biliotecario.")
        print("2- Cliente.")
        usuario = input("Ingrese un número para el tipo de usuario:  ")
        if usuario == c.bibliotecario:
            contrasena_general = input("Ingrese el código de acceso: ")
            while contrasena_general != ud.contrasenia_general:
                contrasena_general = input("Error. Ingresa el código de acceso correcto: ")
        registrar = False
        while registrar is False:
            nombre_usuario = input("Ingrese un nombre de usuario : ")
            contrasenia = input("Ingrese la contrasena del usuario: ")
            verificar_contrasena = input("Volvé a ingresar la contrasena : ")
            while contrasenia != verificar_contrasena:
                print("Error. Las contraseñas no coinciden")
                contrasenia = input("Ingrese la contrasena del usuario: ")
                verificar_contrasena = input("Volvé a ingresar la contrasena : ")
            registrar = us.registrar_usuario(usuario, nombre_usuario, contrasenia)
            if registrar is False:
                print("El usuario ingresado ya existe. Volver a intentar: ")

        print("Usuario registrado correctamente !")
        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

    while iniciar_sesion not in c.tipos_usuario:
        print("Su usuario o contrasenia es incorrecta")
        usuario = input("Ingrese nombre de usuario:  ")
        contrasenia = input("Ingrese la contrasena del usuario: ")
        iniciar_sesion = us.login_usuario(usuario, contrasenia)

    # SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
    if iniciar_sesion == c.cliente:
        print("1- Buscar libros.")
        print("2- Obtener libro.")
        print("3- Recomendaciones.")
        print("4- Ver mi historial")
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
        elif numero == "4":
            mi_historial = us.ver_propio_historial
            print(mi_historial)
        else:
            genero_libro = input("Ingrese un género: ")
            recomentacion_libro = bu.recomendaciones(genero_libro, usuario)
            pu.imprimir_libro(recomentacion_libro)

    # SI EL USUARIO QUE INICIA SECIÓN ES EL BIBLIOTECARIO
    elif iniciar_sesion == c.bibliotecario:
        if iniciar_sesion == c.bibliotecario:
            print("1- Cargar libros.")
            print("2- Editar libro.")
            print("3- Alquilar libro.")
            numero = input("Ingresá un número : ")
            while numero != "1" and numero != "2" and numero != "3":
                print("1- Cargar libros.")
                print("2- Editar libro.")
                print("3- Cambiar Status.")
                numero = input("ERROR. Ingresá un número : ")

            # CARGAR LIBRO
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
                print("Estos son los libros que estan actualmente en la biblioteca: ")
                for libro in registrar_libros:
                    print("***************************************************************")
                    pu.imprimir_libro(libro)



            # Editar libro

            elif numero == "2":
                ISBN_editar = int(input("Ingrese el ISBN que quiere editar: "))
                libro = bu.obtener_libro(ISBN=ISBN_editar)
                while libro is None:
                    print(
                        "El ISBN es incorrecto o no se encuentra el libro registrado. Por favor pruebe otra vez: "
                    )
                    ISBN_editar = int(
                        input("Ingrese el ISBN del libro que quiere editar: ")
                    )
                    libro = bu.obtener_libro(
                        ISBN_editar
                    )

                print("Libro encontrado: ")

                pu.imprimir_libro(libro)

                numero = int(input("Ingresá un número para editar o -1 para salir: "))
                while 7 < numero or numero < -1:
                    print("El numero ingresado es incorrecto.")
                    numero = int(input("Ingresá un número para editar : "))
                if numero != -1:
                    nuevo_valor = input("Ingresá el nuevo valor:")
                    editar = bu.editar_libros(
                        ISBN=ISBN_editar, indice=numero, valor=nuevo_valor
                    )
                print("Libro editado con éxito: ")
                pu.imprimir_libro(editar)

            # alquilar libro

            else:
                titulo = input("Ingrese el nombre del libro que quiere alquilar: ")
                libros = bu.busqueda_libros("titulo", titulo)
                print(f"Estos son los libros que coinciden con tu busqueda: {libros}")
                continuar = int(
                    input(
                        "Presione 1 para continuar, 2 si desea realizar otra busqueda o -1 para salir: "
                    )
                )

                bandera = True

                while bandera:
                    while continuar == 2:
                        titulo = input("Ingrese el nombre del libro que quiere alquilar: ")
                        libros = bu.busqueda_libros("titulo", titulo)
                        print(f"Estos son los libros que coinciden con tu busqueda: {libros}")
                        continuar = int(
                            input("Presione 1 para continuar, 2 si desea realizar otra busqueda o -1 para salir: "))

                    if continuar == 1:
                        isbn = int(input("Ingrese el ISBN del libro que quiere alquilar: "))
                        cantidad_pedidos = int(input("Ingrese la cantidad de pedidos: "))
                        usuario = input("Ingrese el nombre de ususario que va a alquilarlos: ")
                        libro_alquilado = bu.alquilar_libro(isbn, cantidad_pedidos, usuario)
                        print(
                            f"El libro se alquilo con exito, quedan {libro_alquilado[1]} unidades disponibles."
                        )
                        bandera = False


main()
