import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    # On vérifie maintenant si le titre de notre HTML est présent
    assert b"Application DevOps" in rv.data
