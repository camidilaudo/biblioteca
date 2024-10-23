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

#DICCIONARIO DE LIBROS ALQUILADOS: Nombre y cantidad de libros  

alquilados = [
    [9780307474278, 1],
    [9780007136834, 1],
    [9780553293357, 4],
    [9780553573404, 3]
]

# MATRIZ DE HISTORIAL

# filas de la matriz = [nombre de usuario,[ISBN1, ISBN2]]
historiales = [
    ["cami", [9780747532743, 9780553573404]],
    ["dani", [9780007136834, 9780307474728]],
]
