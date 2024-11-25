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


class UserRez(BaseModel):
    user_id: int


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


@user.get("/users/")
async def get_users():
    try:
        ans = db.get_users()
        return {"msg": ans}
    except Exception:
        return {"msg": "error"}


@user.post("/userrez/")
async def get_user_rez(inp: UserRez):
    try:
        ans = db.get_user_rez(inp.user_id)
        return {"msg": ans}
    except Exception:
        return {"msg": "error"}