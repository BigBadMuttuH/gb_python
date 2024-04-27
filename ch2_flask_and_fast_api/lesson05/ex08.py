from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <html>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/message/")
async def get_message():
    message = {"message": "Hello, World!"}
    return JSONResponse(content=message, status_code=200)
