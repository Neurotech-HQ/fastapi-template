"""
The models

The models are the classes that define the structure of the database tables.

The models are defined using the SQLModel class, which is a class that comes from the SQLModel library.

Define the querying logics in particular model
"""

from typing import Optional
from sqlmodel import SQLModel, Field, Session, select

from src.database.connect import Connect
from src.database.enums import IDTypes

engine = Connect.connect()


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    id_type: Optional[IDTypes] = Field(default=None)
    id_number: Optional[str] = Field(default=None)

    def save(self):
        pass

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        pass

    @classmethod
    def by_username(cls, username: str) -> Optional["User"]:
        """
        Gets a user by their username

        Args:
            username (str): The username of the user

        Returns:
            Optional["User"]: The user if found, else None
        """
        with Session(engine) as session:
            statement = select(cls).where(cls.username == username)
            results = session.exec(statement).first()
            return results


def create_tables():
    """
    Create the tables in the database
    """
    SQLModel.metadata.create_all(engine)