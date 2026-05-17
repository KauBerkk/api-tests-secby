import pytest
import random
from utils.api_client import ApiClient


@pytest.fixture
def test_user():

    num = random.randint(1000, 9999)

    username = f"user{num}"
    email = f"user{num}@mail.com"
    password = "Test12345!"

    ApiClient.register(username, email, password)

    return {
        "username": username,
        "password": password
    }


@pytest.fixture
def user_token(test_user):

    response = ApiClient.login(
        test_user["username"],
        test_user["password"]
    )

    return response.json()["access_token"]