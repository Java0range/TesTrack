from fastapi import APIRouter
from pydantic import BaseModel
import db


class CreateTest(BaseModel):
    name: str
    imgUrls: list
    otv: list


admin = APIRouter(prefix="/admin", tags=["admin"])


@admin.post("/createtest/")
async def create_test(inp: CreateTest):
    try:
        if db.create_test(inp.name, inp.imgUrls, inp.otv) == "true":
            return "true"
        return "error"
    except Exception:
        return "error"