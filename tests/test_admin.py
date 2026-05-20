import allure

from utils.api_client import ApiClient
from utils.config import ADMIN_LOGIN, ADMIN_PASSWORD
from utils.assertions import assert_status_code

def get_admin_token():

    response = ApiClient.login(
        ADMIN_LOGIN,
        ADMIN_PASSWORD
    )

    response_data = response.json()

    return response_data["access_token"]


@allure.feature("Admin")
@allure.story("Admin login")
def test_admin_login_success():

    response = ApiClient.login(
        ADMIN_LOGIN,
        ADMIN_PASSWORD
    )

    assert_status_code(response, 200)

    response_data = response.json()

    assert "access_token" in response_data


@allure.feature("Admin")
@allure.story("Admin role validation")
def test_admin_role():

    response = ApiClient.login(
        ADMIN_LOGIN,
        ADMIN_PASSWORD
    )

    response_data = response.json()

    assert response_data["user"]["role"]["name"] == "admin"


@allure.feature("Admin")
@allure.story("Admin can access profiles")
def test_admin_can_get_profiles():

    token = get_admin_token()

    response = ApiClient.get_profiles(token)

    assert_status_code(response, 200)

    response_data = response.json()

    assert len(response_data) > 0