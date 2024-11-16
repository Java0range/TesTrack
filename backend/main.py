import uvicorn
from fastapi import FastAPI
from user import user
from tests import tests
from admin import admin


app = FastAPI()
app.include_router(user)
app.include_router(tests)
app.include_router(admin)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)