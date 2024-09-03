# Funcion para logear el usuario. 

# Objetivo: La corriente función busca poder disernir si la persona interesada busca ingresar al sistema como usario o como administrador.
#Datos de entrada: Nombre / contraseña.

# Datos de salida: Bienvenida al usuario o al admi segun corresponda.

# Desarrollo:

#Primero el ingresante deberá elegir si quiere logearse como administrador o como usuario. Luego le pedirán ingresar 
#la contraseña correspondiente. 
# En caso de que eliga usuario, existe una lista con las contraseñas validas. Cuando veamos Diccionarios debemos agregar
# la posibilidad de ingresar un nombre y vincularlo con una contraseña.

# Asumo que hay 1 solo admi. Cuando veamos diccionario
#si la contraseña está mal se le devuelve un mensaje de error
#Por ahora el administrador tiene 1 sola contraseña y el usuario tambien


def login_usuario (a):
    tipo_de_usuario = ""
    contra_admi= 1234
    contra_usuario = [5678, 9101, 1112]
    if a == 1:
        usuario = int (input ("Ingrese su identificador"))
        for contra in contra_usuario:
            if usuario == contra: 
                tipo_de_usuario = "usuario"
                return tipo_de_usuario
            else:
                tipo_de_usuario = "mal"
    elif a == 2:
        seguridad = int (input ("Ingrese el codigo de seguirdad"))
        if seguridad == contra_admi:
            tipo_de_usuario = "admi"
        else:
            tipo_de_usuario = "mal"
    else:
        tipo_de_usuario = "mal"
    
    return tipo_de_usuario

# Codigo principal

print ("Bienvenid@ al sistema de gestión.")
quien_sos = int (input ("Marca 1 para ingresar como -usuario- o 2 para ingresar -adminsitrador-."))

comprobar = login_usuario (quien_sos)

if comprobar== "usuario":
    print ("Bienvenido Usuario, a explorar")
elif comprobar == "admi":
    print ("Bienvenido administrador, a trabajar")
else:
    print ("error")

#Podemos decidir si queremos que le vuelva a dar la opción de ingresar sus datos o no. 
