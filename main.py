import utils.users_utils as us
import utils.book_utils as bu
import data_store.users_data as ud
import utils.print_utils as pu
import data_store.books_data as bd
import constantes as c


# PROGRAMA PRINCIPAL :
def main():
    print(
        r"____  _                           _     _                     _         _     _ _     _ _       _                 ")
    print(
        r"| __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  ___    __ _  | | __ _  | |__ (_) |__ | (_) ___ | |_ ___  ___ __ _ ")
    print(
        r"|  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \/ __|  / _` | | |/ _` | | '_ \| | '_ \| | |/ _ \| __/ _ \/ __/ _` |")
    print(
        r"| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) \__ \ | (_| | | | (_| | | |_) | | |_) | | | (_) | ||  __/ (_| (_| |")
    print(
        r"|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/|___/  \__,_| |_|\__,_| |_.__/|_|_.__/|_|_|\___/ \__\___|\___\__,_|")

    input("Para continuar presione ENTER: ")
    print("")

    pu.limpiar_terminal()
    print("Ingrese una opción: ")
    print("1- Iniciar sesión.")
    print("2- Registrarse.")

    # Ingresar al sistema como usuario pre - existente
    numero_inicio = int(input("Ingrese un número : "))
    while numero_inicio not in c.tipos_usuario:
        numero_inicio = int(input("ERROR. Ingrese un número correcto : "))
    if numero_inicio == 1:

        nombre_usuario = input("Ingrese nombre de usuario:  ")
        contrasenia = input("Ingrese la contraseña del usuario: ")

        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)
        pu.limpiar_terminal()
    # Ingresar al sistema creando un nuevo usuario
    else:
        print("1- Bibliotecario.")
        print("2- Cliente.")
        usuario = int(input("Ingrese un número para el tipo de usuario:  "))
        if usuario == c.bibliotecario:
            contrasenia_general = input("Ingrese el código de acceso: ")
            while contrasenia_general != c.contrasenia_general:
                contrasenia_general = input(
                    "ERROR. Ingresa el código de acceso correcto: "
                )
        registrar = False
        while registrar is False:
            nombre_usuario = input("Ingrese un nombre de usuario : ")
            contrasenia = input("Ingrese la contraseña del usuario: ")
            verificar_contrasenia = input("Volvé a ingresar la contraseña : ")
            while contrasenia != verificar_contrasenia:
                print("Error. Las contraseñas no coinciden")
                contrasenia = input("Ingrese la contraseña del usuario: ")
                verificar_contrasenia = input("Volvé a ingresar la contraseña : ")
            registrar = us.registrar_usuario(usuario, nombre_usuario, contrasenia)
            if registrar is False:
                print("El usuario ingresado ya existe. Volver a intentar: ")
        pu.limpiar_terminal()
        print("Usuario registrado correctamente !")
        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

    while iniciar_sesion not in c.tipos_usuario:
        print("Su usuario o contrasenia es incorrecta")
        nombre_usuario = input("Ingrese nombre de usuario:  ")
        contrasenia = input("Ingrese la contrasena del usuario: ")
        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

    # SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
    numero = 0
    while numero != "-1":
        print(f"¡Bienvenido {nombre_usuario}!")
        print("")
        print("Elegí una opción para continuar: ")
        if iniciar_sesion == c.cliente:
            print("1- Buscar libros.")
            print("2- Buscar información detallada de un libro.")
            print("3- Recomendaciones.")
            print("4- Ver mi historial")
            print("O presione -1 para finalizar.")
            numero = input("Ingresá un número : ")
            print("---------------------------------------------------------------")
            while (
                numero != "1"
                and numero != "2"
                and numero != "3"
                and numero != "4"
                and numero != "-1"
            ):
                print("ERROR. Opción incorrecta.")
                print("")
                print("Elegí una opción para continuar: ")
                print("1- Buscar libros.")
                print("2- Obtener un libro.")
                print("3- Recomendaciones.")
                print("4- Ver mi historial")
                print("O presione -1 para finalizar.")
                numero = input("Ingresá un número correcto : ")
                print("---------------------------------------------------------------")
            # Buscar libro
            if numero == "1":
                clave = str(
                    input("Ingrese el campo por el cual va a realizar la búsqueda: ")
                )
                valor = str(input("Ingrese el valor del campo: "))
                libros_encontrados = bu.busqueda_libros(clave, valor)
                print(f"Se encontraron {len(libros_encontrados)}")
                pu.imprimir_res_busqueda(libros_encontrados)
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")

            # Info especifica del libro

            elif numero == "2":
                ISBN = int(
                    input(
                        "Ingrese el ISBN del libro que quiere obtener informacion detallada: "
                    )
                )
                libro = bu.obtener_libro(ISBN)
                if libro is not None:
                    pu.imprimir_libro(libro)
                else:
                    print("No encontramos el libro, volve a intentar!")
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")

            # ver propio historial

            elif numero == "4":
                if numero_inicio == 2:
                    print("Todavia no tienes libros en tu historial")
                else:
                    mi_historial = us.ver_propio_historial(usuario=nombre_usuario)
                    pu.imprimir_historial(mi_historial)
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")

            # recomendaciones

            elif numero == "3":
                genero_libro = input("Ingrese un género: ")
                recomendacion_libro = bu.recomendaciones(genero_libro, nombre_usuario)
                if recomendacion_libro is None:
                    print("¡Te leiste todos los libros de esta categoria!")
                    print("Podes volver a probar con otro genero.")
                else:
                    print("Te recomendamos este libro: ")
                    print("")
                    pu.imprimir_libro(recomendacion_libro)
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")
            else:
                print("¡Muchas gracias por visitar nuestra biblioteca!")

            pu.limpiar_terminal()

        # SI EL USUARIO QUE INICIA SESIÓN ES EL BIBLIOTECARIO

        elif iniciar_sesion == c.bibliotecario:
            if iniciar_sesion == c.bibliotecario:
                print("1- Cargar libros.")
                print("2- Editar libro.")
                print("3- Alquilar libro.")
                print("4- Borrar libro.")
                print("O presione -1 para finalizar.")
                numero = input("Ingresá un número : ")
                print("---------------------------------------------------------------")
                while (
                    numero != "1"
                    and numero != "2"
                    and numero != "3"
                    and numero != "-1"
                    and numero != "4"
                ):
                    print("ERROR. Opción incorrecta.")
                    print("")
                    print("Elegí una opción para continuar: ")
                    print("1- Buscar libros.")
                    print("2- Obtener un libro.")
                    print("3- Recomendaciones.")
                    print("4- Ver mi historial")
                    print("O presione -1 para finalizar.")
                    numero = input("ERROR. Ingresá un número : ")

                # CARGAR LIBRO
                if numero == "1":
                    titulo = input("Ingrese el titulo : ")
                    autor = input("Ingrese el autor : ")
                    genero = input("Ingrese el genero : ")
                    ISBN = int(input("Ingrese el ISBN : "))
                    editorial = input("Ingrese el editorial : ")
                    anio_publicacion = int(input("Ingrese el anio publicacion : "))
                    serie_libros = input("Ingrese el serie_libros : ")
                    nro_paginas = int(input("Ingrese el nro_paginas : "))
                    cant_ejemplares = int(input("Ingrese el la cantidad de ejemplares : "))
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
                    print(
                        "Estos son los libros que estan actualmente en la biblioteca: "
                    )
                    for libro in registrar_libros:
                        print(
                            "***************************************************************"
                        )
                        pu.imprimir_libro(libro)
                    input("Para continuar presione ENTER: ")

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
                        libro = bu.obtener_libro(ISBN_editar)

                    print("Libro encontrado: ")

                    pu.imprimir_libro(libro)

                    numero = int(
                        input("Ingresá un número para editar o -1 para salir: ")
                    )
                    while 9 < numero or numero < -1:
                        print("El numero ingresado es incorrecto.")
                        numero = int(input("Ingresá un número para editar : "))
                    if numero != -1:
                        nuevo_valor = input("Ingresá el nuevo valor:")
                        libro_editado = bu.editar_libros(
                            ISBN=ISBN_editar, indice=numero, valor=nuevo_valor
                        )
                        if libro_editado is not None:
                            print("Libro editado con éxito: ")
                            pu.imprimir_libro(libro_editado)
                        else:
                            print("Libro no encontrado")
                    input("Para continuar presione ENTER: ")

                # alquilar libro

                elif numero == "3":
                    titulo = input("Ingrese el nombre del libro que quiere alquilar: ")
                    libros = bu.busqueda_libros("titulo", valor=titulo)
                    print(f"Estos son los libros que coinciden con tu búsqueda: ")
                    pu.imprimir_res_busqueda(libros)
                    continuar = int(
                        input(
                            "Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "
                        )
                    )

                    bandera = True

                    while bandera:
                        while continuar == 2:
                            titulo = input(
                                "Ingrese el nombre del libro que quiere alquilar: "
                            )
                            libros_encontrados = bu.busqueda_libros("titulo", titulo)
                            print(f"Se encontraron {len(libros_encontrados)}")
                            pu.imprimir_res_busqueda(libros_encontrados)
                            continuar = int(
                                input(
                                    "Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "
                                )
                            )

                        if continuar == 1:
                            isbn = int(
                                input("Ingrese el ISBN del libro que quiere alquilar: ")
                            )
                            cantidad_pedidos = int(
                                input("Ingrese la cantidad de pedidos: ")
                            )
                            usuario = input(
                                "Ingrese el nombre de usuario que va a alquilarlos: "
                            )
                            libro_alquilado = bu.alquilar_libro(
                                isbn, cantidad_pedidos, usuario
                            )
                            print(
                                f"El libro se alquilo con exito, quedan {libro_alquilado[1]} unidades disponibles."
                            )
                            bandera = False

                elif numero == "4":
                    libro_borrado = int(
                        input("Ingrese en ISBN del libro que desea borrar: ")
                    )
                    borrar_libro = bu.borrar_libro(libro_borrado)
                    if borrar_libro:
                        print("Su libro se ha borrado con exito.")
                    else:
                        print("Libro no encontrado, por favor volve a intentar!")

                    input("Para continuar presione ENTER: ")
                    pu.limpiar_terminal()
                else:
                    print("¡Muchas gracias por visitar nuestra biblioteca!")


main()
