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
        opcion_principal = input("¡Hola! 🎉 Elige una opción: ")

        # Validación de opción
        validar_num = su.validacion_enteros(opcion_principal)
        su.limpiar_terminal()

        if validar_num == 1:  # Iniciar sesión
            iniciar_sesion_usuario, nombre_usuario = mu.iniciar_sesion()
            sesion_valida = iniciar_sesion_usuario in c.tipos_usuario

            while not sesion_valida:
                print("\033[31m⚠️ Error: Usuario o contraseña incorrecta. Intenta nuevamente.\033[0m")
                iniciar_sesion_usuario, nombre_usuario = mu.iniciar_sesion()

                if su.volver_atras(iniciar_sesion_usuario):
                    sesion_valida = True
                    iniciar_sesion_usuario = None
                else:
                    sesion_valida = iniciar_sesion_usuario in c.tipos_usuario

            if iniciar_sesion_usuario == c.cliente:
                mu.menu_cliente(nombre_usuario)
            elif iniciar_sesion_usuario == c.bibliotecario:
                mu.menu_bibliotecario()

        elif validar_num == 2:  # Registro de usuario
            registro_valido = False
            while not registro_valido:
                mu.mostrar_menu_registro()
                opcion_registro = input("¿Qué tipo de usuario eres🤔?:  ")

                if su.volver_atras(opcion_registro):
                    registro_valido = True
                else:
                    tipo_usuario = su.validacion_enteros(opcion_registro)
                    if tipo_usuario == c.bibliotecario:
                        print("\n=== VERIFICACIÓN DE ACCESO ===")
                        contrasenia_general = input("Código de acceso: 🔑 ")
                        acceso_valido = contrasenia_general == c.contrasenia_general

                        while not acceso_valido:
                            contrasenia_general = input("\033[31m❌ Código incorrecto, prueba de nuevo: \033[0m")
                            if su.volver_atras(contrasenia_general):
                                acceso_valido = True
                                tipo_usuario = None
                            else:
                                acceso_valido = contrasenia_general == c.contrasenia_general

                        if acceso_valido:
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
                        print("\033[31m❌ Error. Opción no válida.\033[0m")

        else:
            print("\033[31m❌ Error. Opción no válida.\033[0m")


# Ejecutar el programa principal
main()
