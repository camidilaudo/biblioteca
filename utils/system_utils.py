import os
from datetime import datetime, timedelta
import constantes as c


# Función para validar constantes


def limpiar_terminal():
    """Función encargada de limpiar la terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


fecha_actual = lambda: datetime.now()

fecha_devolucion = lambda: datetime.now() + timedelta(days=7)


def validacion_numerica():
    """Verifica si el usuario le estan ingresando un numero 1 2 o -1
    :return True cuando el usuario ingresa un número
    """
    bandera = True
    while bandera:
        try:
            es_valido = int(
                input(
                    "Presione 1 para continuar, 2 si desea realizar otra búsqueda o -1 para salir: "
                )
            )
            if es_valido in [1, 2, -1]:
                bandera = False
            else:
                print("ERROR. Ingrese un número correcto")
        except ValueError:
            print("ERROR. Ingrese un valor numérico.")
    return es_valido


def validacion_enteros(valor):
    """Verifica si el usuario le estan ingresando un valor numerico
    :return número validado
    """
    bandera = True
    numero = None
    while bandera:
        try:
            numero = int(valor)
            bandera = False
        except ValueError:
            print("Error: Debes ingresar un número entero.")
            valor = input("ingresa un número: ")

    return numero


def validar_constantes(clave):
    """Verifica si el usuario le estan ingresando un valor valido dentro de la lista de contactos
    :returnTrue o False segun si se le ingreso una respuesta correcta o no
    """
    validar = False
    texto_normalizado = clave.lower()

    if (texto_normalizado in c.valor_bd) or (texto_normalizado in c.generos):
        validar = True

    return validar


def volver_atras(entrada):
    """Función para verificar si el usuario quiere regresar al menú principal"""
    bandera = False
    if entrada == "-1":
        bandera = True
    return bandera


def ingreso_Valido(ingreso):
    bandera = True
    while bandera:
        verificar = (
            ingreso.strip()
        )  # Elimina espacios en blanco al principio y al final
        if verificar:  # Esto evalúa si la cadena no está vacía
            bandera = False
        else:
            print("No puede ingresar un campo vacío")
            ingreso = input("Ingrese su respuesta: ")
    return verificar
