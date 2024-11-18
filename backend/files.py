import random
import shutil
import os
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel


files = APIRouter(prefix="/files", tags=["files"])


def create_signature():
    lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return "".join(random.choices(lst, k=20))


class TestId(BaseModel):
    test_id: int


@files.post("/upload")
async def upload_file(upload_file: UploadFile = File(...)):
    while True:
        signature = create_signature()
        if not os.path.exists(f"/img/{signature}.{upload_file.filename.split('.')[1]}"):
            break
    upload_file.filename = f"{signature}.{upload_file.filename.split('.')[1]}"
    path = f"img/{upload_file.filename}"
    with open(path, "wb+") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {"msg": upload_file.filename}


@files.get("/download/{file_name}", response_class=FileResponse)
async def download_file(file_name: str):
    path = f"img/{file_name}"
    return path