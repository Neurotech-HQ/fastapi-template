from fastapi import FastAPI


from src.main.routes import users
# Load env here if needed using config if defined
app = FastAPI()

app.include_router(users.users_router)


# General middleware for the application