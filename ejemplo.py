import utils.print_utils as pu
import utils.book_utils as bu
import utils.users_utils as us
import constantes as c
import utils.system_utils as su

def devolver_libro(ISBN, nombre):
    """Verifica si el libro fue alquilado anteriormente por el usuario.
    :param ISBN: Int, codigo ISBN del libro que se quiere eliminar de la biblioteca.
    :param nombre: Str, nombre del usuario que quiere devolver el libro
    :return: Bool, False si el ISBN no se encuentra en el historial de libros alquilados,
    True si se devuelve correctamente el libro.
    """
    with open('./data_store/books_data.json', 'r+', encoding='utf-8') as file:
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
                usuario_encontrado = False

                for historial in ud.historiales:
                    if historial[0] == nombre:
                        historial[1].append((ISBN, fecha_hoy))
                        usuario_encontrado = True

                if not usuario_encontrado:
                    ud.historiales.append([nombre, [(ISBN, fecha_hoy)]])

                devolucion = True

        return devolucion