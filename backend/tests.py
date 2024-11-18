from fastapi import APIRouter
from pydantic import BaseModel
import db


tests = APIRouter(prefix="/tests", tags=["tests"])


class Test(BaseModel):
    test_id: int


@tests.get("/tests/")
async def get_tests():
    try:
        return {"msg": db.get_tests()}
    except Exception:
        return {"msg": "error"}


@tests.post("/test")
async def get_test(inp: Test):
    try:
        return {"msg": db.get_test(inp.test_id)}
    except Exception:
        return {"msg": "error"}