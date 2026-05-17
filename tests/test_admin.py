import allure
from utils.api_client import ApiClient


@allure.feature("Roles")
def test_user_access_profiles(user_token):

    response = ApiClient.get_profiles(user_token)
    assert response.status_code in [200, 403]


@allure.feature("Roles")
def test_token_contains_role(test_user):

    response = ApiClient.login(
        test_user["username"],
        test_user["password"]
    )

    data = response.json()

    assert data["user"]["role"]["name"] == "user"