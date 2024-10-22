# Función para validar constantes

def validar_constantes(clave):
    """
    Verifica si las claves a reemplazar por el usuario existen
    :param clave: Str, dato a editar
    :return: Bool, True si el dato es valido (existe), False si el dato no existe.
    """
    validacion = True

    if (clave not in valor_bd) and (clave not in generos):
        validacion = False

    return validacion
