from sqlalchemy.exc import IntegrityError
from fastapi import Depends
from sqlalchemy.orm import Session

from libraries.domain.repositories import UserRepository
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO, UserDTO
from libraries.domain.entities.models import UserModel
from libraries.adapters.outbound.db.session import get_db


class UserAlreadyExistsError(Exception): ...

class UserRepositoryImpl(UserRepository):
    def create_user(self, user: UserInDTO) -> UserOutDTO:
        db: Session = next(get_db())
        db_user = UserModel(**user.model_dump())
        
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

    def retrieve_users(self, params: UserDTO) -> list[UserOutDTO]:
        db: Session = next(get_db())
        query = db.query(UserModel)
        
        if params.name:
            query = query.filter(UserModel.name == params.name)
        if params.email:
            query = query.filter(UserModel.email == params.email)

        return [UserOutDTO.model_validate(user.__dict__) for user in query.all()]
