from abc import ABC, abstractmethod

from libraries.domain.entities.dtos import UserInDTO, UserOutDTO, UserDTO


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserInDTO) -> UserOutDTO:
        raise NotImplementedError()

    @abstractmethod
    def retrieve_users(self, params: UserDTO) -> list[UserOutDTO]:
        raise NotImplementedError()
