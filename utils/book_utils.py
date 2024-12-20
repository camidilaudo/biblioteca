from datetime import datetime
from utils import users_utils as uu
from utils import system_utils as su
import constantes as c
import random
import json

stock_json = lambda isbn: (
    True
    if [
        libro
        for libro in dict(json.load(open("./data_store/books_data.json"))).values()
        if libro["isbn"] == isbn
    ]
    else False
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
    :return biblioteca: Dict, lista de libros cargados a la biblioteca."""

    # chequear si el libro ya existe en la biblioteca
    libro_en_stock = stock_json(isbn=isbn)

    with open("./data_store/books_data.json", "r", encoding="utf-8") as file:
        biblioteca = dict(json.load(file))

        if libro_en_stock is True:
            clave_libro, _ = obtener_libro(isbn=isbn)
            biblioteca[clave_libro]["cant_ejemplares"] += cant_ejemplares
            biblioteca[clave_libro]["ejemplares_disponibles"] += cant_ejemplares
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
                "ejemplares_alquilados": 0,
            }
            indice = len(biblioteca) + 1
            biblioteca.update({str(indice): nuevo_libro})

    with open("./data_store/books_data.json", "w", encoding="utf-8") as file:
        json.dump(biblioteca, file, indent=4)

    return biblioteca


def obtener_libro(isbn):
    """Obtener un libro y su detalle según su ISBN.
    :param isbn: Str. El número ISBN del libro que se desea obtener.
    :return: El libro correspondiente al ISBN si se encuentra, o None si no se encuentra o si ocurre un error.
    """
    try:
        # Abrir el archivo en modo lectura
        with open("./data_store/books_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for id_libro, detalles in data.items():
                if str(detalles["isbn"]) == str(isbn):
                    return id_libro, detalles

    except FileNotFoundError:
        print("\033[31mEl archivo 'books_data.json' no existe.\033[0m")
    except json.JSONDecodeError:
        print(
            "\033[31mError al leer el archivo JSON. Verifica el formato del archivo.\033[0m"
        )

    return None


def editar_libros(isbn, indice, valor):
    """Edita los metadatos de un libro según el campo y su nuevo valor.
    :param isbn: Str. El número ISBN del libro que se quiere editar.
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
        "anio_publicacion",
        "ejemplares_disponibles",
        "nro_paginas",
        "ejemplares_alquilados",
    ]:
        try:
            valor = su.validacion_cantidades(valor)
        except ValueError:
            print(
                f"El valor para {c.valor_bd[indice]} debe ser un número entero positivo."
            )
            return None

    if c.valor_bd[indice] in [
        "disponibilidad",
    ]:
        if valor in {"True", "False"}:
                valor = eval(valor)
        else:
            print(
                f"\033[31mEl valor para {c.valor_bd[indice]} debe ser True o False.\033[0m"
            )
            return None

    with open("./data_store/books_data.json", "r+", encoding="utf-8") as file:
        data = json.load(file)

        libro_editado = None

        for libro_id, libro in data.items():
            if libro["isbn"] == int(isbn):
                if (c.valor_bd[indice] == "disponibilidad") and (
                        (valor is True and libro["ejemplares_disponibles"] <= 0) or (
                        valor is False and libro["ejemplares_disponibles"] > 0)):
                    print(f"\033[31m ❌ No podes cambiar la disponibilidad a {valor} ya que tiene {libro["ejemplares_disponibles"]} ejemplares disponibles.\033[0m")

                else:
                    print(
                        f"✍️ Campo --{c.valor_bd[indice].upper()}-- antes de la edición: {libro[c.valor_bd[indice]]}"
                    )

                    libro[c.valor_bd[indice]] = valor
                    libro_editado = libro

        if libro_editado:
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()

            print(
                f"✍️ Campo --{c.valor_bd[indice].upper()}-- después de la edición: {libro_editado[c.valor_bd[indice]]}"
            )
            print("Libro editado con éxito.")

        return libro_editado


def alquilar_libro(isbn, cant_pedidos, nombre_usuario):
    """Altera 2 historiales
     1) El de libros alquilados. Se fija que esté en la lista. Si no lo encuentra agrega el ISBN y la cantidad.
      Si lo encuentra, solo modifica la cantidad,
     2) El de usuario. En caso de que no lo haya leido antes, lo agrega a su historial
     Luego cambia el estado de un libro segun la cantidad de pedidos que tiene.
    :param isbn: Str, titulo del libro a pedir.
    :param cant_pedidos: Int, cantidad de libros a alquilar.
    :param nombre_usuario: Str, nombre del usuario que los va a alquilar.
    :return: una lista con la disponibilidad del libros y las cantidades disponibles."""

    with open("./data_store/books_data.json", "r", encoding="utf-8") as file:
        biblioteca = dict(json.load(file))
        libro, _ = obtener_libro(isbn=isbn)
        if libro is None:
            ejemplares_disponibles = -1
            status_libro = False

        else:
            status_libro = biblioteca[libro]["disponibilidad"]
            ejemplares_disponibles = biblioteca[libro]["ejemplares_disponibles"]

            # modificar_alquilar_libro
            if status_libro and (ejemplares_disponibles >= cant_pedidos):
                uu.agregar_libro_historial(nombre_usuario, isbn, cant_pedidos)
                uu.agregar_alquilados(isbn, cant_pedidos)

            elif status_libro and ejemplares_disponibles < cant_pedidos:
                ejemplares_disponibles = ejemplares_disponibles
                status_libro = False

        return [status_libro, ejemplares_disponibles]


