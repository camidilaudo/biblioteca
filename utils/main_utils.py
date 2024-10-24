import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import constantes as c


def menu_cliente(nombre_usuario):
    numero = "0"
    while numero != "-1":
        pu.imprimir_menu_cliente()
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
            pu.imprimir_menu_cliente()
            numero = input("Ingresá un número correcto : ")
            print("---------------------------------------------------------------")
        # Buscar libro
        if numero == "1":

            clave = input("Ingrese el campo por el cual va a realizar la búsqueda: ")
            es_valido = c.validar_constantes(clave)
            while es_valido is False:
                print("Ese campo no existe en nuestra biblioteca, prueba con otro")
                clave = str(input("Ingrese el campo por el cual va a realizar la búsqueda: "))
                es_valido = c.validar_constantes(clave)

            valor = str(input("Ingrese el valor del campo: "))
            libros_encontrados = bu.busqueda_libros(clave, valor)
            if not libros_encontrados:
                print("No contamos con ese libro en nuestra biblioteca")
                print(f"Se encontraron {len(libros_encontrados)}")
            else:
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

        # Recomendaciones
        elif numero == "3":
            genero_libro = input("Ingrese un género: ")
            genero_valido = c.validar_constantes(genero_libro)
            while genero_valido is False:
                print("El género ingresado es incorrecto, por favor volver a ingresar")
                genero_libro = input("Ingrese un género: ")
                genero_valido = c.validar_constantes(genero_libro)

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

        # Ver propio historial
        elif numero == "4":
            mi_historial = us.ver_propio_historial(nombre_usuario)
            if not mi_historial:
                print("No tenes historial todavia!.")
            else:
                pu.imprimir_historial(mi_historial)
            print("---------------------------------------------------------------")
            input("Para continuar presione ENTER: ")
        else:
            print("¡Muchas gracias por visitar nuestra biblioteca!")

        pu.limpiar_terminal()


def menu_bibliotecario():
    numero = "0"
    while numero != "-1":
        pu.imprimir_menu_bibliotecario()
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
            pu.imprimir_menu_bibliotecario()
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
            while not libros:
                print("No contamos con ese libro en la biblioteca")
                titulo = input("Ingrese el nombre de otro libro o -1 para salir: ")
                libros = bu.busqueda_libros("titulo", valor=titulo)

            if libros:
                print(f"Estos son los libros que coinciden con tu búsqueda: ")
                pu.imprimir_res_busqueda(libros)
                continuar = int(input("Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "))

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
