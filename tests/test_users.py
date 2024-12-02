import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import datetime
from utils import users_utils as uu


class TestUsersUtils(unittest.TestCase):

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_registrar_usuario(self, mock_file):
        """
        Verifica que la función registrar_usuario, registre un nuevo usuario en el sistema y que el nombre no coincida con algun usuario existente en la biblioteca

        Precondiciones :
        - La función recibe un tipo_usuario, nombre y una contrasenia como parámetros

        Postcondiciones:
        - Si el nombre de usuario es nuevo, no existe en el archivo, y los parametros son correctos la función agrega el nuevo usuario al archivo y devuelve True
        - Si el nombre de usuario ya existe en el archivo o los parametros son incorrectos la función no agrega el usuario y devuelve False

        """

        # Mock de usuarios existentes
        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"nombre": "Usuario1", "tipo_usuario": 2, "contrasenia": "Pass123!"}}
        )

        # Registrar usuario nuevo
        result = uu.registrar_usuario(2, "UsuarioNuevo", "Pass123!")
        self.assertTrue(result)

        # Intentar registrar usuario existente
        result = uu.registrar_usuario(2, "Usuario1", "Pass123!")
        self.assertFalse(result)

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_login_usuario(self, mock_file):
        """
        Verifica que la función login_usuario, que verifica si un usuario existente puede iniciar sesión en el sistema con su nombre y contraseña.

        Precondiciones:
        - El archivo de usuarios debe contener datos con tipo_usuario, nombre y contrasenia válidos.
        - La función debe recibir un nombre de usuario y una contraseña como parámetros.

        Postcondiciones:
        - Si el nombre de usuario y la contraseña coinciden con los datos en el archivo, la función devuelve el tipo de usuario correspondiente al usuario
        - Si el nombre de usuario no existe en el archivo, la función devuelve `-1`, indicando un error de inicio de sesion.

        """

        # Mock de usuarios existentes
        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"nombre": "Usuario1", "tipo_usuario": 2, "contrasenia": "Pass123!"}}
        )

        # Login exitoso
        result = uu.login_usuario("Usuario1", "Pass123!")
        self.assertEqual(result, 2)

        # Login fallido (usuario no existe)
        result = uu.login_usuario("Usuario2", "Pass123!")
        self.assertEqual(result, -1)

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_agregar_libro_historial(self, mock_file):
        """
        Verifica que la función agregar_libro_historial, agregue el libro al historial de libros alquilados de un usuario

        Precondiciones:
        - El archivo de historial de alquilados debe el usuario que alquilo y el ISBN del libro
        - La función debe permitir agregar un nuevo libro a un usuario que ya tiene historial y también debe permitir crear un historial para un usuario nuevo o que no alquilo aun.

        Postcondiciones:
        - Si se agrega un libro a un usuario existente, la longitud de su lista se incrementa en 1.
        - Si se agrega un libro para un usuario nuevo, se debe crear una nueva listas con usuario y el ISBN.
        - La función devuelve el archivo actualizado con el historial de préstamos.

        """

        # Mock de historial inicial
        mock_file.return_value.read.return_value = json.dumps(
            {
                "Usuario1": [
                    {
                        "isbn": 12345,
                        "fecha_prestamo": "2023-01-01 12:00:00",
                        "fecha_devolucion": None,
                    }
                ]
            }
        )

        # Agregar libro a historial existente
        result = uu.agregar_libro_historial("Usuario1", 67890,1)
        self.assertEqual(len(result["Usuario1"]), 2)

        # Crear nuevo historial para un usuario
        result = uu.agregar_libro_historial("UsuarioNuevo", 12345,1)
        self.assertIn("UsuarioNuevo", result)

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.su.fecha_actual", return_value=datetime(2023, 1, 10))
    def test_agregar_penalizados(self, mock_fecha_actual, mock_file):
        """
        Verifica que la función agregar_penalizados, marque a un usuario como penalizado en el archivo de usuarios y actualice la fecha de despenalización.

        Precondiciones:
        - El usuario no debe estar penalizado, debe haber alquilado un libro y devuelto despues de la fecha estimada.

        Postcondiciones :
        - El usuario debe estar penalizado.
        - La fecha de despenalización se calcula como 7 días después de la fecha actual
        - La función devuelve el diccionario actualizado de usuarios.
        - El archivo de usuarios se actualiza con los cambios y se verifica que se haya llamado write

        """

        # Mock de usuarios iniciales
        mock_file.return_value.read.return_value = json.dumps(
            {
                "1": {
                    "tipo_usuario": 1,
                    "nombre": "Usuario1",
                    "contrasenia": "Yomeamo2!",
                    "esta_penalizado": False,
                    "fecha_despenalizacion": None,
                }
            }
        )

        # Simula la escritura en el archivo
        mock_file.return_value.write = MagicMock()

        # Penalizar usuario
        result = uu.agregar_penalizados("Usuario1")

        # Validar el resultado
        self.assertTrue(result["1"]["esta_penalizado"])
        self.assertEqual(
            result["1"]["fecha_despenalizacion"],
            "2023-01-17 00:00:00",  # 7 días después
        )

        # Verificar que el archivo fue escrito
        mock_file().write.assert_called()

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.bu.editar_libros")
    @patch(
        "utils.users_utils.bu.obtener_libro",
        return_value=(None, {"ejemplares_disponibles": 5, "ejemplares_alquilados": 2}),
    )
    def test_agregar_alquilados(
        self, mock_obtener_libro, mock_editar_libros, mock_file
    ):
        """
        Verifica que la función agregar_alquilados, actualice los ejemplares alquilados de un libro en el historial y en el JSON.

        Precondiciones:
        - El historial inicial debe estar disponible en formato CSV, con columnas del isbn y el número que el libro fue alquilado.
        - La función obtener_libro devuelve un libro válido con los ejemplares disponibles y los ejemplares alquilados.

        Postcondiciones:
        - Se incrementa las veces que se alquilo el libro en el historial.
        - Los ejemplares disponibles y alquilados del libro en la biblioteca se actualizan según la cantidad alquilada.
        - La función devuelve un diccionario actualizado con el nuevo estado del historial

        """

        # Mock de historial inicial como CSV
        mock_file.return_value.__iter__ = lambda self: iter(
            ["isbn,cant_pedidos\n", "12345,2\n"]
        )

        # Llamada a la función
        result = uu.agregar_alquilados(12345, 2)

        # Validar el resultado
        self.assertIn("12345", result)
        self.assertEqual(result["12345"], 4)  # 2 originales + 2 agregados

        # Verificar actualizaciones en la biblioteca
        mock_editar_libros.assert_any_call(
            isbn=12345, indice=9, valor=3
        )  # Actualización de ejemplares disponibles
        mock_editar_libros.assert_any_call(
            isbn=12345, indice=10, valor=4
        )  # Actualización de ejemplares alquilados

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_ver_propio_historial(self, mock_file):
        """
        Verifica que la función ver_propio_historial, permita a un usuario consultar su historial de libros alquilados.

        Precondiciones:
        - El archivo de historial debe tener información sobre los libros alquilados por los usuarios y  su isbn
        - El JSON debe contener los datos de los libros disponibles y los isbn.

        Postcondiciones:
        - La función devuelve una lista con los títulos de los libros que el usuario alquilo y devolvio.
        - Si el usuario no tiene historial, la función devuelve una lista vacía.

        """

        # Mock de historial general y biblioteca
        mock_file.side_effect = [
            mock_open(
                read_data=json.dumps({"Usuario1": [{"isbn": 12345}]})
            ).return_value,
            mock_open(
                read_data=json.dumps({"1": {"isbn": 12345, "titulo": "Libro1"}})
            ).return_value,
        ]

        # Obtener historial del usuario
        result = uu.ver_propio_historial("Usuario1")
        self.assertEqual(result, ["Libro1"])

    def test_validar_contrasenia(self):
        """
        Verifica que la función validar_contrasenia, verifique que una contraseña cumple con los requisitos.

        Precondiciones:
        - La contraseña debe contener una longitud mínima, al menos una letra mayúscula, un número y un símbolo especial.

        Postcondiciones:
        - La función devuelve True si la contraseña cumple con todos los requerimientos.
        - La función devuelve False si la contraseña no cumple con los requerimientos.

        """

        # Contraseña válida
        self.assertTrue(uu.validar_contrasenia("Pass@123"))
        # Contraseña inválida (sin símbolo)
        self.assertFalse(uu.validar_contrasenia("Pass123"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_validar_usuario(self, mock_file):
        """
        Verifica que la función validar_usuario, verifique si un usuario existe y cumple con los requerimientos.

        Precondiciones :
        - El JSON debe contener para cada usuario los campos nombre y tipo_usuario.
        - El nombre del usuario pasado como argumento debe ser un Str no vacio.

        Postcondiciones :
        - La función devuelve True si el usuario existe y cumple los requerimientos .
        - Devuelve False si el usuario no existe en el JSON o no cumple con los requerimeintos.

        """

        # Mock de usuarios
        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"nombre": "Usuario1", "tipo_usuario": 2}}
        )

        # Usuario válido
        self.assertTrue(uu.validar_usuario("Usuario1"))

        # Usuario inválido
        self.assertFalse(uu.validar_usuario("Usuario2"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_usuario_penalizado(self, mock_file):
        """
        Verifica que la función usuario_penalizado, compruebe si al devolver un libro un usuario pasa a penalizado si supero el tiempo disponible.

        Precondiciones:
        - El JSON debe contener para cada usuario el booleano esta_penalizado.
        - El nombre del usuario pasado como parametro debe coincidir con uno existente en el JSON.

        Postcondiciones:
        - Si el usuario está penalizado (esta_penalizado = True), la función devuelve True.
        - Si el usuario no está penalizado o no existe en el JSON, la función devuelve False.

        """

        # Mock de usuarios
        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"nombre": "Usuario1", "esta_penalizado": True}}
        )

        # Usuario penalizado
        self.assertTrue(uu.usuario_penalizado("Usuario1"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.datetime", wraps=datetime)
    def test_despenalizar_usuarios(self, mock_datetime, mock_file):
        """
        Valida que la  función despenalizar_usuarios, elimine la penalización de usuarios si ha pasado la fecha de despenalización registrada en el JSON.

        Precondiciones:
        - El JSON debe contener para cada usuario penalizados los campos esta_penalizado y fecha_despenalizacion.

        Postcondiciones:
        - Los usuarios cuya penalizacion termino, esta_penalizado pasa a False y fecha_despenalizacion debe ser eliminada
        - El JSON debe sobreescribirse con los cambios realizados.
        - La función usa la fecha actual y calcula la fecha para ser despenalizado.
        - Se debe usar write para guardar los cambios.

        """

        # Mock de usuarios penalizados
        mock_file.return_value.read.return_value = json.dumps(
            {
                "1": {
                    "nombre": "Usuario1",
                    "esta_penalizado": True,
                    "fecha_despenalizacion": "2023-01-01 12:00:00",
                }
            }
        )
        mock_datetime.now.return_value = datetime(2023, 1, 10)

        # Despenalizar usuarios
        uu.despenalizar_usuarios()
        mock_file().write.assert_called()


if __name__ == "__main__":
    unittest.main()
