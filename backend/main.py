import uvicorn
from fastapi import FastAPI
from user import user
from tests import tests
from admin import admin
from files import files


app = FastAPI()
app.include_router(user)
app.include_router(tests)
app.include_router(admin)
app.include_router(files)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)