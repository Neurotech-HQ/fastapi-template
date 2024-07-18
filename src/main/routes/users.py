from fastapi import APIRouter


users_router = APIRouter()


@users_router.get("/users/me")
async def read_users_me():
    return {"users": "me"}
