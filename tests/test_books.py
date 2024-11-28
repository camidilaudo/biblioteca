import pdb
import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import datetime
import random
from utils import book_utils as bu  # Reemplaza con el nombre de tu módulo


class TestBookUtils(unittest.TestCase):

    @patch("utils.book_utils.open", new_callable=mock_open, read_data=json.dumps({}))
    def test_stock_json(self, mock_file):
        # Caso libro no encontrado
        isbn = 12345
        result = bu.stock_json(isbn)
        self.assertFalse(result)

        # Caso libro encontrado
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"isbn": 12345}
        })
        result = bu.stock_json(isbn)
        self.assertTrue(result)

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_busqueda_libros(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"titulo": "Libro1", "autor": "Autor1"}
        })
        result = bu.busqueda_libros("titulo", "Libro1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["titulo"], "Libro1")

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_cargar_libros(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps({})
        result = bu.cargar_libros(
            "Libro1", ["Autor1"], ["Genero1"], 12345, "Editorial1", 2023, None, 300, 5
        )
        self.assertIn("1", result)
        self.assertEqual(result["1"]["titulo"], "Libro1")

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_obtener_libro(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"isbn": 12345}
        })
        result = bu.obtener_libro(12345)
        self.assertIsNotNone(result)
        self.assertEqual(result[1]["isbn"], 12345)

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.su.validacion_cantidades", return_value=10)
    def test_editar_libros(self, mock_validacion, mock_file):
        mock_file.return_value.read.return_value = json.dumps({
            "1": {
        "autor": "Agatha Christie",
        "titulo": "Diez Negritos",
        "genero": "Misterio",
        "isbn": 12345,
        "editorial": "HarperCollins",
        "anio_publicacion": 1939,
        "serie": "Hercule Poirot",
        "nro_paginas": 264,
        "cant_ejemplares": 7,
        "disponibilidad": True,
        "ejemplares_disponibles": 2,
        "ejemplares_alquilados": 5
    }
        })
        result = bu.editar_libros(12345, 0, "Dani")
        self.assertIsNotNone(result)
        self.assertEqual(result["autor"], "Dani")

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.uu.agregar_libro_historial")
    @patch("utils.book_utils.uu.agregar_alquilados")
    def test_alquilar_libro(self, mock_agregar_alquilados, mock_agregar_historial, mock_file):
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"isbn": 12345, "ejemplares_disponibles": 5, "disponibilidad": True}
        })
        result = bu.alquilar_libro(12345, 3, "Usuario1")
        self.assertTrue(result[0])
        self.assertEqual(result[1], 5)

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.uu.agregar_penalizados")
    @patch("utils.book_utils.su.fecha_actual", return_value=datetime(2023, 1, 10))
    def test_devolver_libro(self, mock_fecha_actual, mock_agregar_penalizados, mock_file):
        mock_file.side_effect = [
            mock_open(read_data=json.dumps({
                "1": {"isbn": 12345, "ejemplares_disponibles": 2, "disponibilidad": False}
            })).return_value,
            mock_open(read_data=json.dumps({
                "Usuario1": [{"isbn": 12345, "fecha_prestamo": "2023-01-01 12:00:00", "fecha_devolucion": None}]
            })).return_value,
        ]
        result = bu.devolver_libro(12345, "Usuario1")
        self.assertTrue(result)

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_recomendaciones(self, mock_file):
        mock_file.side_effect = [
            mock_open(read_data=json.dumps({
                "1": {"titulo": "Libro1", "genero": "Ficcion", "isbn": 12345}
            })).return_value,
            mock_open(read_data=json.dumps({
                "Usuario1": [{"isbn": 54321}]
            })).return_value,
        ]
        result = bu.recomendaciones("Ficcion", "Usuario1")
        self.assertEqual(result, "Libro1")

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_borrar_libro(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps({
            "1": {"isbn": 12345}
        })
        result = bu.borrar_libro(12345)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
