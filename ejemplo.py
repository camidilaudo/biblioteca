

import utils.users_utils as us
import utils.main_utils as mu
import data_store.users_data as ud
import data_store.books_data as bd
import utils.print_utils as pu
import utils.system_utils as su
import constantes as c


# PROGRAMA PRINCIPAL :
def main():


    # Ingresar al sistema como usuario pre - existente
    bandera = True
    while bandera:
        try:
            numero_inicio = int(input("Ingrese un número: "))
            if numero_inicio in [1, 2]:
                bandera = False
            else:
                print("ERROR. Ingrese un número correcto")
        except ValueError:
            print("ERROR. Ingrese un valor numérico.")

    if numero_inicio == 1:

        nombre_usuario = input("Ingrese nombre de usuario:  ")
        contrasenia = input("Ingrese la contraseña del usuario: ")

        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)
        su.limpiar_terminal()
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
            cumple_requisito = us.validar_contrasenia(contrasenia)
            while (contrasenia != verificar_contrasenia) or not cumple_requisito:
                if contrasenia != verificar_contrasenia:
                    print("Error. Las contraseñas no coinciden")
                else:
                    print("Tu contraseña es debil.")
                contrasenia = input("Ingrese la contraseña del usuario: ")

                verificar_contrasenia = input("Volvé a ingresar la contraseña : ")
                cumple_requisito = us.validar_contrasenia(contrasenia)
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

    if iniciar_sesion == c.cliente:
        mu.menu_cliente(nombre_usuario)
    # SI EL USUARIO QUE INICIA SESIÓN ES EL BIBLIOTECARIO
    elif iniciar_sesion == c.bibliotecario:
        mu.menu_bibliotecario()


main()