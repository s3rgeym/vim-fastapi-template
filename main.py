from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def index():
    return "Index Page."


@app.get("/hello/{name}")
async def read_item(name: str = "world"):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    import uvicorn

    # Для hot reload в качестве app нужно указать строку для импорта
    uvicorn.run("main:app", reload=True)
