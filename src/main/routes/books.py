# src/main/routes/books.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
from src.utilities.database_operations import get_all_books, get_book_by_id, add_book, update_book_data, delete_book_by_id

router = APIRouter()

class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None

@router.get("/", response_class=JSONResponse)
async def read_books():
    response = get_all_books()
    return response

@router.get("/{book_id}", response_class=JSONResponse)
async def read_book(book_id: int):
    response = get_book_by_id(book_id)
    return response

@router.post("/", response_class=JSONResponse)
async def create_book(book_data: BookCreate):
    response = add_book(book_data)
    return response

@router.put("/{book_id}", response_class=JSONResponse)
async def update_book(book_id: int, book_data: BookUpdate):
    response = update_book_data(book_id, book_data)
    return response

@router.delete("/{book_id}", response_class=JSONResponse)
async def delete_book(book_id: int):
    response = delete_book_by_id(book_id)
    return response
