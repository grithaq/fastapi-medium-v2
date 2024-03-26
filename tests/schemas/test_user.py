from src.schemas.user import UserBase, UserCreate, UserUpdate


def test_user_base():
    user = UserBase(
        email="test@gmail.com",
        full_name="Test aja"
    )
    assert user.email == "test@gmail.com"
    assert user.is_active == None
    assert user.is_superuser == False
    assert user.full_name == "Test aja"


def test_user_create_schema():
    user = UserCreate(
        email="test@gmail.com",
        password="test",
        full_name="Test aja"
    )
    assert user.email == "test@gmail.com"
    assert user.password == "test"
    assert user.full_name == "Test aja"
    assert user.is_active == None
    assert user.is_superuser == False


def test_user_update_schema():
    user = UserUpdate(
        email="test@gmail.com",
        password="ganti test",
        full_name="Test aja"
    )
    assert user.email == "test@gmail.com"
    assert user.password != "test"
    assert user.full_name == "Test aja"
    assert user.is_active == None
    assert user.is_superuser == False