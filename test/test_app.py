import pytest


def test_app_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_app_bad_scorer(client):
    response = client.post("/model/score/foo")
    assert response.status_code == 422
