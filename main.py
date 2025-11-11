from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get('/')
async def main():
    return {"message" : "home page"}


@app.get("/greet")
async def greet(name: Optional[str] = "user",age : Optional[int] = 0) -> dict:
    return {"message" : f"welcome {name} your age is {age}"}