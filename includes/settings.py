import os

from dotenv import load_dotenv


BASE_PATH: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

load_dotenv(os.environ.get(BASE_PATH, ".env"))

CONDUCTOR_API_URL: str = os.environ.get("CONDUCTOR_API_URL")

REST_API_URL: str = os.environ.get("REST_API_URL")
