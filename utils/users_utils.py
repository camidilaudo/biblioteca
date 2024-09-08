# noinspection PyUnresolvedReferences
from data_store import users_data as ud


# TODO: Agregar tipo_usuario a la logica
def registrar_usuario(tipo_usuario, nombre, contrasenia_usuario):
    """ Verifica si el usuario que se ingresó ya existe
    :param tipo_usuario: Int, 1 si es bibliotecario y 2 si es cliente
    :param nombre: Str, nombre que ingresa el usuario para registrar
    :param contrasenia_usuario: Str, contraseña que ingresa el usuario
    :return usuario_registrado: Bool, devuelve True si se registro correctamente el usuario """
    usuario_registrado = True

    # Verifica si el nombre de usuario ya existe
    if nombre in ud.usuarios:
        usuario_registrado = False
    # Agrega el tipo de usuario, nombre y contraseña a la matriz con los usuarios
    else:
        ud.usuarios.append([tipo_usuario, nombre, contrasenia_usuario])
    return usuario_registrado


# TODO: hay que cambiar la variable 'a' a una mas descriptiva y los inputs deben ir solo en el main, separado de la
#  logica de las funciones
def login_usuario(nombre_usuario, contrasenia_usuario):
    """Funcion para loguear el usuario. La corriente función busca poder disernir si la persona interesada busca
    ingresar
    al sistema como usuario o como administrador.
    :param a: Str, tipo de usuario. 1 es usuario y 2 es administrador.
    :return:Str, tipo_de_usuario.
    """
    # tipos de return: 1 admin, 2 cliente, 0 error en usuario o contraseña
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


def agregar_libro_historial(nombre_usuario, isbn):
    """"""
    existe_usuario = False
    for i, historial in ud.historiales:
        if historial[0] == nombre_usuario:
            existe_usuario = True
            indice_historial = i

    if existe_usuario is True:
        ud.historiales[indice_historial][1].append(isbn)
    else:
        ud.historiales.append([nombre_usuario, [isbn]])

    return ud.historiales
