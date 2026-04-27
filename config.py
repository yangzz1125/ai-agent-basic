import os 
from dotenv import load_dotenv, find_dotenv
# Load environment variables from .env file
load_dotenv(find_dotenv())

class Settings:
    API_KEY: str
    BASE_URL: str
    MODEL_NAME: str
    APP_ENV: str
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.BASE_URL = os.getenv("BASE_URL")
        self.MODEL_NAME = os.getenv("MODEL_NAME")
        self.APP_ENV = os.getenv("APP_ENV")

        if not self.API_KEY:
            raise ValueError("API_KEY is not set in the environment variables.")

settings = Settings()