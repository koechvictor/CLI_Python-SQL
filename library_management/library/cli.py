import click
from datetime import datetime
from library.database import SessionLocal, init_db
from library.models import Book, User, Borrow

@click.group()
def cli():
    pass

@click.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("database Initialized successfully")

@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author_name', prompt="Author's Name", help='The ID of the author.')
def add_book(title, author_name):
    """Add a new book."""
    session = SessionLocal()
    book = Book(title=title, author_name=author_name)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Book {title} written by {author_name} added successfully')

@click.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book.')
@click.option('--title', prompt='New Book title', help='The new title of the book.')
@click.option('--author_name', prompt="New Author's Name", help='The Name of the author.')
def update_book(book_id, title, author_name):
    """Update a book."""
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = title
        book.author_name = author_name
        session.commit()
        click.echo(f'Updated book ID {book_id} to title {title}. and author {author_name}.')
    else:
        click.echo(f'Book ID {book_id} not found.')
    session.close()

@click.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book.')
def delete_book(book_id):
    """Delete a book."""
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        click.echo(f'Book ID {book_id} Title: {book.title} written by {book.author_name} deleted successfully')
    else:
        click.echo(f'Book ID {book_id} not found.')
    session.close()

@click.command()
def report_available_books():
    """Generate report of available books."""
    session = SessionLocal()
    available_books = session.query(Book).filter(Book.is_borrowed == False).all()
    if available_books:
        click.echo("Available Books:")
        for book in available_books:
            click.echo(f'ID: {book.id}, Title: {book.title},Author: {book.author_name}')
    else:
        click.echo("No books are currently available.")
    session.close()

@click.command()
@click.option('--name', prompt='User name', help='The name of the user.')
def add_user(name):
    """Add a new user."""
    session = SessionLocal()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f'User {name} added successfully')

@click.command()
@click.option('--user_id', prompt='User ID', help='The ID of the user.')
@click.option('--name', prompt='New User name', help='The new name of the user.')
def update_user(user_id, name):
    """Update a user."""
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        session.commit()
        click.echo(f'Updated user ID {user_id} to name {name}.')
    else:
        click.echo(f'User ID {user_id} not found.')
    session.close()

@click.command()
@click.option('--user_id', prompt='User ID', help='The ID of the user.')
def delete_user(user_id):
    """Delete a user."""
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        click.echo(f'User ID {user_id}, Name:{user.name} deleted successfully')
    else:
        click.echo(f'User ID {user_id} not found.')
    session.close()

@click.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book.')
@click.option('--user_id', prompt='User ID', help='The ID of the user.')
def borrow_book(book_id, user_id):
    """Borrow a book."""
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()
    user = session.query(User).filter(User.id == user_id).first()
    if book and user and not book.is_borrowed:
        borrow = Borrow(book_id=book_id, user_id=user_id )
        book.is_borrowed = True
        session.add(borrow)
        session.commit()
        click.echo(f'Book ID {book_id}, Title: {book.title} borrowing by User Id {user_id} Name: {user.name} was successfull')
    else:
        click.echo(f'Book ID: {book_id}, Title: {book.title} borrowing was unsuccessfull, book may have been borrowed or does not exist')
    session.close()

@click.command()
def list_of_borrowed_books():
    """Generate report of borrowed books."""
    session = SessionLocal()
    borrowed_books = session.query(Book).filter(Book.is_borrowed == True).all()
    if borrowed_books:
        click.echo("Borrowed Books:")
        for book in borrowed_books:
            click.echo(f'ID: {book.id}, Title: {book.title}')
    else:
        click.echo("No books are currently borrowed.")
    session.close()

@click.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book.')
def return_book(book_id):
    """Borrow a book"""
    session = SessionLocal()
    borrow = session.query(Borrow).filter(Borrow.book_id == book_id, Borrow.return_date == None).first()
    if borrow:
        borrow.return_date = datetime.utcnow()
        book = session.query(Book).filter(Book.id == book_id).first()
        book.is_borrowed = False
        session.commit()
        click.echo(f'Returned book ID {book_id}: Title:{book.title}')
    else:
        click.echo(f'Book {book_id} not found or not borrowed.')
    session.close()

cli.add_command(init)
cli.add_command(add_book)
cli.add_command(update_book)
cli.add_command(report_available_books)
cli.add_command(delete_book)
cli.add_command(add_user)
cli.add_command(update_user)
cli.add_command(delete_user)
cli.add_command(borrow_book)
cli.add_command(list_of_borrowed_books)
cli.add_command(return_book)

if __name__ == '__main__':
    cli()
