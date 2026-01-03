import datetime
from typing import List

from pydantic import BaseModel
from database.models import MovieStatusEnum


class Pagination(BaseModel):
    prev_page: str | None = None
    next_page: str | None = None
    total_pages: int | None = None
    items_per_page: int | None = None


class Genre(BaseModel):
    id: int
    name: str

class MovieBase(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country_id: int


class MovieRead(BaseModel, Pagination):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str


    class Config:
        from_attributes = True
