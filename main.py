from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
async def main():
    return {"message" : "home page"}


@app.get("/greet")
async def greet(name: Optional[str] = "user",age : Optional[int] = 0) -> dict:
    return {"message" : f"welcome {name} your age is {age}"}


class BookCreate(BaseModel):
    title : str
    author: str


dic = {}
id = 0
@app.post('/create-book')
async def createbook(book_data : BookCreate) -> dict:
    global id
    dic[id] = book_data
    id = id + 1
    return {
        "title":book_data.title,
        "author":book_data.author
    }

@app.get("/books")
async def getbooks(id : int):
    return dic[id]