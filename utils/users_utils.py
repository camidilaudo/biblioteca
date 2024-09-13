from data_store import users_data as ud
from data_store import books_data as bd


def registrar_usuario(tipo_usuario, nombre, contrasenia_usuario):
    """Verifica si el usuario que se ingresó ya existe
    :param tipo_usuario: Int, 1 si es bibliotecario y 2 si es cliente.
    :param nombre: Str, nombre que ingresa el usuario para registrar.
    :param contrasenia_usuario: Str, contraseña que ingresa el usuario.
    :return usuario_registrado: Bool, devuelve True si se registró correctamente el usuario o False en caso contrario.
    """
    usuario_registrado = True

    # Verifica si el nombre de usuario ya existe

    for nombre in ud.usuarios:
        if nombre == ud.usuarios[1]:
            usuario_registrado = False
    # Agrega el tipo de usuario, nombre y contraseña a la matriz con los usuarios
    else:
        ud.usuarios.append([tipo_usuario, nombre, contrasenia_usuario])
    return usuario_registrado


def login_usuario(usuario, contra):
    """Funcion para loguear el usuario. La corriente función busca poder disernir si la persona interesada busca
    ingresar
    al sistema como usuario o como administrador.
    :param a: Str, tipo de usuario. 1 es usuario y 2 es administrador.
    :return:Str, tipo_de_usuario.
    """
    matriz_usuarios = ud.usuarios
    por_defecto = 3
    for fila in range(len(matriz_usuarios)):
        if usuario == matriz_usuarios[fila][1]:
            if contra == matriz_usuarios[fila][2]:
                return matriz_usuarios[fila][0]

    return por_defecto


def agregar_libro_historial(nombre_usuario, isbn):
    """Agrega el ISBN de un libro al historial del cliente.
    :param nombre_usuario: Str, username del usuario que retiro el libro.
    :param isbn: Int, código ISBN del libro que retiro.
    :return historiales: Matrix, historial de todos los usuarios."""
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


def ver_propio_historial(usuario):
    """Funcion encargada de mostrar el historial de retiros del usuario.
    :param usuario: Str, nombre del usuario.
    :return historial_nombres: titulos del historial de retiros del usuario."""

    historial_general = ud.historiales
    todos_los_libros = bd.libros
    historial_nombres = []
    i = 0
    while usuario != historial_general[i][0]:
        i = i + 1

    for isbn in historial_general[i + 1]:
        for j in range(len(todos_los_libros)):
            if isbn == todos_los_libros[j][3]:
                historial_nombres.append(todos_los_libros)[j][1]

    return historial_nombres
