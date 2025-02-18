from abc import ABC, abstractmethod

from libraries.domain.entities.dtos import UserIn, UserOut


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserIn) -> UserOut:
        raise NotImplementedError()
