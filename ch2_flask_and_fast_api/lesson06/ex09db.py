import databases
import sqlalchemy
from fastapi import FastAPI
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


# используем только для фейковых данных
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f"user{i}", email=f"user{i}@example.com")
#         await database.execute(query)
#     return {'message': f'Created {count} fake users'}

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
