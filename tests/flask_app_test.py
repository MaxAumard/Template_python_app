import pytest
from src.template_python_application.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_index_status(client):
    response = client.get('/')
    print(response.data)
    assert response.status_code == 200
