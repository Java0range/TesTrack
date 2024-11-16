from fastapi import APIRouter
from pydantic import BaseModel
import db


admin = APIRouter(prefix="/admin", tags=["admin"])