from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting the server...")
    await init_db()
    yield
    print("shutting down the server...")


version="v1"

app = FastAPI(
    title="Book Management API",
    description="API for managing a collection of books, allowing CRUD operations.",
    version=version,
    lifespan=lifespan
)


app.include_router(book_router,prefix =f"/api/{version}/book")