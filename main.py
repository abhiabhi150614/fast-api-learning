from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {"message" : "home page"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message" : f"welcome {name}"}