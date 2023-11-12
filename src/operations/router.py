from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import operation
from .schemas import Operation

router = APIRouter(prefix="/operations", tags=["Operation"])


@router.get("/", response_model=List[Operation])
async def get_operations(
    operation_type: str,
    session: AsyncSession = Depends(get_async_session),
):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()
