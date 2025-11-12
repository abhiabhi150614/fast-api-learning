

from pydantic import BaseModel
from typing import Optional
class Book(BaseModel):
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