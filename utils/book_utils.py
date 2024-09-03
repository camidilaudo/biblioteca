import books_data as bd


def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status. """
    libros = []
    clave_posicion = [["autor", 0], ["titulo", 1], ["genero", 2], ["ISBN", 3], ["editorial", 4],
                      ["año de publicacion", 5],
                      ["serie", 6], ["nro de paginas", 7], ["ejemplares", 8]]

    indice = [caracteristica[1] for caracteristica in clave_posicion if clave == caracteristica[0]][0]

    for libro in bd.libros:
        if libro[indice] == valor:
            titulo = libro[1]
            disponibilidad = libro[9]
            libros.append([titulo, disponibilidad])

    return libros


def cargar_libros(titulo, autor, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas, cant_ejemplares):
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
    :return libros_cargados: List, lista de libros cargados a la biblioteca. """

    # chequear si el libro ya existe en la biblioteca

    libros = sum(fila.count(ISBN) for fila in bd.libros)
    if libros > 0:
        for i, libro in enumerate(bd.libros):
            if libro[3] == ISBN:
                bd.libros[i][8] += cant_ejemplares
                bd.libros[i][10] += cant_ejemplares

    else:
        nuevo_libro = [autor, titulo, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas,
                       cant_ejemplares, True, cant_ejemplares]
        bd.libros.append(nuevo_libro)

    return bd.libros


def obtener_libro(ISBN):
    """ Obtener un libro y su detalle segun su id interno o ISBN.
        :param ISBN: Int, International Standard Book Number del libro.
        :return libro: List, informacion detallada del libro buscado.
        """
    libro_encontrado = None
    for libro in bd.libros:
        if libro[3] == ISBN:
            libro_encontrado = libro

    return libro_encontrado


def editar_libros(ISBN):
    """Editar los metadatos de un libro.
     :param ISBN: Int, International Standard Book Number del libro.
     :return libro: List, lista con lops metadatos del libro si el libro existe o None si el libro no existe."""
    # Busca el libro por ISBN 
    for libro in bd.libros:
        if libro[3] == ISBN:
            # Pregunta al usuario que va a editar
            print("Libro encontrado : ")
            print(f"1. Autor: {libro[0]}")
            print(f"2. Título: {libro[1]}")
            print(f"3. Género: {libro[2]}")
            print(f"4. Editorial: {libro[4]}")
            print(f"5. Año de Publicación: {libro[5]}")
            print(f"6. Serie de Libros: {libro[6]}")
            print(f"7. Número de Páginas: {libro[7]}")
            print(f"8. Cantidad de Ejemplares: {libro[8]}")
            numero = input("Ingresá un número para editar : ")
            if numero == "1":
                libro[0] = input("Ingrese el nuevo autor: ")
            elif numero == "2":
                libro[1] = input("Ingrese el nuevo título: ")
            elif numero == "3":
                libro[2] = input("Ingrese el nuevo género: ")
            elif numero == "4":
                libro[4] = input("Ingrese la nueva editorial: ")
            elif numero == "5":
                libro[5] = int(input("Ingrese el nuevo año de publicación: "))
            elif numero == "6":
                libro[6] = input("Ingrese la nueva serie : ")
            elif numero == "7":
                libro[7] = int(input("Ingrese el nuevo número de páginas: "))
            elif numero == "8":
                libro[8] = int(input("Ingrese la nueva cantidad de ejemplares: "))
            else:
                print("Número no reconocido. No se realizó ningún cambio.")
            return libro

    print("No se encontró un libro con ese ISBN.")
    return None

def cambiar_status_libro(titulo, cant_pedidos):
    """Cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param titulo: Str, titulo del libro a pedir.
    :param cant_pedidos: Int, cantidad de libros que se piden.
    :return: list, estado del libro y ejemplares disponibles."""
    libro = busqueda_libros("titulo", titulo)

    status_libro = libro[9]
    ejemplares_disponibles = libro[10]

    if status_libro is True and ejemplares_disponibles > cant_pedidos:
        libro[10] -= cant_pedidos
    elif status_libro is True and ejemplares_disponibles == cant_pedidos:
        libro[10] = 0
        libro[9] = False
    else:
        status_libro = "El libro no se encuentra disponible."

    return [status_libro, ejemplares_disponibles]


