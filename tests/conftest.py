from typing import Generator
import pytest
from src.db.session import SessionLocal
from src.api.deps import get_current_user
from src.main import crate_application
from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    application = crate_application()
    with TestClient(application) as c:
        yield c