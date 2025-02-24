from abc import ABC, abstractmethod

from libraries.domain.entities.dtos import UserInDTO, UserOutDTO


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserInDTO) -> UserOutDTO:
        raise NotImplementedError()
