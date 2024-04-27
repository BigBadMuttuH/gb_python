import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "sqlite:///instance/lesson06.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL,
    # connect_args - это дополнительные параметры подключения к базе данных
    # например, check_same_thread=False - это необходимо, если вы используете SQLite
    # и хотите использовать SQLite в многопоточном режиме
    # https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine
    connect_args={"check_same_thread": False},
)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
