import logging
from fastapi import FastAPI
from .Item import Item

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info('Отработал запрос GET на "/".')
    return {"Hello": "from ex03!"}


@app.post("/items/")
async def create_item(item: Item):
    logger.info(f'Отработал запрос POST на "/items/{item}".')
    return f'{item} was created.'


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал запрос PUT на "/items/{item_id}".')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Отработал запрос DELETE на "/items/{item_id}".')
    return {"item_id": item_id}
