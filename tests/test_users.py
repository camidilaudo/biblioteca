import pdb
import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import datetime, timedelta
import utils.users_utils as uu  # Reemplaza con el nombre del módulo donde está este código


class TestUsersUtils(unittest.TestCase):

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_registrar_usuario(self, mock_file):
        # Mock de usuarios existentes
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"nombre": "Usuario1", "tipo_usuario": 2, "contrasenia": "Pass123!"}
        })

        # Registrar usuario nuevo
        result = uu.registrar_usuario(2, "UsuarioNuevo", "Pass123!")
        self.assertTrue(result)

        # Intentar registrar usuario existente
        result = uu.registrar_usuario(2, "Usuario1", "Pass123!")
        self.assertFalse(result)

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_login_usuario(self, mock_file):
        # Mock de usuarios existentes
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"nombre": "Usuario1", "tipo_usuario": 2, "contrasenia": "Pass123!"}
        })

        # Login exitoso
        result = uu.login_usuario("Usuario1", "Pass123!")
        self.assertEqual(result, 2)

        # Login fallido (usuario no existe)
        result = uu.login_usuario("Usuario2", "Pass123!")
        self.assertEqual(result, -1)

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_agregar_libro_historial(self, mock_file):
        # Mock de historial inicial
        mock_file.return_value.read.return_value = json.dumps({
            "Usuario1": [{"isbn": 12345, "fecha_prestamo": "2023-01-01 12:00:00", "fecha_devolucion": None}]
        })

        # Agregar libro a historial existente
        result = uu.agregar_libro_historial("Usuario1", 67890)
        self.assertEqual(len(result["Usuario1"]), 2)

        # Crear nuevo historial para un usuario
        result = uu.agregar_libro_historial("UsuarioNuevo", 12345)
        self.assertIn("UsuarioNuevo", result)

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.su.fecha_actual", return_value=datetime(2023, 1, 10))
    def test_agregar_penalizados(self, mock_fecha_actual, mock_file):
        # Mock de usuarios iniciales
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"nombre": "Usuario1", "esta_penalizado": False, "fecha_despenalizacion": None}
        })

        # Penalizar usuario
        result = uu.agregar_penalizados("Usuario1")
        self.assertTrue(result["1"]["esta_penalizado"])
        self.assertIsNotNone(result["1"]["fecha_despenalizacion"])

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.bu.editar_libros")
    @patch("utils.users_utils.bu.obtener_libro",
           return_value=(None, {"ejemplares_disponibles": 5, "ejemplares_alquilados": 2}))
    def test_agregar_alquilados(self, mock_obtener_libro, mock_editar_libros, mock_file):
        # Mock de historial inicial
        mock_file.return_value.read.return_value = "isbn,cant_pedidos\n12345,2\n"

        # Agregar ejemplares alquilados
        result = uu.agregar_alquilados(12345, 2)
        pdb.set_trace()
        # Validar el resultado
        self.assertIn("12345", result)
        self.assertEqual(result["12345"], 4)  # 2 originales + 2 agregados

        # Verificar actualizaciones en la biblioteca
        mock_editar_libros.assert_any_call(isbn=12345, indice=9, valor=3)  # Actualización de ejemplares disponibles
        mock_editar_libros.assert_any_call(isbn=12345, indice=10, valor=4)  # Actualización de ejemplares alquilados

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_ver_propio_historial(self, mock_file):
        # Mock de historial general y biblioteca
        mock_file.side_effect = [
            mock_open(read_data=json.dumps({
                "Usuario1": [{"isbn": 12345}]
            })).return_value,
            mock_open(read_data=json.dumps({
                "1": {"isbn": 12345, "titulo": "Libro1"}
            })).return_value
        ]

        # Obtener historial del usuario
        result = uu.ver_propio_historial("Usuario1")
        self.assertEqual(result, ["Libro1"])

    def test_validar_contrasenia(self):
        # Contraseña válida
        self.assertTrue(uu.validar_contrasenia("Pass@123"))
        # Contraseña inválida (sin símbolo)
        self.assertFalse(uu.validar_contrasenia("Pass123"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_validar_usuario(self, mock_file):
        # Mock de usuarios
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"nombre": "Usuario1", "tipo_usuario": 2}
        })

        # Usuario válido
        self.assertTrue(uu.validar_usuario("Usuario1"))

        # Usuario inválido
        self.assertFalse(uu.validar_usuario("Usuario2"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    def test_usuario_penalizado(self, mock_file):
        # Mock de usuarios
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"nombre": "Usuario1", "esta_penalizado": True}
        })

        # Usuario penalizado
        self.assertTrue(uu.usuario_penalizado("Usuario1"))

    @patch("utils.users_utils.open", new_callable=mock_open)
    @patch("utils.users_utils.datetime", wraps=datetime)
    def test_despenalizar_usuarios(self, mock_datetime, mock_file):
        # Mock de usuarios penalizados
        mock_file.return_value.read.return_value = json.dumps({
            "1": {
                "nombre": "Usuario1",
                "esta_penalizado": True,
                "fecha_despenalizacion": "2023-01-01 12:00:00"
            }
        })
        mock_datetime.now.return_value = datetime(2023, 1, 10)

        # Despenalizar usuarios
        uu.despenalizar_usuarios()
        mock_file().write.assert_called()

if __name__ == "__main__":
    unittest.main()
