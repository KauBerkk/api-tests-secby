from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

USER_LOGIN = os.getenv("USER_LOGIN")
USER_PASSWORD = os.getenv("USER_PASSWORD")

ADMIN_LOGIN = os.getenv("ADMIN_LOGIN")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")