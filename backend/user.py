from fastapi import APIRouter
from pydantic import BaseModel
import db


class User(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str
    admin: bool


user = APIRouter(prefix="/users", tags=["users"])


@user.post("/auth/")
async def auth_user(inp: User):
    ans = db.auth(inp.username, inp.password)
    if ans != "false":
        return {"msg": "true", "admin": ans[0], "id": ans[1]}
    else:
        return {"msg": "false"}


@user.post("/useradd/")
async def create_user(inp: UserCreate):
    try:
        await db.create_user(inp.username, inp.password, admin=inp.admin)
        return {"msg": "true"}
    except Exception:
        return {"msg": "error"}
