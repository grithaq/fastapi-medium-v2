from pydantic_settings import BaseSettings
from starlette.config import Config

config_env = Config(".env")


class Settings(BaseSettings):
    PROJECT_NAME: str = config_env("PROJECT_NAME", default="FastAPI Medium Level 2")

    API_V1_STR: str = config_env("API_V1_STR", default="/api/v1")
    SECRET_KEY: str = config_env("SECRET_KEY")
    VERSION: str = config_env("VERSION", default="1.0.0")

    ACCESS_TOKEN_EXPIRE_MINUTE: int = 60 * 24 * 3

    POSTGRES_HOST: str = config_env("POSTGRES_HOST")
    POSTGRES_PORT: str = config_env("POSTGRES_PORT")
    POSTGRES_USER: str = config_env("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config_env("POSTGRES_PASSWORD")
    POSTGRES_DB: str = config_env("POSTGRES_DB")

    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    FIRST_SUPERUSER: str = config_env("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = config_env("FIRST_SUPERUSER_PASSWORD")

    ALGORITHM: str = "HS256"


settings = Settings()
