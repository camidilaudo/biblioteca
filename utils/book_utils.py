from data_store import books_data as bd
from utils import users_utils as uu


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


def editar_libros(ISBN):
    """Editar los metadatos de un libro.
    :param ISBN: Int, International Standard Book Number del libro.
    :return libro: List, lista con lops metadatos del libro si el libro existe o None si el libro no existe.
    """
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


# TODO: Meli -> Agregar logica en el main de si quiere llevar igual los libros pero en menor cantidad
def alquilar_libro(titulo, cant_pedidos, nombre_usuario):
    """Cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param titulo: Str, titulo del libro a pedir.
    :param cant_pedidos: Int, cantidad de libros que se piden.
    :param nombre_usuario: Str, nombre del usuario que realiza el pedido.
    :return: List, estado del libro y ejemplares disponibles."""
    isbn = busqueda_libros("titulo", titulo)[2]

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


# TODO: actualmente no tenemos "categoria" dentro de los libros, habria que agregarla o cambiar la logica de la funcion. Las recomendaciones no deberian estar harcodeadas si no que deberia traerlas de la matriz de libros segun el genero y la cant de disponibles
def Recomendaciones(genero):
    """Función para dar recomendaciones según categorias.
    :param c: str, categoria de la cual se quiere una recomendacion.
    :param g: str, genero dentro de la categoria.
    :return: list, lista de recomendaciones."""

    # buscar libros que matcheen con el genero -> lista
    # generar un random desde 0 hasta el largo de la lista
    # si el isbn del libro existe en el historial generar otro random.
    # devolves la recomendacion que matcheo con el random

    recom_historia = [
        "Historia de la humanidad, de H.G. Wells",
        "Historia universal,de Arnold J. Toynbee",
        "Historia de la civilización,de Will Durant",
    ]
    recom_politica = [
        "La democracia en América,de Alexis de Tocquevill",
        "Los orígenes del totalitarismo, de Hannah Arendt",
        "El príncipe moderno, de Antonio Gramsci",
    ]
    recom_ciencia = [
        "El origen de las especies, de Charles Darwin",
        "Una nueva mente, de Daniel H. Pink",
        "El universo elegante, de Brian Greene",
    ]
    recom_terror = [
        "El resplandor, de Stephen King",
        "Cuentos de terror, de Edgar Allan Poe",
        "La llamada de Cthulhu y otros cuentos, de H.P. Lovecraft",
    ]
    recom_romance = [
        "Orgullo y prejuicio, de Jane Austen",
        "Cumbres borrascosas, de Emily Brontë",
        "Jane Eyre, de Charlotte Brontë",
    ]
    recom_suspenso = [
        "Perdida, de Gillian Flynn",
        "La chica del tren, de Paula Hawkins",
        "El silencio de los corderos, de Thomas Harris",
    ]
    recom_fantasia = [
        "El señor de los anillos, de J.R.R. Tolkien",
        "El nombre del viento,de Patrick Rothfuss",
        "La rueda del tiempo ,de Robert Jordan",
    ]
    recom_nacional = [
        "El hacedor, de Jorge Luis Borges",
        "Poesía completa, de Alfonsina Storni",
        "Los heraldos negros, de César Vallejo",
    ]
    recom_latino = [
        "Veinte poemas de amor y una canción desesperada, de Pablo Neruda",
        "Poemas en prosa, de Gabriela Mistral",
        "Muerte sin fin, de José Gorostiz",
    ]

    if c == "A":
        if g == 1:
            recomendacion = recom_historia
        elif g == 2:
            recomendacion = recom_politica
        elif g == 3:
            recomendacion = recom_ciencia
        else:
            recomendacion = "categoria invalida"
    elif c == "B":
        if g == 4:
            recomendacion = recom_terror
        elif g == 5:
            recomendacion = recom_romance
        elif g == 6:
            recomendacion = recom_suspenso
        elif g == 7:
            recomendacion = recom_fantasia
        else:
            recomendacion = "categoria invalida"
    elif c == "C":
        if g == 8:
            recomendacion = recom_nacional
        elif g == 9:
            recomendacion = recom_latino
        else:
            recomendacion = "categoria invalida"
    else:
        recomendacion = "categoria invalida"

    return recomendacion
