# Función estatus del libro

# Datos de entrada: Nombre del libro

# Datos de salida: el estado (disponible, en espera, no disponible)

#Desarrollo
# En primer lugar el usuario deberá ingresar qué libro busca.
# Existen dos listas. La lista con los llibros en stock y la lista con todos los libros alquilados. Si el libro no está
# en ninguna lista, es porque el libro no se encuentra en el sistema (no disponible)
#La función compara el libro que se consulta con todos los libros presentes en ambas listas. Si lo encuentra en alguna 
#Devuelve el estado pertinente, si no lo encuentra en ninguna de las dos es porque no está en la biblioteca.

def estatus_libros (n):

    disponible = ["emma"]
    en_espera = ["orgullo y prejuicio"]
    final = ""

    if n in disponible:
        return "disponible"
    elif n in en_espera:
        return "en_espera"
  

#Codigo principal

libro = input ("Ingrese el libro de su consulta")
libro_buscado = estatus_libros (libro)

if libro_buscado == "disponible":
    print ("lo tenemos")
elif libro_buscado == "en_espera":
    print ("Ahora está reservado, pero vuelve")
else:
    print ("No contamos con ese libro en nuestra biblioteca")
