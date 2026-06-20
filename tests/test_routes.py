import pytest
from app import app
import os
import jwt
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture

def cliente():

    app.config['TESTING'] = True

    app.secret_key = 'llave_secreta_para_pruebas'

    with app.test_client() as client:

        yield client

def test_pagina_inicio_carga_correctamente(cliente):

    with cliente.session_transaction() as sesion_falsa:
        sesion_falsa['nombre_usuario'] = 'victoria'

    respuesta = cliente.get('/Inicio')

    assert respuesta.status_code == 200

    assert b"Ventas" in respuesta.data


def test_generar_pdf(cliente):

    llave_secreta = os.getenv("SECRET_KEYJWT", "ProbandoJWT2026")
    token_prueba = jwt.encode({"usuario_id": 1, "Nombre_Usuario": "victoria"}, llave_secreta, algorithm="HS256")


    with cliente.session_transaction() as sesion_falsa:

        sesion_falsa['nombre_usuario'] = 'victoria'

        sesion_falsa['archivo_actual'] = 'ventas_juguete.csv'
        sesion_falsa['total_ventas_dinero'] = 2500.50
        sesion_falsa['total_productos_vendidos'] = 14
        sesion_falsa['ticket_promedio'] = 178.60

    respuesta = cliente.post('/Inicio', data={'generar-pdf': 'true'})

    assert respuesta.status_code == 200