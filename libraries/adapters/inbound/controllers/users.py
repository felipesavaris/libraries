from fastapi import APIRouter, Depends

from libraries.adapters.inbound.dependencies import get_create_user_use_case
from libraries.domain.entities.dtos import UserInDTO, UserOutDTO
from libraries.domain.use_cases import CreateUserUseCase

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOutDTO, status_code=201)
def create_user(user: UserInDTO, use_case: CreateUserUseCase = Depends(get_create_user_use_case)):
    return use_case.execute(user)
