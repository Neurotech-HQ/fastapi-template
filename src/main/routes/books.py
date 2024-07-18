from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connect import get_session
from src.schemas.book import BookCreate, BookRead, BookUpdate
from src.utilities.database_operations import get_all_books, get_book_by_id,  add_book,  delete_book_by_id

router = APIRouter()

@router.post("/books", response_model=BookRead)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    return add_book(book, session)

@router.get("/books", response_model=list[BookRead])
def read_books(session: Session = Depends(get_session)):
    return get_all_books(session)

@router.get("/books/{book_id}", response_model=BookRead)
def read_book(book_id: int, session: Session = Depends(get_session)):
    return get_book_by_id(book_id, session)

@router.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookUpdate, session: Session = Depends(get_session)):
    return update_book(book_id, book, session)

@router.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    return delete_book_by_id(book_id, session)
