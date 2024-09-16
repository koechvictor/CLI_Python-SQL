import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Member, Borrow

DATABASE_URL = "sqlite:///site.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.group()
def cli():
    pass

@click.command()
def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)
    click.echo("Database initialized.")

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

cli.add_command(init_db)
cli.add_command(update_book)

if __name__ == '__main__':
    cli()
