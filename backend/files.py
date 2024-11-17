from fastapi import APIRouter
from pydantic import BaseModel


files = APIRouter(prefix="/files", tags=["files"])