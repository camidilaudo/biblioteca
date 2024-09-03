def registrar_usuario (lista_usuarios, lista_contrasenas):
    usuario = input("Ingrese un nombre de usuario: ")
    # VERIFICA SI EL NOMBRE DE USUARIO YA EXISTE
    while usuario in lista_usuarios:
        print("Ese usuario ya existe")
        usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese la contrasena del usuario: ")
    verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    # VERIFICA QUE LAS CONTRASEÑAS COINCIDAN
    while contrasena == verificar_contrasena:
        print("Error. Las contraseñas no coinciden, intente de nuevo. ")
        contrasena = input("Ingrese la contrasena del usuario: ")
        verificar_contrasena = input("Volvé a ingresar la contrasena : ")
    print("Listo ", usuario, "!")
    # SE GUARDAN EN LISTAS EL USUARIO Y LA CONTRASEÑA
    usuario.append(lista_usuarios)
    contrasena.append(lista_contrasenas)


# Funcion para logear el usuario.

# Objetivo: La corriente función busca poder disernir si la persona interesada busca ingresar al sistema como usario o como administrador.
# Datos de entrada: Nombre / contraseña.

# Datos de salida: Bienvenida al usuario o al admi segun corresponda.

# Desarrollo:

# Primero el ingresante deberá elegir si quiere logearse como administrador o como usuario. Luego le pedirán ingresar
# la contraseña correspondiente.
# En caso de que eliga usuario, existe una lista con las contraseñas validas. Cuando veamos Diccionarios debemos agregar
# la posibilidad de ingresar un nombre y vincularlo con una contraseña.

# Asumo que hay 1 solo admi. Cuando veamos diccionario
# si la contraseña está mal se le devuelve un mensaje de error
# Por ahora el administrador tiene 1 sola contraseña y el usuario tambien


def login_usuario(a):
    tipo_de_usuario = ""
    contra_admi = 1234
    contra_usuario = [5678, 9101, 1112]
    if a == 1:
        usuario = int(input("Ingrese su identificador"))
        for contra in contra_usuario:
            if usuario == contra:
                tipo_de_usuario = "usuario"
                return tipo_de_usuario
            else:
                tipo_de_usuario = "mal"
    elif a == 2:
        seguridad = int(input("Ingrese el codigo de seguirdad"))
        if seguridad == contra_admi:
            tipo_de_usuario = "admi"
        else:
            tipo_de_usuario = "mal"
    else:
        tipo_de_usuario = "mal"

    return tipo_de_usuario


# Codigo principal

print("Bienvenid@ al sistema de gestión.")
quien_sos = int(input("Marca 1 para ingresar como -usuario- o 2 para ingresar -adminsitrador-."))

comprobar = login_usuario(quien_sos)

if comprobar == "usuario":
    print("Bienvenido Usuario, a explorar")
elif comprobar == "admi":
    print("Bienvenido administrador, a trabajar")
else:
    print("error")

# Podemos decidir si queremos que le vuelva a dar la opción de ingresar sus datos o no.
# Fundición para dar recomendaciones según categorias.

# Datos de entrada: Categoria buscada, y dentro de esa categoria el genero.

# Datos de salida: la recomendación segun corresponda.

# SUPUESTOS
# Existen 3 categorias: ficción, no ficcion, poemas.
# Dentro de no ficcion existen 3 divisiones: historia, politica, ciencia.
# Dentro de ficcion existen 4 divisiones: terror, romance, suspenso, fantasia
# Dentro de poesia existen 2 divisiones: nacional o traducciones

# Desarrollo
# Se le consultará al usuario de qué categoria desea una recomendacion. Depende de qué elija, se le ofreceran distintas
# opcciones para especificar más la categoria.
# Existen listas de recomendaciones segun cada categoria y cada genero. En base a lo que haya elegido el usuario se le
# mostrarán las opciones pertinentes.

def Recomendaciones(c, g):
    recom_historia = ["Historia de la humanidad, de H.G. Wells", "Historia universal,de Arnold J. Toynbee",
                      "Historia de la civilización,de Will Durant"]
    recom_politica = ["La democracia en América,de Alexis de Tocquevill",
                      "Los orígenes del totalitarismo, de Hannah Arendt", "El príncipe moderno, de Antonio Gramsci"]
    recom_ciencia = ["El origen de las especies, de Charles Darwin", "Una nueva mente, de Daniel H. Pink",
                     "El universo elegante, de Brian Greene"]
    recom_terror = ["El resplandor, de Stephen King", "Cuentos de terror, de Edgar Allan Poe",
                    "La llamada de Cthulhu y otros cuentos, de H.P. Lovecraft"]
    recom_romance = ["Orgullo y prejuicio, de Jane Austen", "Cumbres borrascosas, de Emily Brontë",
                     "Jane Eyre, de Charlotte Brontë"]
    recom_suspenso = ["Perdida, de Gillian Flynn", "La chica del tren, de Paula Hawkins",
                      "El silencio de los corderos, de Thomas Harris"]
    recom_fantasia = ["El señor de los anillos, de J.R.R. Tolkien", "El nombre del viento,de Patrick Rothfuss",
                      "La rueda del tiempo ,de Robert Jordan"]
    recom_nacional = ["El hacedor, de Jorge Luis Borges", "Poesía completa, de Alfonsina Storni",
                      "Los heraldos negros, de César Vallejo"]
    recom_latino = ["Veinte poemas de amor y una canción desesperada, de Pablo Neruda",
                    "Poemas en prosa, de Gabriela Mistral", "Muerte sin fin, de José Gorostiz"]

    if c == "A":
        if g == 1:
            recomendacion = recom_historia
        elif g == 2:
            recomendacion = recom_politica
        elif g == 3:
            recomendacion = recom_ciencia
        else:
            recomendacion = "categoria invalida"
    elif c == "B":
        if g == 4:
            recomendacion = recom_terror
        elif g == 5:
            recomendacion = recom_romance
        elif g == 6:
            recomendacion = recom_suspenso
        elif g == 7:
            recomendacion = recom_fantasia
        else:
            recomendacion = "categoria invalida"
    elif c == "C":
        if g == 8:
            recomendacion = recom_nacional
        elif g == 9:
            recomendacion = recom_latino
        else:
            recomendacion = "categoria invalida"
    else:
        recomendacion = "categoria invalida"

    return recomendacion


# Codigo principal

categoria = input("Ingrese A si desea una recomendación de Ficcion, B si es No ficcion y C si es poesia: ")

if categoria == "A":
    genero = int(input("Ingrese 1 para Historia, 2 para politica o 3 para ciencia. "))
elif categoria == "B":
    genero = int(input("Ingrese 4 para Terror, 5 para romance, 6 para suspenso, 7 para fantasia. "))
elif categoria == "C":
    genero = int(input("Ingrese 8 para nacional o 9 para Latinoamerica. "))
else:
    genero = 0

reco = Recomendaciones(categoria, genero)

print("Recomendaciones: ", reco)
