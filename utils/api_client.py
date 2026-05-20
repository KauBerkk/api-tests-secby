import requests
from utils.config import BASE_URL


class ApiClient:

    @staticmethod
    def register(username, email, password):
        return requests.post(
            f"{BASE_URL}/api/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password
            }
        )

    @staticmethod
    def login(username, password):
        return requests.post(
            f"{BASE_URL}/api/auth/login",
            json={
                "username": username,
                "password": password
            }
        )

    @staticmethod
    def get_token(username, password):
        response = ApiClient.login(username, password)
        return response.json()["access_token"]

    @staticmethod
    def get_my_profile(token):
        return requests.get(
            f"{BASE_URL}/api/profiles/me",
            headers={"Authorization": f"Bearer {token}"}
        )

    @staticmethod
    def get_profiles(token):
        return requests.get(
            f"{BASE_URL}/api/profiles/",
            headers={"Authorization": f"Bearer {token}"}
        )
    
    @staticmethod
    def delete_profile(token, account_id):

        return requests.delete(
            f"{BASE_URL}/api/profiles/{account_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
    
    @staticmethod
    def verify_token(token):

        return requests.post(
            f"{BASE_URL}/api/auth/verify",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )