from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List,Optional
from .book_model import books
from .schemas import Book,UpdateBook


book_router = APIRouter()



@book_router.get("/")
def home():
    return {"message":"Happy Home"}


@book_router.get("/books",response_model = List[Book],status_code = 200)
def get_all_books():
    return books

@book_router.post("/books",response_model = Book,status_code = 200)
def post_the_book(book_data:Book):
    l = len(books) + 1
    book_data.id = l
    books.append(book_data)
    
    return book_data


@book_router.get("/books/{id}",response_model = Book)
def get_particular_book(id : int):
    for book in books:
        if(book["id"] == id):
            return book
    raise HTTPException(status_code=404,detail="Book not found")

@book_router.patch("/books",response_model = Book)
def update_the_book(bookdata:UpdateBook,id : int):
    for book in books:
        if(book["id"] == id):
            book['title'] = bookdata.title
            book['author'] = bookdata.author
            book['publisher'] = bookdata.publisher
            return book
    raise HTTPException(status_code=404,detail="Book not found")
    
@book_router.delete("/books",response_model = Book)
def delete_the_book(id : int):
    for book in books:
        if(book["id"] == id):
            books.remove(book)
            return book
    raise HTTPException(status_code=404,detail="Book not found")
        