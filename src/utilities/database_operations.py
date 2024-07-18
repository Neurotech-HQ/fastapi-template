# src/utilities/database_operations.py

from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from src.database.models import Book


def get_book_by_id(book_id: int, session: Session):
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if book is None:
            return JSONResponse(status_code=404, content={"message": "Book not found"})
        return book
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error retrieving book: {str(e)}"})


def add_book(book_data, session: Session):
    try:
        db_book = Book(**book_data.dict())
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book
    except Exception as e:
        session.rollback()
        return JSONResponse(status_code=500, content={"message": f"Error adding book: {str(e)}"})


def get_all_books(session: Session) -> List[Book]:
    try:
        books = session.query(Book).all()
        return books
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error retrieving all books: {str(e)}"})

def update_book_data(db_book, book_data):
    try:
        update_data = book_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        Session.commit()
        Session.refresh(db_book)
        return db_book
    except Exception as e:
        Session.rollback()
        return JSONResponse(status_code=500, content={"message": f"Error updating book: {str(e)}"})


def delete_book_by_id(book_id: int, session: Session):
    try:
        db_book = session.query(Book).filter(Book.id == book_id).first()
        if db_book:
            session.delete(db_book)
            session.commit()
            return {"message": "Book deleted successfully"}
        return JSONResponse(status_code=404, content={"message": "Book not found"})
    except Exception as e:
        session.rollback()
        return JSONResponse(status_code=500, content={"message": f"Error deleting book: {str(e)}"})
