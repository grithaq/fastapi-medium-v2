from src.core.config import settings


def test_setting_config():
    assert settings.PROJECT_NAME == "todo-fastapi-v2"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.VERSION == "0.1.0"
    assert settings.POSTGRES_HOST == "localhost"
    assert settings.POSTGRES_PORT == "5432"
    assert settings.POSTGRES_USER == "mint"
    assert settings.POSTGRES_PASSWORD == "m1nt0"
    assert settings.POSTGRES_DB == "todo_fastapi"
    assert settings.FIRST_SUPERUSER == "grithaq@gmail.com"
    assert settings.FIRST_SUPERUSER_PASSWORD == "gritsekali"