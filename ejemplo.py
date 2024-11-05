import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import constantes as c
import utils.system_utils as su


bandera = True

while bandera:
                titulo = input("Ingrese el nombre del libro que quiere alquilar o -1 para salir: ")
                if titulo != "-1":
                    libros = bu.busqueda_libros("titulo", valor=titulo)
                    if libros:
                        print("Estos son los libros que coinciden con tu búsqueda:")
                        pu.imprimir_res_busqueda(libros)

                        continuar = ''
                        while continuar not in ['1', '2', '-1']:
                            continuar = input(
                                "Presione 1 para continuar, 2 para realizar otra búsqueda o -1 para salir: ")
                            if continuar not in ['1', '2', '-1']:
                                print("Error. Ingrese un número correcto.")

                        if continuar == '1':
                            alquilando = True
                            while alquilando and bandera:
                                isbn = int(input("Ingrese el ISBN del libro que quiere alquilar: "))
                                cantidad_pedidos = int(input("Ingrese la cantidad de pedidos: "))
                                usuario = input("Ingrese el nombre de usuario que va a alquilarlos: ")

                                if us.validar_usuario(usuario):
                                    libro_alquilado = bu.alquilar_libro(isbn, cantidad_pedidos, usuario)

                                    if libro_alquilado[0]:
                                        print("***************************************************************")
                                        libro_actualizado = bu.obtener_libro(isbn)
                                        print(f"El libro se alquiló con éxito.")

                                        print(
                                            f"Quedan {libro_actualizado['ejemplares_disponibles']} unidades disponibles.")
                                        print(
                                            f"Debe devolverlo antes del: {su.fecha_devolucion().strftime('%Y-%m-%d %H:%M:%S')}")

                                    elif libro_alquilado[1] < cantidad_pedidos:
                                        print("Error. No quedan ejemplares disponibles actualmente.")
                                    else:
                                        print("Error. El ISBN es incorrecto.")
                                else:
                                    print("Error. El usuario no existe.")

                                continuar_alquiler = input("Presione 1 para continuar alquilando o -1 para salir: ")
                                alquilando = continuar_alquiler == '1'
                                bandera = continuar_alquiler != '-1'

                        elif continuar == '2':
                            titulo = input("Ingrese el nombre del libro que quiere alquilar o -1 para salir: ")
                            if titulo == '-1':
                                bandera = False

                    else:
                        print("No contamos con ese libro en la biblioteca")
                else:

                    print(f"Estos son los libros que coinciden con tu búsqueda: ")
                    pu.imprimir_res_busqueda(libros)
                    bandera = True
                
                bandera_alquilar_libro = True
                while bandera_alquilar_libro:
                    try:
                        continuar = int(input("Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "))
                        if continuar in [1, 2, -1]:
                            bandera_alquilar_libro= False
                        else:
                            print("ERROR. Ingrese un número correcto")
                    except ValueError:
                        print("ERROR. Ingrese un valor numérico.")

                while continuar != -1:
                    if continuar == 2:

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

                    elif continuar == 1:
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
                        if libro_alquilado[0]:
                            print(
                                f"El libro se alquilo con exito, quedan {libro_alquilado[1]} unidades disponibles."
                            )
                        else:
                            if libro_alquilado[0]:
                                print(
                                    f"No se pudo realizar el alquiler. Asegúrese de que el ISBN sea correcto."
                                )
                            else:
                                print(
                                    f"No se pudo realizar el alquiler. Puede que no haya suficientes ejemplares disponibles."
                                )
                    continuar = int(
                        input(
                            "Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "))