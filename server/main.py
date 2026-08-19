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

class BookRespone(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    status: str

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
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=list[BookRespone])
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

@app.get("/books/{book_id}", response_model=BookRespone)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book). filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found, sorry :)")
    
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book). filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found, sorry :)")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book). filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found, sorry :)")

    update_data = book.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

   


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)