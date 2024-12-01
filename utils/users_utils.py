import json
import re
import csv
from datetime import timedelta, datetime
from utils import system_utils as su
from utils import book_utils as bu


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

    with open("./data_store/users_data.json", "w", encoding="utf-8") as file:
        for usuario in dic_usuarios:
            if nombre == dic_usuarios[usuario]["nombre"]:
                usuario_registrado = False
        # Agrega el tipo de usuario, nombre y contraseña a la matriz con los usuarios

        if usuario_registrado:
            nuevo_usuario = {
                "tipo_usuario": int(tipo_usuario),
                "nombre": nombre,
                "contrasenia": contrasenia_usuario,
                "esta_penalizado": False,
                "fecha_despenalizacion": None,
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


def agregar_libro_historial(nombre_usuario, isbn):
    """Agrega el ISBN de un libro al historial del cliente.
    :param nombre_usuario: Str, username del usuario que retiro el libro.
    :param isbn: Int, código ISBN del libro que retiro.
    :param Str, fecha en que se alquiló el libro.
    :return historiales: Matrix, historial de todos los usuarios."""
    existe_usuario = False

    with open(
        "./data_store/withdrawn_books_per_user.json", "r", encoding="utf-8"
    ) as file:
        dict_historial = dict(json.load(file))
    for usuario in dict_historial:
        if usuario == nombre_usuario:
            existe_usuario = True
    if existe_usuario is True:
        nuevo_libro = {
            "isbn": isbn,
            "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_devolucion": None,
        }
        dict_historial[nombre_usuario].append(nuevo_libro)
    else:
        nuevo_historial = {
            f"{nombre_usuario}": [
                {
                    "isbn": isbn,
                    "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "fecha_devolucion": None,
                }
            ]
        }

        dict_historial.update(nuevo_historial)
    with open(
        "./data_store/withdrawn_books_per_user.json", "w", encoding="utf-8"
    ) as file:
        json.dump(dict_historial, file, indent=4)

    return dict_historial


def agregar_penalizados(nombre_usuario):
    """Agrega el ISBN de un libro al historial del cliente penalizado.
    :param nombre_usuario: Str, username del usuario que retiro el libro.
    :param isbn: Int, código ISBN del libro que retiro.
    :param Str, fecha en que se alquiló el libro.
    :return historiales: Matrix, historial de todos los usuarios."""

    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dic_usuarios = dict(json.load(file))

    with open("./data_store/users_data.json", "w", encoding="utf-8") as file:
        for user in dic_usuarios:
            if dic_usuarios[user]["nombre"] == nombre_usuario:
                user_id = user
                dic_usuarios[user_id]["esta_penalizado"] = True
                dic_usuarios[user_id]["fecha_despenalizacion"] = (
                    su.fecha_actual() + timedelta(days=7)
                ).strftime("%Y-%m-%d %H:%M:%S")
        json.dump(dic_usuarios, file, indent=4)
    return dic_usuarios


def agregar_alquilados(isbn, cant_pedidos):
    """Agrega el ISBN de un libro a la lista de libros alquilados
    :param isbn: Int, código ISBN del libro que retiro.
    :param cant_pedidos: int, cuantos libros quiere alquilar.
    :return alquilados: diccionario, historial de todos los libros alquilados."""

    existe_libro = False

    # Actualizo el historial de alquilaos
    with open("./data_store/withdrawn_books.csv", "r", encoding="utf-8") as file:
        historial_alquilados = list(csv.reader(file))
        for i in range(len(historial_alquilados)):
            if historial_alquilados[i][0] == str(isbn):
                existe_libro = True
                indice = i
        if existe_libro:
            historial_cant_libro = int(historial_alquilados[indice][1])
            historial_cant_libro += cant_pedidos
            historial_alquilados[indice][1] = historial_cant_libro
        else:
            historial_alquilados.append([isbn, cant_pedidos])

    with open(
        "./data_store/withdrawn_books.csv", "w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerows(historial_alquilados)

        _, libro = bu.obtener_libro(isbn=isbn)
        # Actualizo la biblioteca
        ejemplares_disponibles = libro["ejemplares_disponibles"] - cant_pedidos
        ejemplares_alquilados = libro["ejemplares_alquilados"] + cant_pedidos
        bu.editar_libros(isbn=isbn, indice=9, valor=ejemplares_disponibles)
        bu.editar_libros(isbn=isbn, indice=10, valor=ejemplares_alquilados)
        if ejemplares_disponibles == 0:
            bu.editar_libros(isbn=isbn, indice=8, valor=False)
    # Creo el diccionario de libros alquilados y los devuelvo
    rows = historial_alquilados[1:]
    libros_alquilados = {row[0]: int(row[1]) for row in rows}

    return libros_alquilados


def ver_propio_historial(usuario):
    """Funcion encargada de mostrar el historial de retiros del usuario.
    :param usuario: Str, nombre del usuario.
    :return historial_nombres: titulos del historial de retiros del usuario."""
    with open(
        "./data_store/withdrawn_books_per_user.json", "r", encoding="utf-8"
    ) as file:
        historial_general = dict(json.load(file))
    with open("./data_store/books_data.json", "r", encoding="utf-8") as file_biblio:
        biblioteca = dict(json.load(file_biblio))
    historial_nombres = []
    i = 0
    claves = list(historial_general.keys())
    while (i < len(historial_general)) and usuario != claves[i]:
        i = i + 1

    if i < len(historial_general):
        for libro_leido in historial_general[usuario]:
            for libro in biblioteca:
                if libro_leido["isbn"] == biblioteca[libro]["isbn"]:
                    historial_nombres.append(biblioteca[libro]["titulo"])

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
    "Valida que el usuario este registrado."
    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dict_usuarios = dict(json.load(file))
    validar = False
    for usuario in dict_usuarios.values():
        if usuario["nombre"] == nombre_usuario and usuario["tipo_usuario"] == 2:
            validar = True
    return validar


def usuario_penalizado(nombre_usuario):
    "Verifica si el usuario esta penalizado."
    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dict_usuarios = dict(json.load(file))
        for usuario in dict_usuarios.values():
            if usuario["nombre"] == nombre_usuario:
                estado = usuario["esta_penalizado"]

    return estado


def despenalizar_usuarios():
    "Funcion que se ejecuta al comienzo del programa para cambiar el estado de los usuarios penalizados."
    with open("./data_store/users_data.json", "r", encoding="utf-8") as file:
        dict_usuarios = dict(json.load(file))
        for usuario in dict_usuarios:
            if dict_usuarios[usuario]["esta_penalizado"] is True:
                fecha_despenalizacion = datetime.strptime(
                    dict_usuarios[usuario]["fecha_despenalizacion"], "%Y-%m-%d %H:%M:%S"
                )
                fecha_hoy = datetime.now()
                if (fecha_despenalizacion - fecha_hoy).days < 0:
                    dict_usuarios[usuario]["esta_penalizado"] = False

    with open("./data_store/users_data.json", "w", encoding="utf-8") as file:
        json.dump(dict_usuarios, file, indent=4)
