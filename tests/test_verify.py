from utils.api_client import ApiClient
from utils.assertions import assert_status_code


def test_verify_token(test_user):

    response = ApiClient.verify_token(
        test_user["token"]
    )

    assert_status_code(response, 200)