from src.core.security import get_password_hash, verify_password

password = "bakwan anyep"


def test_hashing_password():
    hashed_password = get_password_hash(password)
    assert hashed_password != password


def test_verify_password():
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)