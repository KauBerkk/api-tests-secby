import allure

from utils.api_client import ApiClient
from utils.assertions import assert_status_code


@allure.feature("Profile")
def test_get_my_profile(test_user):

    response = ApiClient.get_my_profile(
        test_user["token"]
    )

    assert_status_code(response, 200)
    response_data = response.json()

    assert test_user["username"] in str(response_data)
    assert test_user["email"] in str(response_data)


@allure.feature("Profile")
def test_get_profile_invalid_token():

    response = ApiClient.get_my_profile(
        "invalid_token"
    )

    assert_status_code(response, 401)


@allure.feature("Profile")
def test_get_profile_without_token():

    response = ApiClient.get_my_profile(
        ""
    )

    assert_status_code(response, 403)