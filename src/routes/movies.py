from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.schemas.movies import MovieRead
from database import get_db, MovieModel
from database.models import CountryModel, GenreModel, ActorModel, LanguageModel


router = APIRouter()

@router.get("/movies/", response_model=List[MovieModel])
def get_movies(
        db: AsyncSession = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number, >= 1"),
        per_page: int = Query(10, ge=1, le=20, description="Items per page, 1-20"),
):
    pass