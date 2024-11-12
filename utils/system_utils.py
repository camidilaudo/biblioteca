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

def validacion_nenteros(entrada):
    while True: 
        try:
            numero = int(entrada)  
            return numero  
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            entrada = input("Ingrese un número entero nuevamente o -1 para salir: ")  

def validar_constantes(clave):
    
    validar= False
    texto_normalizado = clave.lower()

    if (texto_normalizado in c.valor_bd) or (texto_normalizado in c.generos):
        validar=True
    
    return validar







