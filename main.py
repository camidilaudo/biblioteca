import utils.users_utils as us
import utils.main_utils as mu
import data_store.users_data as ud
import data_store.books_data as bd
import utils.print_utils as pu
import utils.system_utils as su
import constantes as c


# PROGRAMA PRINCIPAL :
def main():
    print(
        r" ____  _                           _     _                     _         _     _ _     _ _       _                 "
    )
    print(
        r"| __ )(_) ___ _ ____   _____ _ __ (_) __| | ___  ___    __ _  | | __ _  | |__ (_) |__ | (_) ___ | |_ ___  ___ __ _ "
    )
    print(
        r"|  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \/ __|  / _` | | |/ _` | | '_ \| | '_ \| | |/ _ \| __/ _ \/ __/ _` |"
    )
    print(
        r"| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) \__ \ | (_| | | | (_| | | |_) | | |_) | | | (_) | ||  __/ (_| (_| |"
    )
    print(
        r"|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/|___/  \__,_| |_|\__,_| |_.__/|_|_.__/|_|_|\___/ \__\___|\___\__,_|"
    )

    print("")

    while True:
        bandera = True
        print("=== MENÚ PRINCIPAL ===")
        print("1- Iniciar sesión.")
        print("2- Registrarse.")
        entrada = input("Ingrese una opción: ")
        print("---------------------------------------------------------------")
        validar_num = su.validacion_enteros(entrada)

        if validar_num not in [1, 2] and validar_num is not None and validar_num != -1:
            print("Error. Número inválido.")
            bandera = False

        if bandera:

            # Inicio de sesion
            if validar_num == 1:
                print("\n=== INICIO DE SESIÓN ===")
                nombre_usuario = input("Ingrese nombre de usuario:  ")
                contrasenia = input("Ingrese la contraseña del usuario: ")

                iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)
                su.limpiar_terminal()

            # Ingresar al sistema creando un nuevo usuario
            elif validar_num == 2:
                validar_usuario = None
                salir = False
                while validar_usuario not in [1, 2] and not salir:
                    su.limpiar_terminal()
                    print("=== REGISTRO DE USUARIO ===")
                    print("1- Bibliotecario.")
                    print("2- Cliente.")
                    usuario = input("Ingrese una opción correcta o -1 para salir: ")
                    print(
                        "---------------------------------------------------------------"
                    )
                    if su.volver_atras(usuario):
                        bandera = False
                        salir = True
                    validar_usuario = su.validacion_enteros(usuario)

                    if (
                        validar_usuario not in [1, 2]
                        and validar_usuario is not None
                        and validar_usuario != -1
                        and bandera
                    ):
                        print("Error. Número inválido.")
                        bandera = False

                if bandera:

                    if validar_usuario == c.bibliotecario:
                        print("\n=== VERIFICACIÓN DE ACCESO ===")
                        contrasenia_general = input("Ingrese el código de acceso: ")

                        salir = False
                        while (
                            contrasenia_general != c.contrasenia_general and not salir
                        ):
                            contrasenia_general = input(
                                "Error: Ingresa el código de acceso correcto o -1 para salir: "
                            )
                            if su.volver_atras(contrasenia_general):
                                salir = True
                                bandera = False

                    if bandera:
                        registrar = False
                        while registrar is False:
                            print("\n=== CREACIÓN DE CUENTA ===")
                            nombre_usuario = input("Ingrese un nombre de usuario : ")
                            contrasenia = input("Ingrese la contraseña del usuario: ")
                            verificar_contrasenia = input(
                                "Volvé a ingresar la contraseña : "
                            )

                            cumple_requisito = us.validar_contrasenia(contrasenia)
                            salir = False
                            while (
                                (
                                    (contrasenia != verificar_contrasenia)
                                    or not cumple_requisito
                                )
                                and not salir
                                and bandera
                            ):

                                if contrasenia != verificar_contrasenia:
                                    print("Error. Las contraseñas no coinciden")
                                else:
                                    print("Tu contraseña es debil.")
                                    print(
                                        "Tu contraseña debe contar con entre 8 y 15 caracteres y contener al menos un número, una letra minuscula, una letra mayuscula y un simbolo"
                                    )
                                contrasenia = input(
                                    "Ingrese la contraseña del usuario o -1 para salir: "
                                )
                                if su.volver_atras(contrasenia):
                                    bandera = False
                                    salir = True
                                    registrar = True

                                else:
                                    verificar_contrasenia = input(
                                        "Volvé a ingresar la contraseña : "
                                    )
                                    cumple_requisito = us.validar_contrasenia(
                                        contrasenia
                                    )

                            if bandera:
                                registrar = us.registrar_usuario(
                                    usuario, nombre_usuario, contrasenia
                                )
                                if registrar is False:
                                    print(
                                        "El usuario ingresado ya existe. Volver a intentar: "
                                    )
                    if bandera:
                        su.limpiar_terminal()
                        print("Usuario registrado correctamente !")
                        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

            else:
                bandera = False

            if bandera:
                while iniciar_sesion not in c.tipos_usuario and bandera:
                    print("Su usuario o contrasenia es incorrecta")
                    nombre_usuario = input(
                        "Ingrese nombre de usuario o -1 para salir: "
                    )
                    if su.volver_atras(nombre_usuario):
                        bandera = False
                        salir = True
                    else:
                        contrasenia = input("Ingrese la contrasena del usuario: ")
                        iniciar_sesion = us.login_usuario(nombre_usuario, contrasenia)

                # SI EL USUARIO QUE INICIA SEsIÓN ES EL CLIENTE
                if bandera:
                    if iniciar_sesion == c.cliente:
                        mu.menu_cliente(nombre_usuario)
                    # SI EL USUARIO QUE INICIA SESIÓN ES EL BIBLIOTECARIO
                    elif iniciar_sesion == c.bibliotecario:
                        mu.menu_bibliotecario()


main()
