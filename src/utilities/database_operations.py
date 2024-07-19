# src/utilities/database_operations.py

from fastapi.responses import JSONResponse
from src.database.models import Book

def get_book_by_id(book_id: int):
    try:
        return Book.get_by_id(book_id)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error retrieving book: {str(e)}"})

def add_book(book_data):
    try:
        return Book.create(book_data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error adding book: {str(e)}"})

def get_all_books():
    try:
        return Book.get_all()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error retrieving all books: {str(e)}"})

def update_book_data(book_id: int, book_data):
    try:
        return Book.update(book_id, book_data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error updating book: {str(e)}"})

def delete_book_by_id(book_id: int):
    try:
        return Book.delete(book_id)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error deleting book: {str(e)}"})
