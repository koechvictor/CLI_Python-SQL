import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Member, Borrow

DATABASE_URL = "sqlite:///./library.db"

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
