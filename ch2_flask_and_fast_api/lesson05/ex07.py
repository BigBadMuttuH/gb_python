from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "from ex07!"}


@app.get("/items/")
async def skip_limit(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
# http://127.0.0.1:8000/items/?limit=25
# http://127.0.0.1:8000/items/?limit=10&skip=20
