# Declaracion de constantes utilizadas en el programa

# TIPOS DE USUARIO
bibliotecario = 1
cliente = 2
tipos_usuario = [cliente, bibliotecario]
contrasenia_general = "ADMIN123"

# TIPOS DE GENERO
generos = [
    "fantasia",
    "terror",
    "policial",
    "historia",
    "misterio",
    "realismo magico",
    "distopia",
    "ficcion",
]

valor_bd = [
    "autor",
    "titulo",
    "genero",
    "editorial",
    "anio publicacion",
    "serie",
    "nro_paginas",
    "cant_ejemplares",
    "disponibilidad",
    "ejemplares_disponibles",
]

# Diccionario de claves para la base de datos

claves_bd = {
    # [Autor, Título, Género, Editorial, Año de Publicación, Serie, Nro. Páginas, Cant. Ejemplares, Disponibilidad, Ejemplares Disponibles]
    0: "autor",
    1: "titulo",
    2: "genero",
    3: "editorial",
    4: "anio_publicacion",
    5: "serie",
    6: "nro_paginas",
    7: "cant_ejemplares",
    8: "disponibilidad",
    9: "ejemplares_disponibles",
}

#Función para validar constantes 

def validar_constantes (clave):

    validacion = True

    if (clave not in valor_bd) and (clave not in generos):
        validacion = False 
 
    return validacion