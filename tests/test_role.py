import allure
from utils.api_client import ApiClient
from utils.assertions import assert_status_code


@allure.feature("Roles")
def test_token_contains_role(test_user):

    response = ApiClient.login(
        test_user["username"],
        test_user["password"]
    )

    data = response.json()

    assert data["user"]["role"]["name"] == "user"