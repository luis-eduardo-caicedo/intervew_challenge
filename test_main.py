from fastapi.testclient import TestClient
from fastapi import status
from .main import app

client = TestClient(app)


def test_gets_users():
    response = client.get("/api/v1/list/user")
    assert response.status_code == status.HTTP_200_OK


def test_create_user_correct():
    response = client.post(
        "/api/v1/create/user",
        json={
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "password": "string",
            "address_1": "string",
            "address_2": "string",
            "city": "string",
            "state": "string",
            "zip": 0,
            "country": "string",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED


def test_create_user_error_type():
    response = client.post(
        "/api/v1/create/user",
        json={
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "password": "string",
            "address_1": "string",
            "address_2": "string",
            "city": "string",
            "state": "string",
            "zip": "string",
            "country": "string",
        },
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
