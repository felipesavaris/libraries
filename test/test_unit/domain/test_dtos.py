from datetime import datetime, UTC

import pytest
from pydantic import ValidationError 

from libraries.domain.entities.dtos import UserDTO, UserInDTO, UserOutDTO


def test_user_dto_creation():
    user = UserDTO(name="Alice", email="alice@example.com")

    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_user_in_dto_creation():
    user = UserInDTO(name="Bob", email="bob@example.com", password="1234")

    assert user.name == "Bob"
    assert user.email == "bob@example.com"
    assert user.password == "1234"


def test_user_out_dto_creation():
    now = datetime.now(tz=UTC)

    user = UserOutDTO(name="Carol", email="carol@example.com", created_at=now, updated_at=now)

    assert user.name == "Carol"
    assert user.email == "carol@example.com"
    assert user.created_at == now
    assert user.updated_at == now


def test_user_dto_missing_fields():
    with pytest.raises(ValidationError):
        UserDTO()
    with pytest.raises(ValidationError):
        UserInDTO(name="Test", email="test@example.com")
    with pytest.raises(ValidationError):
        UserOutDTO(name="Test", email="test@example.com", created_at=datetime.now(tz=UTC))
