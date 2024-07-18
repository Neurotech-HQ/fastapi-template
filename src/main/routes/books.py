from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.models import Book
from src.schemas.book import BookCreate, BookRead, BookUpdate
from src.database.connect import get_session

router = APIRouter()

@router.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    db_book = Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.get("/books/", response_model=list[BookRead])
def read_books(session: Session = Depends(get_session)):
    books = session.query(Book).all()
    return books

@router.get("/books/{book_id}", response_model=BookRead)
def read_book(book_id: int, session: Session = Depends(get_session)):
    db_book = session.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookUpdate, session: Session = Depends(get_session)):
    db_book = session.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    db_book = session.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(db_book)
    session.commit()
    return {"message": "Book deleted successfully"}
