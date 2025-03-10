from fastapi import Depends

from libraries.domain.use_cases import CreateUserUseCase, RetrieveUsersUseCase
from libraries.adapters.outbound.db.user_repository_impl import UserRepositoryImpl
from libraries.adapters.outbound.db.session import get_db


def get_user_repository():
    return UserRepositoryImpl()


def get_create_user_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
):
    return CreateUserUseCase(user_repository)


def get_retrieve_users_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
):
    return RetrieveUsersUseCase(user_repository)
