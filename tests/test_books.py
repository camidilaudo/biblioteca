import unittest
from unittest.mock import patch, mock_open
import json
from datetime import datetime
from utils import book_utils as bu


class TestBookUtils(unittest.TestCase):

    @patch("utils.book_utils.open", new_callable=mock_open, read_data=json.dumps({}))
    def test_stock_json(self, mock_file):
        """
        Verifica si un libro está en stock en el JSON.

        Precondición:
        - Que el ISBN sea un numero entero.

        Resultado esperado:
        - False si el libro no está en stock.
        - True si el libro está en stock.
        """
        # Caso libro no encontrado
        isbn = 12345
        result = bu.stock_json(isbn)
        self.assertFalse(result)

        # Caso libro encontrado
        mock_file.return_value.read.return_value = json.dumps({"1": {"isbn": 12345}})
        result = bu.stock_json(isbn)
        self.assertTrue(result)

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_busqueda_libros(self, mock_file):
        """
        Verifica que la funcion buscar_libros por un campo y valor específicos funcione correctamente.

        Precondición:
        - Ingreso del Str campo y valor por el cual se quiere realizar la búsqueda.

        Resultado esperado:
        - La funcion devuelve una lista con el libro encontrado.
        - La informacion del libro debe coincidir con el valor buscado.
        """

        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"titulo": "Libro1", "autor": "Autor1"}}
        )
        result = bu.busqueda_libros("titulo", "Libro1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["titulo"], "Libro1")

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_cargar_libros(self, mock_file):
        """
        Verifica que la función cargar_libros, que pueda añadir un nuevo libro al JSON con los valores ingresados.

        Precondiciones :
        - Título : debe ser una cadena no vacía.
        - Autores y géneros : deben ser listas de cadenas no vacías.
        - ISBN : debe ser un número entero.
        - Editorial : debe ser una cadena no vacía.
        - Año : debe ser un número entero representando un año válido.
        - Número de páginas y la cantidad : deben ser números enteros positivos

        Postcondiciones:
        - Devuelve un diccionario con el libro recien añadido.
        - Los valores del libro deben coincidir con los input.

        """
        mock_file.return_value.read.return_value = json.dumps({})
        result = bu.cargar_libros(
            "Libro1", ["Autor1"], ["Genero1"], 12345, "Editorial1", 2023, None, 300, 5
        )
        self.assertIn("1", result)
        self.assertEqual(result["1"]["titulo"], "Libro1")

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_obtener_libro(self, mock_file):
        """
        Verifica que la funcion obtener_libro, busque un libro en la biblioteca utilizando el ISBN como parámetro.

        Precondiciones:
        - El ISBN debe ser un Int, que se encuentre en la biblioteca.

        Postcondiciones:
        - El return de la funcion no debe ser None
        - El libro obtenido debe tener el mismo ISBN que el del parametro.
        """
        mock_file.return_value.read.return_value = json.dumps({"1": {"isbn": 12345}})
        result = bu.obtener_libro(12345)
        self.assertIsNotNone(result)
        self.assertEqual(result[1]["isbn"], 12345)

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.su.validacion_cantidades", return_value=10)
    def test_editar_libros(self, mock_validacion, mock_file):
        """
        Verifica que la función editar_libros, modifique un valor de un libro pasado como parametro en el JSON.

        Precondiciones:
        - ISBN : Int, que pertenezca a un libro en el JSON.
        - Campo : debe ser un índice del elemento del archivo que se quiere editar.
        - Valor : debe ser un dato a reemplazar el valor del campo actual

        Postcondiciones:
        - El libro, en el JSON se debe actualizarse con el nuevo valor en el campo especificado.
        - La función debe devolver un diccionario con el libro modificado y el nuevo valor.
        - La función reescribe el archivo para guardar los cambios realizados en el JSON = books_data.json
        - Si el campo no existe o el valor proporcionado no es válido, la función debería manejar el error de manera adecuada.
        """
        mock_file.return_value.read.return_value = json.dumps(
            {
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
                    "ejemplares_alquilados": 5,
                }
            }
        )
        result = bu.editar_libros(12345, 0, "Dani")
        self.assertIsNotNone(result)
        self.assertEqual(result["autor"], "Dani")

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.uu.agregar_libro_historial")
    @patch("utils.book_utils.uu.agregar_alquilados")
    def test_alquilar_libro(
        self, mock_agregar_alquilados, mock_agregar_historial, mock_file
    ):
        """
        Verifica que la función alquilar_libro, pueda alquilae un libro disponible en la biblioteca a un usuario no penalizado.

        Precondiciones:
        - El libro del ISBN pasado como parámetro debe existir en el JSON y estar disponible.
        - La cantidad de ejemplares que se quiere alquilar debe ser menor o igual a los disponibles.
        - El usuario que alquila debe existir en el sistema y no estar penalizado.

        Postcondiciones:
        - El JSON debe actualizarse, disminuyendo los ejemplares disponibles del libro alquilado
        - La función debe devolver una tupla que el primer valor sea True (que se alquilo correctamente)) y el segundo sea el número actualizado de ejemplares disponibles
        - El alquiler se debe guardar en los libros alquilados y en el historial del usuario en el sistema.
        - Si se alquila correctamente, no debe haber excepciones.
        """
        mock_file.return_value.read.return_value = json.dumps(
            {"1": {"isbn": 12345, "ejemplares_disponibles": 5, "disponibilidad": True}}
        )
        result = bu.alquilar_libro(12345, 3, "Usuario1")
        self.assertTrue(result[0])
        self.assertEqual(result[1], 5)

    @patch("utils.book_utils.open", new_callable=mock_open)
    @patch("utils.book_utils.uu.agregar_penalizados")
    @patch("utils.book_utils.su.fecha_actual", return_value=datetime(2023, 1, 10))
    def test_devolver_libro(
        self, mock_fecha_actual, mock_agregar_penalizados, mock_file
    ):
        """
        Verifica que la función devolver_libro, devuelva un alquilado anteriormente por un usuario y actualice el historial del usuario, la cantidad de ejemplares disponibles, y la detección de penalizaciones.

        Precondiciones:
        - withdrawn_books_per_user.json debe tener el ISBN, fecha de alquiler y devolucion para el usuario que alquilo
        - Se debe pasar como parametro la fecha de devolución
        - La función debe agregar_penalizados, para gestionar la sancion.

        Postcondiciones:
        - El JSON debe actualizarse, incrementando el número de ejemplares disponibles y reduciendo los ejemplares alquilados.
        - withdrawn_books_per_user.json debe registrar la fecha de devolución del libro.
        - La función devuelve True si se devolvio correctamente o False si hubo un error
        - Si la devolución es mayor a la fecha estimada de la devolucion, la función debe guardar penalización del usuario y gestionarla.
        - La función debe reescribir en el JSON los cambios.

        """
        # Mock para books_data.json
        mock_books = mock_open(
            read_data=json.dumps(
                {
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
                        "ejemplares_alquilados": 5,
                    }
                }
            )
        )

        # Mock para withdrawn_books_per_user.json
        mock_historial = mock_open(
            read_data=json.dumps(
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
        )

        # Definir side_effect para devolver diferentes mocks según el archivo
        def mock_file_side_effect(filepath, mode, *args, **kwargs):
            if filepath == "./data_store/books_data.json" and mode == "r":
                return mock_books()
            elif (
                filepath == "./data_store/withdrawn_books_per_user.json" and mode == "r"
            ):
                return mock_historial()
            elif filepath == "./data_store/books_data.json" and mode == "w":
                return mock_books()
            elif (
                filepath == "./data_store/withdrawn_books_per_user.json" and mode == "w"
            ):
                return mock_historial()
            else:
                raise FileNotFoundError(f"Archivo inesperado: {filepath}")

        mock_file.side_effect = mock_file_side_effect

        # Llamar a la función
        result = bu.devolver_libro(12345, "Usuario1")

        # Verificar que el libro fue devuelto correctamente
        self.assertTrue(result)

        # Verificar que el estado del libro cambió
        mock_books().write.assert_called()
        mock_historial().write.assert_called()

        # Verificar que se aplicaron penalizaciones
        mock_agregar_penalizados.assert_called()

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_recomendaciones(self, mock_file):
        """
        Verifica que la función recomendaciones, recomiende un libro a un usuario basado en un campo específico y el historial de libros leidos.

        Precondiciones:
        - Genero : Str. Debe contener algun genero valido
        - Usuario: Str. Debe ser un usuario existente.

        Postcondiciones:
        - La función debe devolver el título de un libro que sea del género pasado por parametro y que el usuario no haya leído antes.
        - Si hay mas de uno, debe devolver uno random
        - Si el usuario leyo todos los libros del género o no hay libros disponibles, la función devuelve None
        """

        # Mock para books_data.json
        mock_books_data = json.dumps(
            {
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
                    "ejemplares_alquilados": 5,
                },
                "2": {
                    "autor": "Arthur Conan Doyle",
                    "titulo": "Estudio en Escarlata",
                    "genero": "Misterio",
                    "isbn": 54321,
                    "editorial": "George Newnes",
                    "anio_publicacion": 1887,
                    "serie": "Sherlock Holmes",
                    "nro_paginas": 188,
                    "cant_ejemplares": 3,
                    "disponibilidad": True,
                    "ejemplares_disponibles": 1,
                    "ejemplares_alquilados": 2,
                },
            }
        )

        # Mock para withdrawn_books_per_user.json
        mock_user_history = json.dumps(
            {"Usuario1": [{"isbn": 54321}]}  # Usuario ya leyó "Estudio en Escarlata"
        )

        # Configurar side_effect para devolver los datos adecuados
        mock_file.side_effect = [
            mock_open(read_data=mock_books_data).return_value,
            mock_open(read_data=mock_user_history).return_value,
        ]

        # Llamar a la función
        result = bu.recomendaciones("misterio", "Usuario1")

        # Verificar que el libro recomendado sea "Diez Negritos"
        self.assertEqual("Diez Negritos", result)

    @patch("utils.book_utils.open", new_callable=mock_open)
    def test_borrar_libro(self, mock_file):
        """
        Verifica que la función borrar_libro, elimine un libro específico existente en la biblioteca según su ISBN.

        Precondiciones:
        - El JSON debe tener un libro con un ISBN que coincida con el argumento.
        - El ISBN debe ser un número entero válido.

        Postcondiciones:
        - Si el libro existe se elimina del JSON.
        - El JSON se actualiza y sobreescribe.
        - La funcion devuelve True si la eliminación fue exitosa O False si el libro no existe o hubo un error en el proceso.
        """

        mock_file.return_value.read.return_value = json.dumps({"1": {"isbn": 12345}})
        result = bu.borrar_libro(12345)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
