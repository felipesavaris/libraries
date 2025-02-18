from libraries.domain.entities.dtos import UserIn, UserOut
from libraries.domain.repositories import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user: UserIn) -> UserOut:
        return self.user_repository.create_user(user)
