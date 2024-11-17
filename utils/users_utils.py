import json
import pdb
import re
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
    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dic_usuarios = dict(json.load(file))

    with open('./data_store/books_data.json', 'w', encoding='utf-8') as file:
        for usuario in dic_usuarios:
            if nombre == dic_usuarios[usuario]["nombre"]:
                usuario_registrado = False
        # Agrega el tipo de usuario, nombre y contraseña a la matriz con los usuarios

        if usuario_registrado:
            nuevo_usuario = {
                "tipo_usuario": int(tipo_usuario),
                "nombre": nombre,
                "contrasenia": contrasenia_usuario,
            }
            indice = len(dic_usuarios) + 1
            dic_usuarios.update({str(indice): nuevo_usuario})
            json.dump(dic_usuarios, file, indent=4)
    return usuario_registrado


def login_usuario(nombre_usuario, contrasenia):
    """Funcion para loguear el usuario. La corriente función busca poder disernir si la persona interesada busca
    ingresar
    al sistema como usuario o como administrador.
    :param usuario: Str, nombre de usuario del cliente.
    :return:Str, contraseña del usuario.
    """
    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dic_usuarios = dict(json.load(file))
        tipo_usuario = -1
        for usuario in dic_usuarios:
            if nombre_usuario == dic_usuarios[usuario]["nombre"]:
                if contrasenia == dic_usuarios[usuario]["contrasenia"]:
                    tipo_usuario = dic_usuarios[usuario]["tipo_usuario"]
    return tipo_usuario


def agregar_libro_historial(nombre_usuario, isbn, fecha):
    """Agrega el ISBN de un libro al historial del cliente.
    :param nombre_usuario: Str, username del usuario que retiro el libro.
    :param isbn: Int, código ISBN del libro que retiro.
    :param Str, fecha en que se alquiló el libro.
    :return historiales: Matrix, historial de todos los usuarios."""
    existe_usuario = False
    indice_historial = -1

    for i, historial in enumerate(ud.historiales):
        if historial[0] == nombre_usuario:
            existe_usuario = True
            indice_historial = i

    if existe_usuario is True:
        ud.historiales[indice_historial][1].append((isbn, fecha))
    else:
        ud.historiales.append([nombre_usuario, [(isbn, fecha)]])
    return ud.historiales


def agregar_penalizados(nombre_usuario, isbn):
    """Agrega el ISBN de un libro al historial del cliente penalizado.
    :param nombre_usuario: Str, username del usuario que retiro el libro.
    :param isbn: Int, código ISBN del libro que retiro.
    :param Str, fecha en que se alquiló el libro.
    :return historiales: Matrix, historial de todos los usuarios."""
    existe_usuario = False
    indice_historial = -1
    va = ""

    for i, historial in enumerate(ud.penalizados):
        if historial[0] == nombre_usuario:
            existe_usuario = True
            indice_historial = i

    if existe_usuario is True:
        ud.penalizados[indice_historial][1].append((isbn))
    else:
        ud.penalizados.append([nombre_usuario, [(isbn)]])
    return ud.penalizados


def agregar_alquilados(isbn, cant_pedidos):
    """Agrega el ISBN de un libro a la lista de libros alquilados
    :param isbn: Int, código ISBN del libro que retiro.
    :param cant_pedidos, int,  cuantos libros quiere alquilar.
    :return alquilados: diccionario, historial de todos los libros alquilados."""

    libros_totales = bd.libros
    libros_alquilados = ud.alquilados
    existe_libro = False

    for existente in libros_totales:
        if existente["isbn"] == isbn:
            existe_libro = True
        else:
            return existe_libro

    if existe_libro:
        for libro in libros_alquilados:
            if libro == isbn:
                libros_alquilados[libro] = libros_alquilados[libro] + cant_pedidos
            else:
                libros_alquilados[isbn] = cant_pedidos
        return libros_alquilados


def ver_propio_historial(usuario):
    """Funcion encargada de mostrar el historial de retiros del usuario.
    :param usuario: Str, nombre del usuario.
    :return historial_nombres: titulos del historial de retiros del usuario."""
    historial_general = ud.historiales
    historial_nombres = []
    i = 0

    while (i < len(historial_general)) and usuario != historial_general[i][0]:
        i = i + 1

    if i < len(historial_general):
        for isbn in historial_general[i][1]:
            for libro in bd.libros:
                if isbn == libro["isbn"]:
                    historial_nombres.append(libro["titulo"])
        return historial_nombres


def validar_contrasenia(contrasenia):
    """Valida que la contraseña ingresada respete los siguientes requesitos:
    - Contener (al menos) un número.
    - Contener (al menos) una letra minúscula.
    - Contener (al menos) una letra mayuscula.
    - Contener (al menos) un símbolo.
    - Que el largo de la cadena sea entre 8 o 15 caracteres.
    :param contrasenia: str, contraseña creada por el usuario.
    :return match: bool, si la contraseña cumple con el patron o no."""
    patron = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.!]).{8,15}$"
    match = bool(re.match(patron, contrasenia))
    return match


def validar_usuario(nombre_usuario):
    validar = False
    for usuario in ud.usuarios:
        if usuario["nombre"] == nombre_usuario and usuario["tipo_usuario"] == 2:
            validar = True
    return validar
