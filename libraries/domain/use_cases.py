from libraries.domain.entities.dtos import UserInDTO, UserOutDTO
from libraries.domain.repositories import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user: UserInDTO) -> UserOutDTO:
        return self.user_repository.create_user(user)


class RetrieveUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, params: UserInDTO) -> list[UserOutDTO]:
        return self.user_repository.retrieve_users(params)
