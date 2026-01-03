from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import MovieModel
from src.database import get_db


async def get_movies(
        db: AsyncSession = Depends(get_db),
        page: int = 1,
        per_page: int = 10
) -> List[MovieModel]:
    stmt = select(MovieModel)


