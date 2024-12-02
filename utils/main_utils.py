import pdb

import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import utils.system_utils as su
import sys


def menu_cliente(nombre_usuario):
    """Ejecución del menú del cliente."""
    numero = "0"
    while numero != "-1":
        su.limpiar_terminal()
        pu.imprimir_menu_cliente()
        numero = input("¡Selecciona una opción! 📚: ")

        print("---------------------------------------------------------------")

        # Validación de opción
        while numero not in ["1", "2", "3", "4", "-1"]:
            print("\033[31m⚠️ Error: Opción incorrecta. Elige una opción válida.\033[0m")
            pu.imprimir_menu_cliente()
            numero = input("Por favor, ingresa una opción correcta: ")

        if numero == "1":  # Buscar libro
            clave = input("¿Qué campo deseas buscar? (Título, autor, género, etc.): ")
            es_valido = su.validar_constantes(clave)
            while not es_valido:
                print("\033[31m❌ Ese campo no existe, intenta con otro.\033[0m")
                clave = input("Por favor, ingresa un campo válido para la búsqueda: ")
                es_valido = su.validar_constantes(clave)

            valor = input("¿Qué valor deseas buscar? 🧐 ")
            campo_a_buscar = su.ingreso_Valido(valor)
            libros_encontrados = bu.busqueda_libros(clave, campo_a_buscar)

            if not libros_encontrados:
                print(
                    "\033[31m❌ No encontramos ese libro en nuestra biblioteca.\033[0m"
                )
            else:
                pu.imprimir_res_busqueda(libros_encontrados)
            print("---------------------------------------------------------------")
            input("Para continuar, presiona ENTER... ")

        elif numero == "2":  # Ver info del libro
            pedir_isbn = input("Ingrese el ISBN del libro 📖: ")
            ISBN = su.validacion_enteros(pedir_isbn)
            libro = bu.obtener_libro(ISBN)
            if libro is not None:
                _, detalle_libro = libro
                pu.imprimir_libro(detalle_libro)
            else:
                print("\033[31m❌ No encontramos el libro. Intenta de nuevo.\033[0m")
            print("---------------------------------------------------------------")
            input("Para continuar, presiona ENTER... ")

        elif numero == "3":  # Recomendaciones
            genero_libro = input("¿Qué género te gustaría leer? 🎭: ")
            genero_valido = su.validar_constantes(genero_libro)
            while not genero_valido:
                print(
                    "\033[31m❌ El género ingresado es incorrecto. Intenta nuevamente.\033[0m"
                )
                genero_libro = input("Por favor, ingresa un género válido: ")
                genero_valido = su.validar_constantes(genero_libro)

            recomendacion_libro = bu.recomendaciones(genero_libro, nombre_usuario)
            if recomendacion_libro is None:
                print("¡Has leído todos los libros de este género! 📚 😲")
                print("¡Intenta con otro género! 🎨")
            else:
                print(f"Te recomendamos este libro: {recomendacion_libro}")
            print("---------------------------------------------------------------")
            input("Para continuar, presiona ENTER... ")

        elif numero == "4":  # Ver historial
            mi_historial = us.ver_propio_historial(nombre_usuario)
            if not mi_historial:
                print("\033[31m❌ No tienes historial todavía. ¡Empieza a leer!\033[0m")
            else:
                pu.imprimir_historial(mi_historial)
            print("---------------------------------------------------------------")
            input("Para continuar, presiona ENTER... ")
        else:
            print("¡Gracias por visitar nuestra biblioteca! 🎉")
            sys.exit()

        su.limpiar_terminal()


