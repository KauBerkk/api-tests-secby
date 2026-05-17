import random

from utils.api_client import ApiClient


def test_register_user():

    random_number = random.randint(1, 99999)

    username = f"testuser{random_number}"

    email = f"test{random_number}@gmail.com"

    password = "Test12345!"

    response = ApiClient.register(
        username,
        email,
        password
    )

    assert response.status_code in [200, 201]