from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50)
    price: float = Field(...,  title="Price", gt=0, le=100_000)
    description: str = Field(0, title="Description", max_length=1_000)
    tax: float = Field(0, title="Tax", ge=0, le=100)


@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
