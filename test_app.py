import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Vérifie que la page d'accueil répond bien 200 (OK) et contient 'Hello'"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello" in rv.data
