import allure
from utils.api_client import ApiClient


@allure.feature("Auth")
def test_login_success(test_user):

    response = ApiClient.login(
        test_user["username"],
        test_user["password"]
    )

    assert response.status_code == 200

    assert "access_token" in response.json()


@allure.feature("Auth")
def test_login_invalid():

    response = ApiClient.login("wrong", "wrong")

    assert response.status_code in [400, 401]