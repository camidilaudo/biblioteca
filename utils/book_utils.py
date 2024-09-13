from data_store import users_data as ud

from data_store import books_data as bd

from utils import users_utils as uu

import random


def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status.
    """
    libros = []
    clave_posicion = [
        ["autor", 0],
        ["titulo", 1],
        ["genero", 2],
        ["ISBN", 3],
        ["editorial", 4],
        ["año de publicacion", 5],
        ["serie", 6],
        ["nro de paginas", 7],
        ["ejemplares", 8],
    ]

    indice = [
        caracteristica[1]
        for caracteristica in clave_posicion
        if clave == caracteristica[0]
    ][0]

    for libro in bd.libros:
        if libro[indice] == valor:
            titulo = libro[1]
            disponibilidad = libro[9]
            isbn = libro[3]
            libros.append([titulo, disponibilidad, isbn])

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

    libros = sum(fila.count(ISBN) for fila in bd.libros)
    if libros > 0:
        for i, libro in enumerate(bd.libros):
            if libro[3] == ISBN:
                bd.libros[i][8] += cant_ejemplares
                bd.libros[i][10] += cant_ejemplares

    else:
        nuevo_libro = [
            autor,
            titulo,
            genero,
            ISBN,
            editorial,
            anio_publicacion,
            serie_libros,
            nro_paginas,
            cant_ejemplares,
            True,
            cant_ejemplares,
        ]
        bd.libros.append(nuevo_libro)

    return bd.libros


def obtener_libro(ISBN):
    """Obtener un libro y su detalle segun su id interno o ISBN.
    :param ISBN: Int, International Standard Book Number del libro.
    :return libro: List, informacion detallada del libro buscado.
    """
    libro_encontrado = None
    for libro in bd.libros:
        if libro[3] == ISBN:
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
    for libro in bd.libros:
        if libro[3] == ISBN:
            libro[indice] = valor
    return libro


def alquilar_libro(isbn, cant_pedidos, nombre_usuario):
    """Cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param isbn: Str, titulo del libro a pedir.
    :param cant_pedidos: Int, cantidad de libros que se piden.
    :param nombre_usuario: Str, nombre del usuario que realiza el pedido.
    :return: List, estado del libro y ejemplares disponibles."""

    libro = obtener_libro(ISBN=isbn)

    status_libro = libro[9]
    ejemplares_disponibles = libro[10]

    if status_libro is True and ejemplares_disponibles > cant_pedidos:
        libro[10] -= cant_pedidos
        uu.agregar_libro_historial(nombre_usuario, isbn)

    elif status_libro is True and ejemplares_disponibles == cant_pedidos:
        libro[10] = 0
        libro[9] = False

        uu.agregar_libro_historial(nombre_usuario, isbn)

    return [status_libro, ejemplares_disponibles]


def recomendaciones(genero, usuario):
    """Devuelve una recomendación segun el genero que pida el usuario. Chequea que no
    sea un libro que haya leido anteriormente.
    :param genero: Str, genero del cual el usuario quiere una recomendacion.
    :param usuario: Str, usuario que pide la recomendacion.
    :return libro: List, libro recomendado.
    """

    todos_los_libros = bd.libros
    historial = ud.historiales
    recomendaciones_por_genero = []

    for fila in range(len(todos_los_libros)):
        if genero == todos_los_libros[fila][2]:
            recomendaciones_por_genero.append(todos_los_libros[fila][3])

    # comparar la lista de recomendaciones_por_genero con el historial recorriendolo con un for.
    # si alguno de recomendaciones NO esta en el historial lo añado a una nueva lista
    # el random lo aplico sobre esa lista nueva creada

    aleatorio_libro = random.choice(recomendaciones_por_genero)

    for fila in range(len(historial)):
        if usuario == historial[fila][0]:
            while aleatorio_libro in historial[fila]:
                aleatorio_libro = random.choice(recomendaciones_por_genero)

                # que pasa si el usuario leyo todos los libros de ese genero de la biblioteca?

    for fila in range(len(todos_los_libros)):
        if aleatorio_libro == todos_los_libros[fila][3]:
            return todos_los_libros[fila]


def borrar_libro(ISBN):
    """Eliminar libro de la biblioteca.
    :param ISBN: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :return bd.libros: Matrix, biblioteca actualizada."""

    for i, libro in bd.libros:
        if ISBN == libro[3]:
            del bd.libros[i]

    return bd.libros
