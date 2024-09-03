import users_data as ud


# TODO: h los inputs deben ir solo en el main, separado de la logica de las funciones
def registrar_usuario():
    """Registrar usuario en el sistema."""
    lista_usuarios = ud.usuarios
    lista_contrasenas = ud.contrasenas
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


# TODO: hay que cambiar la variable 'a' a una mas descriptiva y los inputs deben ir solo en el main, separado de la
#  logica de las funciones
def login_usuario(a):
    """Funcion para loguear el usuario. La corriente función busca poder disernir si la persona interesada busca ingresar
    al sistema como usuario o como administrador.
    :param a: Str, tipo de usuario. 1 es usuario y 2 es administrador.
    :return:Str, tipo_de_usuario.
    """
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
