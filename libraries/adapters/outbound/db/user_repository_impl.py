from fastapi import Depends
from sqlalchemy.orm import Session

from libraries.domain.repositories import UserRepository
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO
from libraries.domain.entities.models import User
from libraries.adapters.outbound.db.session import get_db


class UserRepositoryImpl(UserRepository):
    def create_user(self, user: UserInDTO) -> UserOutDTO:
        db: Session = next(get_db())
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return UserOutDTO.model_validate(db_user.__dict__)
