import databases
import sqlalchemy
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


# валидация данных
# from fastapi import Path
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item", ge=1), q: str = None):
    return {"item_id": item_id, "q": q}
