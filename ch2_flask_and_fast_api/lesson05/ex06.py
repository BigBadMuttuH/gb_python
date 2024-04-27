from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "from ex06!"}


# http://127.0.0.1:8000/user/1/order/1
@app.get("/user/{user_id}/order/{order_id}")
async def read_data(user_id: int, order_id: int):
    return {"user_id": user_id, "order_id": order_id}
