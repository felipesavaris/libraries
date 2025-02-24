from fastapi import HTTPException, status

from libraries.adapters.outbound.db.user_repository_impl import UserAlreadyExistsError
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO
from libraries.domain.repositories import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user: UserInDTO) -> UserOutDTO:
        try:
            return self.user_repository.create_user(user)
        except UserAlreadyExistsError as err:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err)) from err
