# ADMIN tipo de usuario 1
# CLIENTE tipo de usuario 2

# DICCIONARIO USUARIOS
usuarios = [
    {"tipo_usuario": 2, "nombre": "dani", "contrasenia": "123"},
    {"tipo_usuario": 2, "nombre": "cami", "contrasenia": "123"},
    {"tipo_usuario": 1, "nombre": "meli", "contrasenia": "123"},
]

# DICCIONARIOS DE LIBROS PENALIZADOS: Nombre del usuario y ISBN
# Historial de libros que ya excedieron el plazo de préstamo y aún no han vuelto a la biblioteca

penalizados = [
    ["cami", [9780307474278]],
]

# DICCIONARIO DE LIBROS ALQUILADOS: ISBN, cantidad, Nombre de usuario
# Historial de todos los libros que la biblioteca tiene alquilados junto a sus cantidades

alquilados = {9780747532743: 1, 9780007136834: 4, 9780307474278: 2, 9780553573404: 1}


# MATRIZ DE HISTORIAL

# filas de la matriz = [nombre de usuario,[(ISBN1, Falquiler, Fdevolución), ISBN2]]
# Historial con los libros que ha leido cada usuario
historiales = [
    [
        "cami",
        [
            (9780747532743, "2024-10-23 12:45:32", "2024-10-24 12:45:32"),
            (9780553573404, "2024-10-23 12:50:00", "2024-10-24 12:45:32"),
        ],
    ],
    [
        "dani",
        [
            (9780007136834, "2024-10-23 13:05:12", "2024-10-24 12:45:32"),
            (9780307474278, "2024-10-23 13:10:45", "2024-10-24 12:45:32"),
        ],
    ],
]
