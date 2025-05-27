import pytest

from libraries.domain.entities.models import UserModel


def test_user_model_initialization():
    user = UserModel(name='Felps', email='felps@sava.com', password='123')

    assert user.name == 'Felps'
    assert user.email == 'felps@sava.com'
    assert user.password == '123'
    assert user.created_at is None
    # assert user.updated_at is None


def test_user_model_missing_name():
    with pytest.raises(TypeError):
        UserModel(email='felps@sava.com', password='123')


def test_user_model_missing_email():
    with pytest.raises(TypeError):
        UserModel(name='Felps', password='123')


def test_user_model_missing_password():
    with pytest.raises(TypeError):
        UserModel(name='Felps', email='felps@sava.com')


def test_user_model_unique_constraints():
    user1 = UserModel(name='Felps', email='felps@sava.com', password='123')
    user2 = UserModel(name='Felps', email='felps@other.com', password='456')
    user3 = UserModel(name='Other', email='felps@sava.com', password='789')

    assert user1.name == user2.name
    assert user1.email != user2.email
    assert user1.email == user3.email
    assert user1.name != user3.name
