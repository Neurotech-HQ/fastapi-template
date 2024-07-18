"""
This is the main entry point of the application

"""

from src.main.app import app 

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
