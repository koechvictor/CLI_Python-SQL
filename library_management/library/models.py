from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

#class Author(Base):
 #   __tablename__ = 'authors'
  #  id = Column(Integer, primary_key=True)
   # name = Column(String, nullable=False)
    #books = relationship('Book', back_populates='author')

#class Book(Base):
 #   __tablename__ = 'books'
  #  id = Column(Integer, primary_key=True)
   # title = Column(String, nullable=False)
    #author_id = Column(Integer, ForeignKey('authors.id'))
    #author = relationship('Author', back_populates='books')
    #is_borrowed = Column(Boolean, default=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_name = Column(String, nullable=False)
    is_borrowed = Column(Boolean, default=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    borrowed_books = relationship('Borrow', back_populates='user')

class Borrow(Base):
    __tablename__ = 'borrows'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    book = relationship('Book')
    user = relationship('User', back_populates='borrowed_books')
