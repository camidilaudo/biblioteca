import utils.users_utils as us
import utils.main_utils as mu
import data_store.users_data as ud
import data_store.books_data as bd
import utils.print_utils as pu
import constantes as c

# PROGRAMA PRINCIPAL :
def main():
    print(
        r" ____  _                           _     _                     _         _     _ _     _ _       _                 ")
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
    while numero_inicio not in [1, 2]:
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
            mu.menu_cliente()
    # SI EL USUARIO QUE INICIA SESIÓN ES EL BIBLIOTECARIO
    elif iniciar_sesion == c.bibliotecario:
            mu.menu_bibliotecario()

main()
