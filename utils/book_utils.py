import pdb
from data_store import users_data as ud
from data_store import books_data as bd
from utils import users_utils as uu
from utils import system_utils as su
import utils.book_utils as bu
import constantes as c
import random
import json

stock_json = lambda isbn: (
    True
    if [libro for libro in json.load(open("libros.json")) if libro["isbn"] == isbn]
    else False
)

stock_bd = lambda isbn: (
    True if [libro for libro in bd.libros if libro["isbn"] == isbn] else False
)


def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status.
    """

    libros = []
    with open("./data_store/books_data.json", "r", encoding="utf-8") as file:
        biblioteca = dict(json.load(file))

        for libro in biblioteca:
            if clave in biblioteca[libro]:
                if str(biblioteca[libro][clave]).lower() == str(valor).lower():
                    libros.append(biblioteca[libro])

    return libros


def cargar_libros(
    titulo,
    autor,
    genero,
    isbn,
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
    :param isbn: Int, International Standard Book Number del libro.
    :param editorial: Str, editorial del libro.
    :param anio_publicacion: Int, año de publicacion del libro.
    :param serie_libros: Str opcional, si el libro pertenece a una serie, escribirla. Caso contrario escribir None.
    :param nro_paginas: Int, número de páginas del libro.
    :param cant_ejemplares: Int, cantidad de ejemplares del mismo libro que se está cargando.
    :return libros_cargados: List, lista de libros cargados a la biblioteca."""

    # chequear si el libro ya existe en la biblioteca
    libro_en_stock = stock_json(isbn=isbn)

    with open("./data_store/books_data.json", "r+", encoding="utf-8") as file:
        biblioteca = dict(json.load(file))
        if libro_en_stock:
            libro = obtener_libro(isbn)
            libro["cant_ejemplares"] += cant_ejemplares
            libro["ejemplares_disponibles"] += cant_ejemplares
        else:

            nuevo_libro = {
                "autor": autor,
                "titulo": titulo,
                "genero": genero,
                "isbn": isbn,
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
    """Obtener un libro y su detalle según su ISBN.
    :param ISBN: Str. El número ISBN del libro que se desea obtener.
    :return: El libro correspondiente al ISBN si se encuentra, o None si no se encuentra o si ocurre un error.
    """
    try:
        # Abrir el archivo en modo lectura
        with open("./data_store/books_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

                # Buscar el libro por ISBN
            for libro in data:
                    if data[libro]["isbn"] == ISBN:
                        return libro

    except FileNotFoundError:
        print("El archivo 'books_data.json' no existe.")
        return None

    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Verifica el formato del archivo.")
        return None


def editar_libros(ISBN, indice, valor):
    """Edita los metadatos de un libro según el campo y su nuevo valor.
    :param ISBN: Str. El número ISBN del libro que se quiere editar.
    :param indice: Int. El índice en la lista 'c.valor_bd' que indica qué campo se desea modificar.
    :param valor: Str. El nuevo valor que se asignará al campo especificado. Si el campo requiere un número,
                  se intentará convertir a entero.
    :return: El libro editado si se encuentra y se realiza la modificación, o None si no se encuentra o ocurre un error.
    """
    if indice < 0 or indice >= len(c.valor_bd):
        print("Índice fuera de rango.")
        return None

    if c.valor_bd[indice] in [
        "cant_ejemplares",
        "disponibilidad",
        "ejemplares_disponibles",
    ]:
        try:
            valor = int(valor)
        except ValueError:
            print(f"El valor para {c.valor_bd[indice]} debe ser un número entero.")
            return None

    with open("./data_store/books_data.json", "r+", encoding="utf-8") as file:
        data = json.load(file)

        libro_editado = None

        for libro_id, libro in data.items():
            if libro["isbn"] == int(ISBN):
                print(f"Libro antes de la edición: {libro[c.valor_bd[indice]]}")

                libro[c.valor_bd[indice]] = valor
                libro_editado = libro

        if libro_editado:
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()

            print(f"Libro después de la edición: {libro[c.valor_bd[indice]]}")
            print("Libro editado con éxito.")
        else:
            print("No se encontró el libro para editar.")

        return libro_editado


def alquilar_libro(isbn, cant_pedidos, nombre_usuario):
    """Altera 2 historales
     1) El de libros alquilados. Se fija que esté en la lista. Si no lo encuentra agrega el ISBN y la cantidad.
      Si lo encuentra, solo modifica la cantidad,
     2) El de usuario. En caso de que no lo haya leido antes, lo agrega a su historial
     Luego cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param isbn: Str, titulo del libro a pedir."""

    with open("./data_store/books_data.json", "r+", encoding="utf-8") as file:

        libro = obtener_libro(ISBN=isbn)

        status_libro = libro["disponibilidad"]
        ejemplares_disponibles = libro["ejemplares_disponibles"]

        if libro is None:
            ejemplares_disponibles = -1
            status_libro = False

        # modificar_alquilar_libro
        if (status_libro) and (ejemplares_disponibles > cant_pedidos):
            ejemplares_disponibles = libro["ejemplares_disponibles"] - cant_pedidos

            fecha_hoy = su.fecha_actual
            uu.agregar_libro_historial(nombre_usuario, isbn, fecha_hoy)
            uu.agregar_alquilados(isbn, cant_pedidos)
            if isbn in ud.alquilados:
                ud.alquilados[isbn] += cant_pedidos
            else:
                ud.alquilados[isbn] = cant_pedidos

        elif status_libro and ejemplares_disponibles == cant_pedidos:
            libro["ejemplares_disponibles"] = 0
            libro["disponibilidad"] = True

            fecha_hoy = su.fecha_actual
            uu.agregar_libro_historial(nombre_usuario, isbn, fecha_hoy)
            uu.agregar_alquilados(isbn, cant_pedidos)

        elif status_libro and ejemplares_disponibles < cant_pedidos:
            ejemplares_disponibles = ejemplares_disponibles
            status_libro = False

        return [status_libro, ejemplares_disponibles]


def devolver_libro(ISBN, nombre):
    """Verifica si el libro fue alquilado anteriormente por el usuario.
    :param ISBN: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :param nombre: Str, nombre del usuario que quiere devolver el libro
    :return: Bool, False si el ISBN no se encuentra en el historial de libros alquilados,
    True si se devuelve correctamente el libro.
    """
    with open("./data_store/books_data.json", "r+", encoding="utf-8") as file:
        devolucion = False

        if ISBN in ud.alquilados:
            copias = ud.alquilados[ISBN]

            libro = obtener_libro(ISBN)
            if libro:
                libro["disponibilidad"] = True
                libro["ejemplares_disponibles"] += 1

                copias -= 1
                if copias == 0:
                    del ud.alquilados[ISBN]
                else:
                    ud.alquilados[ISBN] = copias

                fecha_hoy = su.fecha_actual()

                for historial in ud.historiales:
                    if historial[0] == nombre:
                        historial[2].append((ISBN, fecha_hoy))
                        penalizaciones = (
                            lambda fsalida, fregreso: (historial[2] - historial[1]).days
                            <= 7
                        )
                        if not penalizaciones:
                            uu.agregar_penalizados(nombre, ISBN)
                devolucion = True

        return devolucion

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
