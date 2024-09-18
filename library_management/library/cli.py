import click
from library.database import SessionLocal, init_db
from library.models import Author, Book, User, Borrow

@click.group()
def cli():
    pass

@click.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Initialized the database.")

@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author_id', prompt='Author ID', help='The ID of the author.')
def add_book(title, author_id):
    """Add a new book."""
    session = SessionLocal()
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Added book {title}.')

@click.command()
@click.option('--name', prompt='Author name', help='The name of the author.')
def add_author(name):
    """Add a new author."""
    session = SessionLocal()
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.close()
    click.echo(f'Added author {name}.')

@click.command()
@click.option('--book_id', prompt='Book ID', help='The ID of the book to update.')
@click.option('--title', prompt='New title', help='The new title of the book.')
@click.option('--author', prompt='New author', help='The new author of the book.')
def update_book(book_id, title, author):
    """Update a book."""
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = title
        book.author = author
        db.commit()
        db.refresh(book)
        click.echo(f"Book ID {book_id} updated to '{title}' by {author}.")
    else:
        click.echo(f"Book ID {book_id} not found.")
    db.close()

@click.command()
def report_available_books():
    """Generate report of available books."""
    session = SessionLocal()
    available_books = session.query(Book).filter(Book.is_borrowed == False).all()
    if available_books:
        click.echo("Available Books:")
        for book in available_books:
            click.echo(f'ID: {book.id}, Title: {book.title},Author: {book.author.name}')
    else:
        click.echo("No books are currently available.")
    session.close()

cli.add_command(init)
cli.add_command(add_book)
cli.add_command(add_author)
cli.add_command(update_book)
cli.add_command(report_available_books)

if __name__ == '__main__':
    cli()
