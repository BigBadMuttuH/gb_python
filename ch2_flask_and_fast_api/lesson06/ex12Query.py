from fastapi import FastAPI, Query

app = FastAPI()


# валидация данных
@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
