from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(a: str | None = None):
    return {"message": "Hello World"}
