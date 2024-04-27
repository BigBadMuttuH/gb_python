# install FastAPI
# pip install fastapi
# ставим асинхронный сервер
# pip install "uvicorn[standard]"
# запускать нужно вот так
# uvicorn lesson05.ex01:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
