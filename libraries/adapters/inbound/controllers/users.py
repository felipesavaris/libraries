from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from libraries.adapters.inbound.dependencies import get_create_user_use_case, get_retrieve_users_use_case
from libraries.adapters.outbound.db.user_repository_impl import UserAlreadyExistsError
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO, UserDTO
from libraries.domain.use_cases import CreateUserUseCase, RetrieveUsersUseCase

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOutDTO, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserInDTO, use_case: CreateUserUseCase = Depends(get_create_user_use_case)
) -> UserOutDTO:
    try:
        return use_case.execute(user)
    except UserAlreadyExistsError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err)) from err


@router.get("/", response_model=List[UserOutDTO], status_code=status.HTTP_200_OK)
def retrieve_users(
    name: str = '', 
    email: str = '', 
    use_case: RetrieveUsersUseCase = Depends(get_retrieve_users_use_case),
) -> list[UserOutDTO]:
    params: UserDTO = UserDTO(name=name, email=email)

    return use_case.execute(params)
