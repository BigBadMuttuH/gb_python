from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "from ex05!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
