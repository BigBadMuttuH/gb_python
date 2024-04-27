# pip install sqlalchemy
# pip install databases[aiosqlite]
import databases
import sqlalchemy
from fastapi import FastAPI

# CRUD - Create, Read, Update, Delete это основные операции с базами данных
DATABASE_URL = "sqlite:///instance/lesson06.db"
# DATABASE_URL = "postgresql://user:password@localhost/postgres"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

... # тут будет еще код


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
