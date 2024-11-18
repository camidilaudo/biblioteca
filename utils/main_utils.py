import pdb

import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import utils.system_utils as su


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
            es_valido = su.validar_constantes(clave)
            while es_valido is False:
                print("Ese campo no existe en nuestra biblioteca, prueba con otro")
                clave = str(
                    input("Ingrese el campo por el cual va a realizar la búsqueda: ")
                )
                es_valido = su.validar_constantes(clave)

            valor = str(input("Ingrese el valor del campo: "))
            libros_encontrados = bu.busqueda_libros(clave, valor)
            pdb.set_trace()
            if not libros_encontrados:
                print("No contamos con ese libro en nuestra biblioteca")
                print(f"Se encontraron {len(libros_encontrados)}")
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")
            else:
                pu.imprimir_res_busqueda(libros_encontrados)
                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")

        # Info especifica del libro
        elif numero == "2":
            pedir_isbn = input("Ingrese un ISBN: ")
            ISBN = su.validacion_enteros(pedir_isbn)
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
            genero_valido = su.validar_constantes(genero_libro)
            while genero_valido is False:
                print("El género ingresado es incorrecto, por favor volver a ingresar")
                genero_libro = input("Ingrese un género: ")
                genero_valido = su.validar_constantes(genero_libro)

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

        su.limpiar_terminal()


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
            pedir_titulo = input("Ingrese el titulo : ")
            titulo = su.ingreso_Valido(pedir_titulo)
            pedir_autor = input("Ingrese el autor : ")
            autor = su.ingreso_Valido(pedir_autor)
            pedir_genero = input("Ingrese el genero : ")
            genero = su.ingreso_Valido(pedir_genero)
            pedir_ISBN = input("Ingrese un ISBN : ")
            isbn = su.validacion_enteros(pedir_ISBN)
            pedir_editorial = input("Ingrese el editorial : ")
            editorial = su.ingreso_Valido(pedir_editorial)
            pedir_anio_publicacion = input("Ingrese el año publicacion : ")
            anio_publicacion = su.validacion_enteros(pedir_anio_publicacion)
            pedir_serie_libros = input("Ingrese el serie_libros : ")
            serie_libros = su.ingreso_Valido(pedir_serie_libros)
            pedir_nro_paginas = input("Ingrese el número de paginas: ")
            nro_paginas = su.validacion_enteros(pedir_nro_paginas)
            pedir_cant_ejemplares = input("Ingrese el la cantidad de ejemplares : ")
            cant_ejemplares = su.validacion_enteros(pedir_cant_ejemplares)
            registrar_libros = bu.cargar_libros(
                titulo,
                autor,
                genero,
                isbn,
                editorial,
                anio_publicacion,
                serie_libros,
                nro_paginas,
                cant_ejemplares,
            )
            print("Estos son los libros que estan actualmente en la biblioteca: ")
            for libro in registrar_libros:
                print("***************************************************************")
                pu.imprimir_libro(registrar_libros[libro])
            input("Para continuar presione ENTER: ")

        # Editar libro
        elif numero == "2":
            validar = None

            while validar != -1:
                ISBN_editar = input(
                    "Ingrese el ISBN que quiere editar o -1 para salir: "
                )
                validar = su.validacion_enteros(ISBN_editar)

                libro = bu.obtener_libro(isbn=validar)

                if libro is None:
                    print("No encontramos el libro. Intente con otro ISBN.")
                    continue

                print("Libro encontrado:")
                pu.imprimir_libro(libro)

                pedir_numero = int(
                    input("Ingrese un número para editar o -1 para salir: ")
                )
                numero = su.validacion_enteros(pedir_numero)

                if numero != -1:
                    pedir_nuevo_valor = input(
                        "Ingrese el nuevo valor para el campo seleccionado: "
                    )
                    nuevo_valor = su.ingreso_Valido(pedir_nuevo_valor)

                    libro_editado = bu.editar_libros(
                        isbn=ISBN_editar, indice=numero, valor=nuevo_valor
                    )

                    if libro_editado is not None:
                        print("Libro editado con éxito:")
                        pu.imprimir_libro(libro_editado)
                    else:
                        print("Ocurrió un problema al editar el libro.")
                else:
                    # Salir si el índice es -1
                    validar = -1

                print("---------------------------------------------------------------")
                input("Para continuar presione ENTER: ")

        # alquilar libro
        elif numero == "3":
            bandera = True
            while bandera:
                titulo = input(
                    "Ingrese el nombre del libro que quiere alquilar o -1 para salir: "
                )
                if titulo == "-1":
                    bandera = False

                else:
                    libros = bu.busqueda_libros("titulo", valor=titulo)
                    if libros:
                        print("Estos son los libros que coinciden con tu búsqueda:")
                        pu.imprimir_res_busqueda(libros)

                        continuar_ejecucion = None
                        while continuar_ejecucion not in [1, 2, -1]:
                            continuar = input(
                                "Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para "
                                "salir: "
                            )
                            continuar_ejecucion = su.validacion_enteros(continuar)

                        if continuar_ejecucion == 1:
                            encontrar_isbn = None
                            while encontrar_isbn is None and bandera:
                                encontrar_isbn = input(
                                    "Ingrese el ISBN del libro que quiere alquilar o -1 para salir: "
                                )
                                entrada = su.validacion_enteros(encontrar_isbn)
                                if entrada == -1:
                                    bandera = False
                            if bandera:
                                buscar_isbn = bu.obtener_libro(entrada)
                                if buscar_isbn is None:
                                    print(
                                        "Error: El ISBN es incorrecto o no existe en la biblioteca"
                                    )
                                    continue
                                else:
                                    nro_pedidos = None
                                    while nro_pedidos is None and bandera:
                                        cantidad_pedidos = input(
                                            "Ingrese la cantidad de pedidos o -1 para salir: "
                                        )
                                        nro_pedidos = su.validacion_enteros(
                                            cantidad_pedidos
                                        )
                                        if nro_pedidos == -1:
                                            bandera = False
                                        else:
                                            usuario = input(
                                                "Ingrese el nombre de usuario que va a alquilarlos: "
                                            )
                                            encontrar_usuario = us.validar_usuario(
                                                usuario
                                            )
                                            estado_usuario = us.usuario_penalizado(
                                                usuario
                                            )
                                            if not encontrar_usuario:
                                                print("Error. El usuario no existe.")
                                            if estado_usuario is True:
                                                print(
                                                    "Usuario penalizado. No puede alquilar."
                                                )
                                                bandera = False

                                if bandera:
                                    libro_alquilado = bu.alquilar_libro(
                                        entrada, nro_pedidos, usuario
                                    )
                                    if libro_alquilado[0]:
                                        _, libro_actualizado = bu.obtener_libro(entrada)
                                        print(
                                            "***************************************************************"
                                        )
                                        print("El libro se alquiló con éxito.")
                                        print(
                                            f"Quedan {libro_actualizado['ejemplares_disponibles']} unidades disponibles."
                                        )
                                        print(
                                            f"Debe devolverlo antes del: {su.fecha_devolucion().strftime('%Y-%m-%d %H:%M:%S')}"
                                        )
                                    elif libro_alquilado[1] < nro_pedidos:
                                        print(
                                            "Error. No quedan suficientes ejemplares disponibles."
                                        )

                        elif continuar_ejecucion == -1:
                            bandera = False

        # devolver libro
        elif numero == "4":
            isbn = 0
            while isbn != -1:

                pedir_isbn = input("Ingrese un ISBN correcto o -1 para salir: ")
                isbn = su.validacion_enteros(pedir_isbn)

                if isbn != -1:
                    usuario = input(
                        "Ingrese el nombre del usuario que va a devolver el libro: "
                    )
                    devolver = bu.devolver_libro(isbn, usuario)

                    if devolver:
                        libro = bu.obtener_libro(isbn)
                        print(f"El libro {libro['titulo']} fue devuelto por {usuario}!")
                    else:
                        print("ISBN no encontrado. Intente nuevamente.")

                    try:
                        continuar = int(
                            input("Ingrese 1 para continuar o 0 para salir: ")
                        )
                    except ValueError:
                        print("Por favor, ingrese 1 o 0.")
                        continuar = 1

                    if continuar == 0:
                        isbn = -1

        # borrar libro
        elif numero == "5":
            libro_borrado = int(input("Ingrese en ISBN del libro que desea borrar: "))
            borrar_libro = bu.borrar_libro(libro_borrado)
            if borrar_libro:
                print("Su libro se ha borrado con exito.")
            else:
                print("Libro no encontrado, por favor volve a intentar!")

            input("Para continuar presione ENTER: ")
            su.limpiar_terminal()

        else:
            print("¡Muchas gracias por visitar nuestra biblioteca!")


