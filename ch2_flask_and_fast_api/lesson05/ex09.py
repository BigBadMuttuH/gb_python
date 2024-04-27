from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello form ex09."}


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse('index.html', {"request": request, "name": name})


# Интерактивная документация
# Swagger: http://127.0.0.1:8000/docs
# Redoc: http://127.0.0.1:8000/redoc
