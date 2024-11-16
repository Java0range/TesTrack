from fastapi import APIRouter
from pydantic import BaseModel
import db


tests = APIRouter(prefix="/tests", tags=["tests"])