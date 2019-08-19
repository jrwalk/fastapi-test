import pytest

from starlette.testclient import TestClient

from app.app import app


@pytest.fixture(scope='module')
def client():
    return TestClient(app)
