from data_store import users_data as ud

from data_store import books_data as bd

from utils import users_utils as uu

import constantes as c

import random

import datetime  

stock = lambda ISBN: True if [libro for libro in bd.libros if libro["isbn"] == ISBN] else False

def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status.
    """

    libros = [libro for libro in bd.libros if str(libro[clave]).lower() == valor.lower()]

    return libros

def cargar_libros(
        titulo,
        autor,
        genero,
        ISBN,
        editorial,
        anio_publicacion,
        serie_libros,
        nro_paginas,
        cant_ejemplares,
):
    """Cargar libro en stock de biblioteca. Se pueden cargar varios ejemplares del mismo.
    :param titulo: Str, título del libro.
    :param autor: List, nombre del autor/es del libro.
    :param genero: List, género/s del libro.
    :param ISBN: Int, International Standard Book Number del libro.
    :param editorial: Str, editorial del libro.
    :param anio_publicacion: Int, año de publicacion del libro.
    :param serie_libros: Str opcional, si el libro pertenece a una serie, escribirla. Caso contrario escribir None.
    :param nro_paginas: Int, número de páginas del libro.
    :param cant_ejemplares: Int, cantidad de ejemplares del mismo libro que se está cargando.
    :return libros_cargados: List, lista de libros cargados a la biblioteca."""

    # chequear si el libro ya existe en la biblioteca
    libro_en_stock = stock(ISBN=ISBN)
    if libro_en_stock:
        libro = obtener_libro(ISBN)
        libro["cant_ejemplares"] += cant_ejemplares
        libro["ejemplares_disponibles"] += cant_ejemplares
    else:

        nuevo_libro = {
            "autor": autor,
            "titulo": titulo,
            "genero": genero,
            "isbn": ISBN,
            "editorial": editorial,
            "anio_publicacion": anio_publicacion,
            "serie": serie_libros,
            "nro_paginas": nro_paginas,
            "cant_ejemplares": cant_ejemplares,
            "disponibilidad": True,
            "ejemplares_disponibles": cant_ejemplares,
        }
        bd.libros.append(nuevo_libro)

    return bd.libros


def obtener_libro(ISBN):
    """Obtener un libro y su detalle segun su id interno o ISBN.
    :param ISBN: Int, International Standard Book Number del libro.
    :return libro: List, informacion detallada del libro buscado.
    """
    libro_encontrado = None
    for libro in bd.libros:
        if libro["isbn"] == ISBN:
            libro_encontrado = libro

    return libro_encontrado


def editar_libros(ISBN, indice, valor):
    """Editar los metadatos de un libro.
    :param ISBN: Int, International Standard Book Number del libro.
    :param indice: Int, indice del campo que se va a editar.
    :param valor: Str, nuevo valor del campo que se va a editar.
    :return libro: List, lista con lops metadatos del libro si el libro existe o None si el libro no existe.
    """
    # Busca el libro por ISBN

    claves_bd = c.claves_bd
    libro_editado = None

    for libro in bd.libros:
        if libro["isbn"] == ISBN:
            libro[claves_bd[indice]] = valor
            libro_editado = libro
    return libro_editado


def alquilar_libro(isbn, cant_pedidos, nombre_usuario):
    """Cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param isbn: Str, titulo del libro a pedir.
    :param cant_pedidos: Int, cantidad de libros que se piden.
    :param nombre_usuario: Str, nombre del usuario que realiza el pedido.
    :return: List, estado del libro y ejemplares disponibles."""

    libro = obtener_libro(ISBN=isbn) 
    status_libro = libro["disponibilidad"]
    ejemplares_disponibles = libro["ejemplares_disponibles"]

    if status_libro and ejemplares_disponibles > cant_pedidos:
        ejemplares_disponibles = libro["ejemplares_disponibles"] - cant_pedidos
        libro["ejemplares_disponibles"] -= cant_pedidos
        uu.agregar_libro_historial(nombre_usuario, isbn)

    elif status_libro is True and ejemplares_disponibles == cant_pedidos:
        libro["ejemplares_disponibles"] = 0
        libro["disponibilidad"] = False
        ejemplares_disponibles = 0
        status_libro = False
        uu.agregar_libro_historial(nombre_usuario, isbn)
    elif status_libro is True and ejemplares_disponibles > cant_pedidos:
        ejemplares_disponibles = -1
        status_libro = False

    return [status_libro, ejemplares_disponibles]


def recomendaciones(genero, usuario):
    """Devuelve una recomendación segun el genero que pida el usuario. Chequea que no
    sea un libro que haya leido anteriormente.
    :param genero: Str, genero del cual el usuario quiere una recomendacion.
    :param usuario: Str, usuario que pide la recomendacion.
    :return libro: List, libro recomendado.
    """

    recomendaciones_por_genero = []
    historial_preexistente = []
    aleatorio_libro = None

    for historial_usuario in ud.historiales:
        if usuario == historial_usuario[0]:
            historial_preexistente = historial_usuario[1]

    for libro in bd.libros:
        if (libro["genero"].lower() == genero) and (
                libro["isbn"] not in historial_preexistente
        ):
            recomendaciones_por_genero.append(libro)

    # comparar la lista de recomendaciones_por_genero con el historial recorriendolo con un for.
    # si alguno de recomendaciones NO esta en el historial lo añado a una nueva lista
    # el random lo aplico sobre esa lista nueva creada

    if len(recomendaciones_por_genero) > 0:
        aleatorio_libro = random.choice(recomendaciones_por_genero)

    return aleatorio_libro


def borrar_libro(ISBN):
    """Eliminar libro de la biblioteca.
    :param ISBN: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :return bd.libros: Matrix, biblioteca actualizada."""
    bandera = False
    for i, libro in enumerate(bd.libros):
        if ISBN == libro["isbn"]:
            del bd.libros[i]
            bandera = True

    return bandera


def penalizaciones (fsalida , fregreso):

    dias_totales = fregreso - fsalida
    dias_maximos =  7

    if dias_totales <= dias_maximos:
        return True
    else:
        return False
