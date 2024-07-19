from fastapi import FastAPI
from sqlmodel import SQLModel
from src.main.routes import books
from src.database.connect import engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(books.router, prefix="/api/books")
