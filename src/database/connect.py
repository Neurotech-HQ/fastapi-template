"""
Database connection logic goes here

- Connect to the database

Keep the database URL in the .env file

"""

import os

from sqlmodel import create_engine
from sqlalchemy.engine import Engine


class Connect:
    """
    This hadles the connection to the database

    Define your connection logic here
    """

    def get_database_url(self) -> str:
        """
        Get database url depending on environment set up:

        Make sure you have set up your variables in .env

        This assumes you have set up your database URL in the .env file
        """

        if os.getenv("DEVELOPMENT_MODE", "false").lower() == "true":
            if url := os.getenv("DEV_DATABASE_URL"):
                database_url = url
            else:
                sqlite_file_name = "database.db"
                database_url = f"sqlite:///{sqlite_file_name}"
        else:
            database_url = os.getenv("PROD_DATABASE_URL", "")
            if not database_url:
                raise Exception(
                    "DATABASE_URL not set in environment variables. You're using production mode without a database URL"
                )

        return database_url

    def connect(self) -> Engine:
        """
        Connect to the database.

        This is the main function that should be called to connect to the database
        """
        database_url = Connect.get_database_url()
        # Engine accepts more parameters like pool_size, max_overflow, pool_recycle, etc.
        engine = create_engine(database_url)
        return engine
