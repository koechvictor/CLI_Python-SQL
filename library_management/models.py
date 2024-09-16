from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Book:
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)

class Member:
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Borrow:
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    member = relationship("Member")
    book = relationship("Book")
