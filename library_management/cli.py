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

cli.add_command(init_db)

if __name__ == '__main__':
    cli()
