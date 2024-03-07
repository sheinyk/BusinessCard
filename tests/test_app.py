import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_workout_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"submit" in response.data


