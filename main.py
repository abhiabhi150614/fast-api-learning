from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]

app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = 0
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language:str

class PostBook(BaseModel):
    id: Optional[int] = 0
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language:str

class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str

@app.get("/")
def home():
    return {"message":"Happy Home"}


@app.get("/books",response_model = List[Book],status_code = 200)
def get_all_books():
    return books

@app.post("/books",response_model = Book,status_code = 200)
def post_the_book(book_data:PostBook):
    l = len(books) + 1
    book_data.id = l
    books.append(book_data)
    
    return book_data


@app.get("/books/{id}",response_model = Book)
def get_particular_book(id : int):
    for book in books:
        if(book["id"] == id):
            return book
    raise HTTPException(status_code=404,detail="Book not found")

@app.patch("/books",response_model = Book)
def update_the_book(bookdata:UpdateBook,id : int):
    for book in books:
        if(book["id"] == id):
            book['title'] = bookdata.title
            book['author'] = bookdata.author
            book['publisher'] = bookdata.publisher
            return book
    raise HTTPException(status_code=404,detail="Book not found")
    
@app.delete("/books",response_model = Book)
def delete_the_book(id : int):
    for book in books:
        if(book["id"] == id):
            books.remove(book)
            return book
    raise HTTPException(status_code=404,detail="Book not found")
        