# Funciones para imprimir por pantalla


def imprimir_libro(libro):
    """Función encargada de imprimir los atributos de un libro."""
    print(f"0. Autor: {libro["autor"]}")
    print(f"1. Título: {libro["titulo"]}")
    print(f"2. Género: {libro["genero"]}")
    print(f"3. Editorial: {libro["editorial"]}")
    print(f"4. Año de Publicación: {libro["anio_publicacion"]}")
    print(f"5. Serie de Libros: {libro["serie"]}")
    print(f"6. Número de Páginas: {libro["nro_paginas"]}")
    print(f"7. Cantidad de Ejemplares: {libro["cant_ejemplares"]}")
    print(f"8. Disponibilidad:  {libro["disponibilidad"]}")
    print(f"9. Cantidad de libros disponibles: {libro["ejemplares_disponibles"]}")
