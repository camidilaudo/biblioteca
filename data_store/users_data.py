# ADMIN tipo de usuario 1
# CLIENTE tipo de usuario 2

# DICCIONARIO USUARIOS
usuarios = [
    {"tipo_usuario": 2, "nombre": "dani", "contrasenia": "123"},
    {"tipo_usuario": 2, "nombre": "cami", "contrasenia": "123"},
    {"tipo_usuario": 1, "nombre": "meli", "contrasenia": "123"},
]

#DICCIONARIOS DE LIBROS PENALIZADOS: Nombre del usuario y ISBN

penalizados = [
    ["cami", [9780307474278]],
]

#DICCIONARIO DE LIBROS ALQUILADOS: ISBN, cantidad, Nombre de usuario

alquilados = {
    9780747532743: 1,
    9780007136834: 4,
    9780307474278: 2,
    9780553573404: 1
}


# MATRIZ DE HISTORIAL

# filas de la matriz = [nombre de usuario,[ISBN1, ISBN2]]
historiales = [
    ["cami", [(9780747532743, "2024-10-23 12:45:32"), (9780553573404, "2024-10-23 12:50:00")]],
    ["dani", [(9780007136834, "2024-10-23 13:05:12"), (9780307474278, "2024-10-23 13:10:45")]]
]
