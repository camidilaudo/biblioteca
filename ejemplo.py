import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import constantes as c
import utils.system_utils as su

bandera = True

while bandera:
    titulo = input("Ingrese el nombre del libro que quiere alquilar o -1 para salir: ")

    if titulo == "-1":
        bandera = False
    else: 
        libros = bu.busqueda_libros("titulo", valor=titulo)
        if libros:  
            print("Estos son los libros que coinciden con tu búsqueda:")
            pu.imprimir_res_busqueda(libros)

            continuar = su.validacion_numerica()
            if continuar == 1:  
                alquilando = True
                while alquilando:
                    isbn = int(input("Ingrese el ISBN del libro que quiere alquilar: "))
                    cantidad_pedidos = int(input("Ingrese la cantidad de pedidos: "))
                    usuario = input("Ingrese el nombre de usuario que va a alquilarlos: ")

                    if not us.validar_usuario(usuario):
                        print("Error. El usuario no existe.")
                        continue  # Volver a pedir el usuario

                    libro_alquilado = bu.alquilar_libro(isbn, cantidad_pedidos, usuario)
                    if libro_alquilado[0]:
                        libro_actualizado = bu.obtener_libro(isbn)
                        print("***************************************************************")
                        print("El libro se alquiló con éxito.")
                        print(f"Quedan {libro_actualizado['ejemplares_disponibles']} unidades disponibles.")
                        print(f"Debe devolverlo antes del: {su.fecha_devolucion().strftime('%Y-%m-%d %H:%M:%S')}")
                        alquilando = False  
                    elif libro_alquilado[1] < cantidad_pedidos:
                        print("Error. No quedan suficientes ejemplares disponibles.")
                    else:
                        print("Error. El ISBN es incorrecto.")
                

                continuar_alquiler = input("Presione 1 para alquilar otro libro o -1 para salir: ")
                if continuar_alquiler != '1':
                    bandera = False  
            elif continuar == 2:
                continue  
        else:
            print("No contamos con ese libro en la biblioteca.")
