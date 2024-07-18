from typing import Optional
from sqlmodel import SQLModel

class BookBase(SQLModel):
    title: str
    author: str
    publication_year: int

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
