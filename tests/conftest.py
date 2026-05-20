import pytest
import random

from utils.api_client import ApiClient


@pytest.fixture
def test_user():

    number = random.randint(1000, 9999)

    username = f"user{number}"
    email = f"user{number}@mail.com"
    password = "Test12345!"

    register_response = ApiClient.register(
        username,
        email,
        password
    )

    login_response = ApiClient.login(
        username,
        password
    )

    response_data = login_response.json()

    token = response_data["access_token"]

    account_id = response_data["user"]["id"]

    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "token": token,
        "account_id": account_id
    }

    yield user_data

    ApiClient.delete_profile(
        token,
        account_id
    )