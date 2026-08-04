# Импорт
from sqlalchemy import Column, Integer, String
from database import Base

# Создание модели Book для БД

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    genre = Column(String, default="")
    status = Column(String, default="В планах")
