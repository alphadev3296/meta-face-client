from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_TITLE: str = "FastAPI Template"
    APP_NAME: str = "FastAPI Template"
    APP_VERSION: str = "0.1.0"
    APP_URL: str = "https://fastapi-template.vercel.app"
    APP_EMAIL: str = "xqg5o@example.com"

    APP_PORT: int = 8000

    DEBUG: bool = True


config = Config()
