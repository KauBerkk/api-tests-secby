import allure
from utils.api_client import ApiClient
from data.payloads import invalid_login_payload
from utils.assertions import assert_status_code

@allure.feature("Auth")
def test_login_success(test_user):

    response = ApiClient.login(
        test_user["username"],
        test_user["password"]
    )

    assert_status_code(response, 200)

    assert "access_token" in response.json()

    response_data = response.json()

    assert response_data["user"]["username"] == test_user["username"]
    assert response_data["user"]["email"] == test_user["email"]


@allure.feature("Auth")
def test_login_invalid():

    response = ApiClient.login(
        invalid_login_payload["username"],
        invalid_login_payload["password"]
    )

    assert_status_code(response, 401)