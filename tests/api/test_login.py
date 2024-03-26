from src.api.api_v1.endpoints.login import login_access_token
from fastapi.security import OAuth2PasswordRequestForm
from src.db.session import SessionLocal

db = SessionLocal()

form_data = OAuth2PasswordRequestForm(
    username="grithaq@gmail.com", password="gritsekali"
)


def test_login_with_correct_credentials():
    response = login_access_token(form_data=form_data, db=db)
    assert response['token_type'] == "bearer"