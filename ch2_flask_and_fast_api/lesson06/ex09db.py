import databases
import sqlalchemy
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///instance/lesson06.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# users - это название таблицы
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
metadata.create_all(engine)

app = FastAPI()


# это модель данных для входа
class UserIn(BaseModel):
    """ Модель данных для входа """
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    """ Модель данных для вывода """
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# CRUD
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    """ Создание пользователя """
    # обращение к таблице users с явным указанием данных
    query = users.insert().values(name=user.name, email=user.email)
    # обращение к таблице users через распаковку данных из словаря
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**user.dict())
    await database.execute(query)
    return {**user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# валидация данных
# from fastapi import Path
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1)):
    return {"item_id": item_id}
