from sqlalchemy.exc import IntegrityError
from fastapi import Depends
from sqlalchemy.orm import Session

from libraries.domain.repositories import UserRepository
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO
from libraries.domain.entities.models import User
from libraries.adapters.outbound.db.session import get_db


class UserAlreadyExistsError(Exception): ...

class UserRepositoryImpl(UserRepository):
    def create_user(self, user: UserInDTO) -> UserOutDTO:
        db: Session = next(get_db())
        db_user = User(**user.model_dump())
        
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        except IntegrityError as err:
            db.rollback()
            if "users.name" in str(err) or "users.email" in str(err):
                raise UserAlreadyExistsError("Nome de usuário ou email já cadastrado.") from err
            raise
           
        return UserOutDTO.model_validate(db_user.__dict__)
