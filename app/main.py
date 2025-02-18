from fastapi import FastAPI
from app.api.v1.routes import users

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to WHAM!"}

app.include_router(users.router, prefix="/users", tags=["users"])
