import os

# Funciones para imprimir por pantalla


def imprimir_libro(libro):
    """Función encargada de imprimir los atributos de un libro."""
    print("***************************************************************")
    print(f"0. Autor: {libro['autor']}")
    print(f"1. Título: {libro['titulo']}")
    print(f"2. Género: {libro['genero']}")
    print(f"3. Editorial: {libro['editorial']}")
    print(f"4. Año de Publicación: {libro['anio_publicacion']}")
    print(f"5. Serie de Libros: {libro['serie']}")
    print(f"6. Número de Páginas: {libro['nro_paginas']}")
    print(f"7. Cantidad de Ejemplares: {libro['cant_ejemplares']}")
    print(f"8. Disponibilidad:  {libro['disponibilidad']}")
    print(f"9. Cantidad de libros disponibles: {libro['ejemplares_disponibles']}")


def imprimir_res_busqueda(lista):
    """Funcion encargada de imprimir los resultados de una búsqueda de libros."""
    for libro in lista:
        print("***************************************************************")
        print(f"Título: {libro[0]}")
        print(f"Disponibilidad: {libro[1]}")
        print(f"ISBN: {libro[2]}")


def imprimir_historial(lista):
    """Función encargada de imprimir el historial de los usuarios."""
    print("Los libros que leiste hasta el momento son: ")
    for titulo in lista:
        print(f"Título: {titulo}")


def limpiar_terminal():
    """Función encargada de limpiar la terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
