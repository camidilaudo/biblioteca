from data_store import users_data as ud


def registrar_usuario(nombre_usuario, contrasenia_usuario, contrasenia_usuario2):
    lista_usuarios = ud.usuarios
    lista_contrasenas = ud.contrasenas
    usuario_registrado = True
    # Verifica si el nombre de usuario ya existe
    if nombre_usuario in usuarios:
        usuario_registrado = False
    # Verifica si las contraseñas son iguales
    elif contrasenia_usuario != lista_contrasenas:
        usuario_registrado = False
    else:
        nombre_usuario.append(lista_usuarios)
        contrasena.append(lista_contrasenas)
    return usuario_registrado


# TODO: hay que cambiar la variable 'a' a una mas descriptiva y los inputs deben ir solo en el main, separado de la
#  logica de las funciones
def login_usuario(a):
    """Funcion para loguear el usuario. La corriente función busca poder disernir si la persona interesada busca ingresar
    al sistema como usuario o como administrador.
    :param a: Str, tipo de usuario. 1 es usuario y 2 es administrador.
    :return:Str, tipo_de_usuario.
    """
    tipo_de_usuario = ""
    contra_admi = 1234
    contra_usuario = [5678, 9101, 1112]
    if a == 1:
        usuario = int(input("Ingrese su identificador"))
        for contra in contra_usuario:
            if usuario == contra:
                tipo_de_usuario = "usuario"
                return tipo_de_usuario
            else:
                tipo_de_usuario = "mal"
    elif a == 2:
        seguridad = int(input("Ingrese el codigo de seguirdad"))
        if seguridad == contra_admi:
            tipo_de_usuario = "admi"
        else:
            tipo_de_usuario = "mal"
    else:
        tipo_de_usuario = "mal"

    return tipo_de_usuario
