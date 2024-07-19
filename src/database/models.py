# src/database/models.py

from typing import Optional, List
from sqlmodel import Field, SQLModel, Session
from fastapi.responses import JSONResponse
from src.database.connect import engine

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_year: int

    @classmethod
    def get_by_id(cls, book_id: int):
        with Session(engine) as session:
            try:
                book = session.query(cls).filter(cls.id == book_id).first()
                if book is None:
                    return JSONResponse(status_code=404, content={"message": "Book not found"})
                return book
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error retrieving book: {str(e)}"})

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            try:
                books = session.query(cls).all()
                return books
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error retrieving all books: {str(e)}"})

    @classmethod
    def create(cls, book_data):
        with Session(engine) as session:
            try:
                book = cls(**book_data.dict())
                session.add(book)
                session.commit()
                session.refresh(book)
                return book
            except Exception as e:
                session.rollback()
                return JSONResponse(status_code=500, content={"message": f"Error adding book: {str(e)}"})

    @classmethod
    def update(cls, book_id: int, book_data):
        with Session(engine) as session:
            try:
                book = cls.get_by_id(book_id)
                if isinstance(book, JSONResponse):
                    return book
                update_data = book_data.dict(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(book, key, value)
                session.commit()
                session.refresh(book)
                return book
            except Exception as e:
                session.rollback()
                return JSONResponse(status_code=500, content={"message": f"Error updating book: {str(e)}"})

    @classmethod
    def delete(cls, book_id: int):
        with Session(engine) as session:
            try:
                book = cls.get_by_id(book_id)
                if isinstance(book, JSONResponse):
                    return book
                session.delete(book)
                session.commit()
                return JSONResponse(status_code=200, content={"message": "Book deleted successfully"})
            except Exception as e:
                session.rollback()
                return JSONResponse(status_code=500, content={"message": f"Error deleting book: {str(e)}"})
