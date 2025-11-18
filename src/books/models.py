from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import uuid
class Book(SQLModel, table=True):
    uid: uuid.UUID = Field(
        sa_column= Column(
            primary_key=True,
            default=uuid.uuid4(),
            index=True,
            nullable=False
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language:str
    created_at: date_time
    updated_at: date_time



class User(SQLModel, table=True):
    uid: uuid.UUID = Field(
        sa_column= Column(
            primary_key=True,
            default=uuid.uuid4(),
            index=True,
            nullable=False
        )
    )
    username: str
    email: str
    password: str
    created_at: date_time
    updated_at: date_time