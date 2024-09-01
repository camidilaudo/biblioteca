# DECLARACIÓN DE VARIABLES :
Lista_Usuarios = []
Lista_Contrasenas = []

# PROGRAMA PRINCIPAL :
print("Bienvenido a la biblioteca...")
print("1- Iniciar Seción.")
print("2- Registrarse.")

numero = input("Ingrese un número : ")
while numero != "1" and numero != "2":
    print("1- Iniciar Seción.")
    print("2- Registrarse.")
    numero = input("Error. Ingrese un número correcto : ")
if numero == "1":
    # Iniciar_Seción = funcion_iniciar seción
else:
    registrar = registrar_usuario (Lista_Usuarios, Lista_Contrasenas)

# SI EL USUARIO QUE INICIA SECIÓN ES EL CLIENTE
if inicar_secion == cliente
    print("1- Buscar libros.")
    print("2- Obtener libro.")
    numero = input("Ingresá un número : ")
    while numero != "1" and numero != "2":
        print("1- Buscar libros.")
        print("2- Obtener libro.")
    if numero == "1":
        buscar_libros = busqueda_libros(Clave, Valor)
    else:
        alquilar_libro = obtener_libro(id_libro, ISBN)

# SI EL USUARIO QUE INICIA SECIÓN ES EL BIBLIOTECARIO
else:
    if iniciar_secion == bibliotecario:
        print("1- Cargar libros.")
        print("2- Editar libro.")
        print("3- Cambiar Status.")
        numero = input("Ingresá un número : ")
        while numero != "1" and numero != "2" and numero != "3":
            print("1- Cargar libros.")
            print("2- Editar libro.")
            print("3- Cambiar Status.")
            numero = input("ERROR. Ingresá un número : ")
        if numero == "1":
            registrar_libros = cargar_libros(titulo, autor, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas, cant_ejemplares)
        elif numero == "2":
            editar = editar_libros
        else: 
            cambiar_status = cambiar()
