from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from fastapi import *
import uvicorn
from typing import Optional

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class BookCreate(BaseModel):
    title: str
    author: str 
    genre: Optional[str] = ""
    status: Optional[str] = "В планах"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        status=book.status,
    )

    db.add(db_book)
    dp.commit()
    db.refresh(db_book)
    return db_book
   


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)