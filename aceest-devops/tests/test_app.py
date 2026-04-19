import pytest

from app import app
from app.main import init_db

@pytest.fixture
def client():
    init_db()  # Ensure the database is initialized before running tests
    app.testing = True
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ACEest is running!' in response.data

def test_add_client(client):
    response = client.post('/clients', json={
        "name": "TestUser",
        "age": 30,
        "weight": 80
    })
    assert response.status_code == 200
    assert b'Client created successfully' in response.data

def test_get_clients(client):
    response = client.get('/clients')
    assert response.status_code == 200
    assert b'TestUser' in response.data