import utils.users_utils as us
import utils.main_utils as mu
import utils.system_utils as su
import constantes as c


# PROGRAMA PRINCIPAL :
def main():
    mu.mostrar_logo()
    us.despenalizar_usuarios()

    continuar = True
    while continuar:
        mu.mostrar_menu_principal()
        opcion_principal = input("Ingrese una opción: ")
        validar_num = su.validacion_enteros(opcion_principal)
        su.limpiar_terminal()

        if validar_num == 1:  # Iniciar sesión
            iniciar_sesion_usuario = mu.iniciar_sesion()
            sesion_valida = iniciar_sesion_usuario in c.tipos_usuario

            while not sesion_valida:
                print("Usuario o contraseña incorrecta.")
                iniciar_sesion_usuario = mu.iniciar_sesion()

                if su.volver_atras(iniciar_sesion_usuario):
                    sesion_valida = True
                    iniciar_sesion_usuario = None
                else:
                    sesion_valida = iniciar_sesion_usuario in c.tipos_usuario

            if iniciar_sesion_usuario == c.cliente:
                mu.menu_cliente(iniciar_sesion_usuario)
            elif iniciar_sesion_usuario == c.bibliotecario:
                mu.menu_bibliotecario()

        elif validar_num == 2:
            registro_valido = False
            while not registro_valido:
                mu.mostrar_menu_registro()
                opcion_registro = input("Ingrese una opción: ")
                tipo_usuario = su.validacion_enteros(opcion_registro)

                if su.volver_atras(opcion_registro):
                    registro_valido = True
                else:
                    if tipo_usuario == c.bibliotecario:
                        print("\n=== VERIFICACIÓN DE ACCESO ===")
                        contrasenia_general = input("Ingrese el código de acceso: ")
                        acceso_valido = contrasenia_general == c.contrasenia_general

                        while not acceso_valido:
                            contrasenia_general = input(
                                "Error: Ingrese el código correcto o -1 para salir: "
                            )
                            if su.volver_atras(contrasenia_general):
                                acceso_valido = True
                                tipo_usuario = None
                            else:
                                acceso_valido = (
                                    contrasenia_general == c.contrasenia_general
                                )

                        if acceso_valido and tipo_usuario is not None:
                            nombre_usuario = mu.registro_usuario(tipo_usuario)
                            registro_valido = nombre_usuario is not None
                            if registro_valido:
                                mu.menu_bibliotecario()

                    elif tipo_usuario == c.cliente:
                        nombre_usuario = mu.registro_usuario(tipo_usuario)
                        registro_valido = nombre_usuario is not None
                        if registro_valido:
                            mu.menu_cliente(nombre_usuario)

                    else:
                        print("Error. Número inválido.")
        else:
            print("Error. Número inválido.")


main()