def menu_bibliotecario():
    """Ejecución del menú del bibliotecario."""
    numero = "0"
    while numero != "-1":
        su.limpiar_terminal()
        pu.imprimir_menu_bibliotecario()
        numero = input("Selecciona una opción 📚: ")
        print("---------------------------------------------------------------")

        # Validación de opción
        while numero not in ["1", "2", "3", "4", "5", "-1"]:
            print("\033[31m⚠️ Error: Opción incorrecta. Elige una opción válida.\033[0m")
            pu.imprimir_menu_bibliotecario()
            numero = input("Por favor, ingresa una opción válida: ")

        if numero == "1":  # Cargar libro
            pedir_titulo = input("¿Cuál es el título del libro? 📖: ")
            titulo = su.ingreso_Valido(pedir_titulo)
            pedir_autor = input("¿Quién es el autor? ✍️: ")
            autor = su.ingreso_Valido(pedir_autor)
            pedir_genero = input("¿Qué género es? 🧐: ")
            genero = su.ingreso_Valido(pedir_genero)
            pedir_ISBN = input("¿Cuál es el ISBN? 📚: ")
            isbn = su.validacion_cantidades(pedir_ISBN)
            pedir_editorial = input("¿Qué editorial lo publicó? 📘: ")
            editorial = su.ingreso_Valido(pedir_editorial)
            pedir_anio_publicacion = input("¿En qué año se publicó? 📅: ")
            anio_publicacion = su.validacion_anio(pedir_anio_publicacion)
            pedir_serie_libros = input("¿Pertenece a una serie? 📚: ")
            serie_libros = su.ingreso_Valido(pedir_serie_libros)
            pedir_nro_paginas = input("¿Cuántas páginas tiene? 📄: ")
            nro_paginas = su.validacion_cantidades(pedir_nro_paginas)
            pedir_cant_ejemplares = input("¿Cuántos ejemplares tenemos? 📚: ")
            cant_ejemplares = su.validacion_cantidades(pedir_cant_ejemplares)

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
            print("Estos son los libros actualmente en la biblioteca: ")

            for libro in registrar_libros:
                print("***************************************************************")
                pu.imprimir_libro(registrar_libros[libro])
            input("Para continuar, presiona ENTER... ")

        elif numero == "2":  # Editar libro
            validar = None
            while validar != -1:
                ISBN_editar = input("¿Qué ISBN deseas editar? 📖 o -1 para salir: ")
                validar = su.validacion_enteros(ISBN_editar)

                libro = bu.obtener_libro(isbn=validar)

                if libro is None and validar != -1:
                    print(
                        "\033[31m❌ No encontramos el libro. Intenta con otro ISBN.\033[0m"
                    )
                    continue

                if validar != -1:
                    print("Libro encontrado:")
                    _, detalle_libro = libro
                    pu.imprimir_libro(detalle_libro)

                    pedir_numero = input("¿Qué número deseas editar? o -1 para salir: ")

                    numero = su.validacion_enteros(pedir_numero)

                    if numero != -1:
                        pedir_nuevo_valor = input("¿Qué nuevo valor quieres ingresar? 🖋️: ")
                        nuevo_valor = su.ingreso_Valido(pedir_nuevo_valor)

                        libro_editado = bu.editar_libros(
                            isbn=ISBN_editar, indice=numero, valor=nuevo_valor
                        )

                        if libro_editado is not None:
                            print("Los nuevos valores del libro son: ")
                            pu.imprimir_libro(libro_editado)
                        else:
                            print("\033[31m❌ Hubo un problema al editar el libro.\033[0m")
                    else:
                        # Salir si el índice es -1
                        validar = -1

                    print("---------------------------------------------------------------")
                    input("Para continuar, presiona ENTER... ")

        elif numero == "3":  # Alquilar libro
            bandera = True
            while bandera:
                input_usuario = input(
                    "¿Qué libro deseas alquilar? 📚 o -1 para salir: "
                )
                titulo = su.ingreso_Valido(input_usuario)
                if titulo == "-1":
                    bandera = False

                else:
                    libros = bu.busqueda_libros("titulo", valor=titulo)
                    if libros:
                        print("Estos son los libros que coinciden con tu búsqueda: ")
                        pu.imprimir_res_busqueda(libros)

                        continuar_ejecucion = None
                        while continuar_ejecucion not in [1, 2, -1]:
                            continuar = input(
                                "Presiona 1 para continuar, 2 para otra búsqueda o -1 para salir: "
                            )
                            continuar_ejecucion = su.validacion_enteros(continuar)

                        if continuar_ejecucion == 1:
                            encontrar_isbn = None
                            while encontrar_isbn is None and bandera:
                                encontrar_isbn = input(
                                    "¿Qué ISBN deseas alquilar? 📚 o -1 para salir: "
                                )
                                entrada = su.validacion_enteros(encontrar_isbn)
                                if entrada == -1:
                                    bandera = False
                            if bandera:
                                buscar_isbn = bu.obtener_libro(entrada)
                                if buscar_isbn is None:
                                    print(
                                        "\033[31m❌ El ISBN es incorrecto o no existe.\033[0m"
                                    )
                                    continue
                                else:
                                    nro_pedidos = None
                                    while nro_pedidos is None and bandera:
                                        cantidad_pedidos = input(
                                            "¿Cuántos ejemplares deseas? 📦: "
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
                                                print(
                                                    "\033[31mError❌. El usuario no existe o es bibliotecario.\033[0m"
                                                )
                                                bandera = False
                                            if estado_usuario is True:
                                                print(
                                                    "\033[31mUsuario penalizado⚠️. No puede alquilar.\033[0m"
                                                )
                                                bandera = False

                                    if bandera:
                                        libro_alquilado = bu.alquilar_libro(
                                            entrada, nro_pedidos, usuario
                                        )
                                        if libro_alquilado[0]:
                                            _, libro_actualizado = bu.obtener_libro(
                                                entrada
                                            )
                                            print(
                                                "***************************************************************"
                                            )
                                            print("El libro se alquiló con éxito. 🎉")
                                            print(
                                                f"Quedan {libro_actualizado['ejemplares_disponibles']} unidades disponibles."
                                            )
                                            print(
                                                f"Debe devolverlo antes del: {su.fecha_devolucion().strftime('%Y-%m-%d %H:%M:%S')}"
                                            )
                                        elif libro_alquilado[1] < nro_pedidos:
                                            print(
                                                "\033[31m❌ No hay suficientes ejemplares disponibles.\033[0m"
                                            )

                        elif continuar_ejecucion == -1:
                            bandera = False
                    else:
                        print("\033[31m❌ Título incorrecto o no encontrado.\033[0m")

        elif numero == "4":  # Devolver libro
            isbn = 0
            while isbn != -1:
                pedir_isbn = input(
                    "Ingresa el ISBN del libro a devolver 📖 o -1 para salir: "
                )
                isbn = su.validacion_enteros(pedir_isbn)

                if isbn != -1:
                    usuario = input("¿Qué usuario devolverá el libro? 🧑‍🤝‍🧑: ")
                    devolver = bu.devolver_libro(isbn, usuario)

                    if devolver:
                        _, libro = bu.obtener_libro(isbn)
                        print(
                            f"El libro {libro['titulo']} fue devuelto por {usuario}! 🎉"
                        )
                    else:
                        print("\033[31m❌ Libro no encontrado para devolución.\033[0m")

                    try:
                        continuar = int(
                            input("Presiona 1 para continuar o -1 para salir: ")
                        )
                    except ValueError:
                        print("Por favor, ingresa 1 o 0. 🧐")
                        continuar = 1

                    if continuar == -1:
                        isbn = -1

        elif numero == "5":  # Borrar libro
            libro_borrado = input("¿Qué ISBN deseas borrar? 📚: ")
            isbn = su.validacion_cantidades(libro_borrado)
            borrar_libro = bu.borrar_libro(isbn)
            if borrar_libro:
                print("El libro se ha borrado con éxito. 📚")
            else:
                print("\033[31m❌ No encontramos el libro. Intenta de nuevo.\033[0m")

            input("Para continuar, presiona ENTER... ")
            su.limpiar_terminal()

        else:
            print("¡Gracias por tu visita! 🎉")
            sys.exit()


# Las funciones que contienen la interfaz de usuario fueron mejoradas.


def mostrar_logo():
    "Funcion que imprime el logo de la biblioteca."
    logo = [
        r" ____  _                           _     _                     _         _     _ _     _ _       _                 ",
        r"| __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  ___    __ _  | | __ _  | |__ (_) |__ | (_) ___ | |_ ___  ___ __ _ ",
        r"|  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \/ __|  / _` | | |/ _` | | '_ \| | '_ \| | |/ _ \| __/ _ \/ __/ _` |",
        r"| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) \__ \ | (_| | | | (_| | | |_) | | |_) | | | (_) | ||  __/ (_| (_| |",
        r"|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/|___/  \__,_| |_|\__,_| |_.__/|_|_.__/|_|_|\___/ \__\___|\___\__,_|",
    ]
    print("\n".join(logo))


def mostrar_menu_principal():
    "Funcion que imprime las opciones del menu principal."
    print("=== MENÚ PRINCIPAL ===")
    print("1- Iniciar sesión.")
    print("2- Registrarse.")


def mostrar_menu_registro():
    "Funcion que imprime las opciones del menu de registro."
    print("=== REGISTRO DE USUARIO ===")
    print("1- Bibliotecario.")
    print("2- Cliente.")


def iniciar_sesion():
    "Función que loguea al usuario."
    print("\n=== INICIO DE SESIÓN ===")
    nombre_usuario = input("Ingrese nombre de usuario:  ")
    contrasenia = input("Ingrese la contraseña del usuario: ")
    return us.login_usuario(nombre_usuario, contrasenia), nombre_usuario


def registro_usuario(tipo_usuario):
    "Funcion que registra al usuario."
    print("\n=== CREACIÓN DE CUENTA ===")
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    validar = us.validar_usuario(nombre_usuario)
    while validar:
        print("\033[31mError. El usuario ingresado ya existe en el sistema. Intente de nuevo\033[0m")
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        validar = us.validar_usuario(nombre_usuario)

    print(
        "La contraseña debe tener entre 8 y 15 caracteres, y al menos un número, una letra minúscula, una letra "
        "mayúscula y un símbolo")
    contrasenia = input("Ingrese la contraseña del usuario: ")
    cumple_requisito = us.validar_contrasenia(contrasenia)

    while not cumple_requisito:
        print("\033[31mTu contraseña es débil.\033[0m")
        print("La contraseña debe tener entre 8 y 15 caracteres, y al menos un número, una letra minúscula, "
              "una letra mayúscula y un símbolo.")
        contrasenia = input("Ingrese la contraseña del usuario: ")
        cumple_requisito = us.validar_contrasenia(contrasenia)

    verificar_contrasenia = input("Volvé a ingresar la contraseña para confirmar: ")
    while contrasenia != verificar_contrasenia:
        print("\033[31mError. Las contraseñas no coinciden.\033[0m")
        verificar_contrasenia = input("Vuelva a ingresa la contraseña: ")

    if us.registrar_usuario(tipo_usuario, nombre_usuario, contrasenia):
        su.limpiar_terminal()
        print("Usuario registrado correctamente !")
        return nombre_usuario
