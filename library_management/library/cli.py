import click
from library.database import SessionLocal, init_db
from library.models import Book, User, Borrow

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
@click.option('--author_name', prompt="Author's Name", help='The ID of the author.')
def add_book(title, author_name):
    """Add a new book."""
    session = SessionLocal()
    book = Book(title=title, author_name=author_name)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Added book {title} written by {author_name}.')

#@click.command()
#@click.option('--title', prompt='Book title', help='The title of the book.')
#@click.option('--author_id', prompt='Author ID', help='The ID of the author.')
#def add_book(title, author_id):
 #   """Add a new book."""
  #  session = SessionLocal()
   # book = Book(title=title, author_id=author_id)
    #session.add(book)
    #session.commit()
    #session.close()
    #click.echo(f'Added book {title}.')

#@click.command()
#@click.option('--name', prompt='Author name', help='The name of the author.')
#def add_author(name):
 #   """Add a new author."""
  #  session = SessionLocal()
   # author = Author(name=name)
    #session.add(author)
    #session.commit()
    #session.close()
    #click.echo(f'Added author {name}.')

#@click.command()
#@click.option('--book_id', prompt='Book ID', help='The ID of the book.')
#@click.option('--title', prompt='New Book title', help='The new title of the book.')
#def update_book(book_id, title):
 #   """Update a book."""
 #   session = SessionLocal()
  #  book = session.query(Book).filter(Book.id == book_id).first()
   # if book:
    #    book.title = title
     #   session.commit()
      #  click.echo(f'Updated book ID {book_id} to title {title}.')
    #else:
     #   click.echo(f'Book ID {book_id} not found.')
    #session.close()

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
        click.echo(f'Deleted book ID {book_id} Title: {book.title} written by {book.author_name}.')
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
    click.echo(f'Added user {name}.')

cli.add_command(init)
cli.add_command(add_book)
#cli.add_command(add_author)
cli.add_command(update_book)
cli.add_command(report_available_books)
cli.add_command(delete_book)
cli.add_command(add_user)

if __name__ == '__main__':
    cli()