def devolver_libro(isbn, nombre):
    """Verifica si el libro fue alquilado anteriormente por el usuario.
    :param isbn: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :param nombre: Str, nombre del usuario que quiere devolver el libro
    :return: Bool, False si el ISBN no se encuentra en el historial de libros alquilados,
    True si se devuelve correctamente el libro.
    """
    with open(
            "./data_store/books_data.json", "r", encoding="utf-8"
    ) as file_biblio, open(
        "./data_store/withdrawn_books_per_user.json", "r", encoding="utf-8"
    ) as file_historiales:
        biblioteca = dict(json.load(file_biblio))
        historiales = dict(json.load(file_historiales))
        devolucion = False
        data_libro = obtener_libro(isbn)
        if data_libro is not None:
            book_id, _ = obtener_libro(isbn)
            if book_id:
                biblioteca[book_id]["disponibilidad"] = True
                biblioteca[book_id]["ejemplares_disponibles"] += 1
                biblioteca[book_id]["ejemplares_alquilados"] -= 1

                fecha_hoy = su.fecha_actual()
            for usuario in historiales:
                if usuario == nombre:
                    libros_devueltos = 0
                    for i in range(len(historiales[usuario])):
                        if (
                                historiales[usuario][i]["isbn"] == isbn
                                and historiales[usuario][i]["fecha_devolucion"] is None
                                and libros_devueltos < 1
                        ):
                            historiales[usuario][i]["fecha_devolucion"] = (
                                fecha_hoy.strftime("%Y-%m-%d %H:%M:%S")
                            )
                            penalizaciones = (
                                lambda fsalida, fregreso: (fsalida - fregreso).days > 7
                            )

                            fecha_devolucion = historiales[usuario][i]["fecha_devolucion"]
                            fecha_prestamo = historiales[usuario][i]["fecha_prestamo"]


                            fsalida = datetime.strptime(fecha_devolucion, "%Y-%m-%d %H:%M:%S")
                            fregreso = datetime.strptime(fecha_prestamo, "%Y-%m-%d %H:%M:%S")

                            # Usar la lambda
                            es_penalizado = penalizaciones(fsalida, fregreso)
                            if es_penalizado:
                                uu.agregar_penalizados(nombre)
                                print("⚠️ Libro devuelto fuera de tiempo. El usuario queda penalizado por 7 dias.")
                            devolucion = True
                            libros_devueltos += 1

            with open(
                    "./data_store/books_data.json", "w", encoding="utf-8"
            ) as file_biblio, open(
                "./data_store/withdrawn_books_per_user.json", "w", encoding="utf-8"
            ) as file_historiales:
                json.dump(biblioteca, file_biblio, indent=4)
                json.dump(historiales, file_historiales, indent=4)
        return devolucion


def recomendaciones(genero, usuario):
    """Devuelve una recomendación segun el genero que pida el usuario. Chequea que no
    sea un libro que haya leido anteriormente.
    :param genero: Str, genero del cual el usuario quiere una recomendacion.
    :param usuario: Str, usuario que pide la recomendacion.
    :return libro: List, libro recomendado.
    """

    with open("./data_store/books_data.json", "r", encoding="utf-8") as file_biblio:
        biblioteca = dict(json.load(file_biblio))

    with open(
            "./data_store/withdrawn_books_per_user.json", "r", encoding="utf-8"
    ) as file_historiales:
        historiales = dict(json.load(file_historiales))
    recomendaciones_por_genero = []
    historial_preexistente = []
    aleatorio_libro = None

    for historial_usuario in historiales:
        if usuario == historial_usuario:
            historial_preexistente = historiales[historial_usuario]

    isbn_leidos = []
    for libro in historial_preexistente:
        isbn_leidos.append(libro["isbn"])
    for id_libro in biblioteca:
        if (biblioteca[id_libro]["genero"].lower() == genero) and (
                biblioteca[id_libro]["isbn"] not in isbn_leidos
        ):
            recomendaciones_por_genero.append(biblioteca[id_libro]["titulo"])

    # comparar la lista de recomendaciones_por_genero con el historial recorriendolo con un for.
    # si alguno de recomendaciones NO esta en el historial lo añado a una nueva lista
    # el random lo aplico sobre esa lista nueva creada

    if len(recomendaciones_por_genero) > 0:
        aleatorio_libro = random.choice(recomendaciones_por_genero)

    return aleatorio_libro


def borrar_libro(isbn):
    """Eliminar libro de la biblioteca.
    :param isbn: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :return bandera: True o False para indicar que el libro fue borrado correctamente.
    """
    bandera = False
    with open("./data_store/books_data.json", "r", encoding="utf-8") as file_biblio:
        biblioteca = dict(json.load(file_biblio))

    for i, libro in enumerate(biblioteca):
        if isbn == biblioteca[libro]["isbn"]:
            del biblioteca[libro]
            bandera = True
            break
    with open("./data_store/books_data.json", "w", encoding="utf-8") as file_biblio:
        json.dump(biblioteca, file_biblio, indent=4)

    return bandera
