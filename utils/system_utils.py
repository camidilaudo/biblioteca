import os
from datetime import datetime, timedelta


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


def limpiar_terminal():
    """Función encargada de limpiar la terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


fecha_actual = lambda: datetime.now()

fecha_devolucion = lambda: datetime.now() + timedelta(days=7)

 
def validacion_numerica ():
    bandera= True
    while bandera:
        try:
            es_valido = int(input("Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "))
            if es_valido in [1, 2, -1]:
                bandera= False
            else:
                print("ERROR. Ingrese un número correcto")
        except ValueError:
            print("ERROR. Ingrese un valor numérico.")
    return es_valido

