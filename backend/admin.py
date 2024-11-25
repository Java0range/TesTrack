from fastapi import APIRouter
from pydantic import BaseModel
import db


class CreateTest(BaseModel):
    name: str
    imgUrls: list
    otv: list


class DeleteTest(BaseModel):
    test_id: int


class DeleteUser(BaseModel):
    user_id: int


admin = APIRouter(prefix="/admin", tags=["admin"])


@admin.post("/createtest/")
async def create_test(inp: CreateTest):
    try:
        if db.create_test(inp.name, inp.imgUrls, inp.otv) == "true":
            return "true"
        return "error"
    except Exception:
        return "error"


@admin.delete("/deletetest/")
async def delete_test(inp: DeleteTest):
    try:
        db.delete_test(inp.test_id)
        return {"msg": "true"}
    except Exception:
        return {"msg": "error"}


@admin.delete("/deleteuser/")
async def delete_user(inp: DeleteUser):
    try:
        db.delete_user(inp.user_id)
        return {"msg": "true"}
    except Exception:
        return {"msg": "error"}