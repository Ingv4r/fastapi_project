from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from auth.models import User, user
from auth.schemas import UserRead

from auth.base_config import current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def protected_route(user: User = Depends(current_user)):
    response = {
        'username': user.username,
        'email': user.email,
        'role': user.role_id,
        'registered_at': user.registered_at
    }
    return response


@router.get('/users', response_model=List[UserRead])
async def get_users_list(session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    return result.all()
