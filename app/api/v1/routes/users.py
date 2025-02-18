from fastapi import APIRouter

# from app.db.mongo_client import db

router = APIRouter()

# @router.get("/")
# async def get_users():
#     users = db.users.find()
#     return [{"name": user["name"], "email": user["email"]} for user in users]
