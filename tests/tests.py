import pytest
from unittest.mock import patch, mock_open
import json
import utils.book_utils as bu
import utils.users_utils as us


# Fixture para los datos de usuarios
@pytest.fixture
def mock_users_data():
    users_data = {
        "1": {"tipo_usuario": 2, "nombre": "cliente1", "contrasenia": "Cliente123", "esta_penalizado": False,
              "fecha_despenalizacion": None},
        "2": {"tipo_usuario": 1, "nombre": "bibliotecario1", "contrasenia": "Biblio123", "esta_penalizado": False,
              "fecha_despenalizacion": None}
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(users_data))):
        yield users_data  # Solo yield aquí para devolver los datos


# Fixture para los datos de libros
@pytest.fixture
def mock_books_data():
    books_data = {
        "1": {"autor": "Autor1", "titulo": "Libro1", "genero": "Ficción", "isbn": 123456, "editorial": "Editorial1",
              "anio_publicacion": 2020, "serie": None, "nro_paginas": 200, "cant_ejemplares": 5, "disponibilidad": True,
              "ejemplares_disponibles": 5, "ejemplares_alquilados": 0}
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(books_data))):
        yield books_data  # Solo yield aquí para devolver los datos


# Casos de prueba para inicio de sesión
def test_iniciar_sesion_cliente_existente(mock_users_data):
    with patch("builtins.input", side_effect=["cliente1", "Cliente123"]):
        resultado = us.login_usuario("cliente1", "Cliente123")
        assert resultado == 2  # Tipo usuario: Cliente


def test_iniciar_sesion_bibliotecario_existente(mock_users_data):
    with patch("builtins.input", side_effect=["bibliotecario1", "Biblio123"]):
        resultado = us.login_usuario("bibliotecario1", "Biblio123")
        assert resultado == 1  # Tipo usuario: Bibliotecario


def test_iniciar_sesion_usuario_inexistente(mock_users_data):
    with patch("builtins.input", side_effect=["usuario_inexistente", "12345"]):
        resultado = us.login_usuario("usuario_inexistente", "12345")
        assert resultado == -1  # Usuario no existe


# Casos de prueba para registro de usuarios
def test_registrar_cliente(mock_users_data):
    with patch("builtins.input", side_effect=["cliente_nuevo", "Cliente123", "Cliente123"]):
        resultado = us.registrar_usuario(2, "cliente_nuevo", "Cliente123")
        assert resultado is True  # Registro exitoso


def test_registrar_bibliotecario(mock_users_data):
    with patch("builtins.input", side_effect=["biblio_nuevo", "Biblio123", "Biblio123"]):
        resultado = us.registrar_usuario(1, "biblio_nuevo", "Biblio123")
        assert resultado is True  # Registro exitoso


def test_registrar_usuario_existente(mock_users_data):
    with patch("builtins.input", side_effect=["cliente1", "Cliente123", "Cliente123"]):
        resultado = us.registrar_usuario(2, "cliente1", "Cliente123")
        assert resultado is False  # El usuario ya existe

# Casos de prueba para carga de libros
def test_cargar_libro(mock_books_data):
    with patch("builtins.input",
               side_effect=["Nuevo Libro", "Autor Nuevo", "Ficción", "987654", "Editorial XYZ", "2023", "Serie A",
                            "300", "10"]):
        resultado = bu.cargar_libros("Nuevo Libro", "Autor Nuevo", "Ficción", 987654, "Editorial XYZ", 2023, "Serie A",
                                     300, 10)
        assert resultado is not None  # Se cargó correctamente el libro


# Casos de prueba para alquilar libros
def test_alquilar_libro(mock_books_data):
    with patch("builtins.input", side_effect=["123456", "2"]):
        resultado = bu.alquilar_libro(123456, 2, "cliente1")
        assert resultado[0] == True  # El libro fue alquilado correctamente


# Casos de prueba para devolver libros
def test_devolver_libro(mock_books_data):
    with patch("builtins.input", side_effect=["123456", "cliente1"]):
        resultado = bu.devolver_libro(123456, "cliente1")
        assert resultado is True  # El libro fue devuelto correctamente


# Casos de prueba para buscar libros
def test_buscar_libros_existentes(mock_books_data):
    with patch("builtins.input", side_effect=["titulo", "Libro1"]):
        resultado = bu.busqueda_libros("titulo", "Libro1")
        assert len(resultado) > 0  # Se encontró el libro


def test_buscar_libros_inexistentes(mock_books_data):
    with patch("builtins.input", side_effect=["titulo", "Libro Inexistente"]):
        resultado = bu.busqueda_libros("titulo", "Libro Inexistente")
        assert len(resultado) == 0  # No se encontró el libro


# Casos de prueba para recomendaciones
def test_recomendacion_genero_ya_leido(mock_books_data):
    with patch("builtins.input", side_effect=["Ficción"]):
        resultado = bu.recomendaciones("Ficción", "cliente1")
        assert resultado is not None  # Se recomienda un libro


def test_recomendacion_genero_inexistente(mock_books_data):
    with patch("builtins.input", side_effect=["Ciencia Ficción"]):
        resultado = bu.recomendaciones("Ciencia Ficción", "cliente1")
        assert resultado is None  # No hay libros recomendados