def mostrar_logo():
    logo = [
        r" ____  _                           _     _                     _         _     _ _     _ _       _                 ",
        r"| __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  ___    __ _  | | __ _  | |__ (_) |__ | (_) ___ | |_ ___  ___ __ _ ",
        r"|  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \/ __|  / _` | | |/ _` | | '_ \| | '_ \| | |/ _ \| __/ _ \/ __/ _` |",
        r"| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) \__ \ | (_| | | | (_| | | |_) | | |_) | | | (_) | ||  __/ (_| (_| |",
        r"|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/|___/  \__,_| |_|\__,_| |_.__/|_|_.__/|_|_|\___/ \__\___|\___\__,_|",
    ]
    print("\n".join(logo))


def mostrar_menu_principal():
    print("=== MENÚ PRINCIPAL ===")
    print("1- Iniciar sesión.")
    print("2- Registrarse.")


def mostrar_menu_registro():
    print("=== REGISTRO DE USUARIO ===")
    print("1- Bibliotecario.")
    print("2- Cliente.")
    return input("Ingrese una opción correcta o -1 para salir: ")


def iniciar_sesion():
    print("\n=== INICIO DE SESIÓN ===")
    nombre_usuario = input("Ingrese nombre de usuario:  ")
    contrasenia = input("Ingrese la contraseña del usuario: ")
    return us.login_usuario(nombre_usuario, contrasenia)


def registro_usuario(tipo_usuario):
    print("\n=== CREACIÓN DE CUENTA ===")
    nombre_usuario = input("Ingrese un nombre de usuario : ")
    contrasenia = input("Ingrese la contraseña del usuario: ")
    verificar_contrasenia = input("Volvé a ingresar la contraseña : ")
    cumple_requisito = us.validar_contrasenia(contrasenia)

    while contrasenia != verificar_contrasenia or not cumple_requisito:
        if contrasenia != verificar_contrasenia:
            print("Error. Las contraseñas no coinciden")
        else:
            print("Tu contraseña es débil.")
            print(
                "Debe tener entre 8 y 15 caracteres, y al menos un número, una letra minúscula, una letra mayúscula y un símbolo"
            )

        contrasenia = input("Ingrese la contraseña del usuario o -1 para salir: ")
        if su.volver_atras(contrasenia):
            return False

        verificar_contrasenia = input("Volvé a ingresar la contraseña : ")
        cumple_requisito = us.validar_contrasenia(contrasenia)

    if us.registrar_usuario(tipo_usuario, nombre_usuario, contrasenia):
        su.limpiar_terminal()
        print("Usuario registrado correctamente !")
        return nombre_usuario
    else:
        print("El usuario ingresado ya existe.")
        return None
