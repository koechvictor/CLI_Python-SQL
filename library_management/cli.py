import click
from .database import SessionLocal, init_db
from .models import Base, Book, Member, Borrow

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

cli.add_command(init)
cli.add_command(add_book)
cli.add_command(add_author)
cli.add_command(update_book)

if __name__ == '__main__':
    cli()
