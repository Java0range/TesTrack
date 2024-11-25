from fastapi import APIRouter
from pydantic import BaseModel
import db


tests = APIRouter(prefix="/tests", tags=["tests"])


class Test(BaseModel):
    test_id: int


class CreateRez(BaseModel):
    test_id: int
    user_id: int
    rez: list


@tests.get("/tests/")
async def get_tests():
    try:
        return {"msg": db.get_tests()}
    except Exception:
        return {"msg": "error"}


@tests.post("/test")
async def get_test(inp: Test):
    try:
        ans = db.get_test(inp.test_id)
        return {"msg": ans[0], "otv": ans[1]}
    except Exception:
        return {"msg": "error"}


@tests.post("/saverez/")
async def save_rez(inp: CreateRez):
    try:
        db.create_rez(inp.test_id, inp.user_id, inp.rez)
        return {"msg": "true"}
    except Exception:
        return {"msg": "error"}


@tests.post("/reztest/")
async def get_rez_from_test(inp: Test):
    try:
        ans = db.get_rez_for_test(inp.test_id)
        return {"msg": ans}
    except Exception:
        return {"msg": "error"}