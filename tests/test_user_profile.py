import allure

from utils.api_client import ApiClient
from utils.config import USER_LOGIN, USER_PASSWORD


def get_token():

    response = ApiClient.login(
        USER_LOGIN,
        USER_PASSWORD
    )

    response_data = response.json()

    if "token" in response_data:
        return response_data["token"]

    return response_data["access_token"]


@allure.feature("Profile")
def test_get_my_profile():

    token = get_token()

    response = ApiClient.get_my_profile(token)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data is not None