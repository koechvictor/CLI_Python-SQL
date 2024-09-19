``# Library Management System

A command-line interface (CLI) based library management system built with Python and SQLAlchemy. This system allows you to manage books, authors, and users, as well as record borrowing and returning of books and generate reports.

## Features

- Add, update, and delete books.
- Register and manage library members.
- Record borrowing and returning of books.
- Generate reports of borrowed and available books.

## Project Structure

library_management/
├── library/
│ ├── models.py
│ ├── database.py
│ └── cli.py
└── README.md

## Installation

1. Clone the repository:

```sh
 git clone https://github.com/koechvictor/CLI_Python-SQL
cd library_management/library
```

2. Install pipenv

```sh
pip install pipenv
```

3. Create a virtual environment and activate it:

```sh
pipenv shell
```

## Usage

1. While in the library_management directory:

### Initialize the Database

```sh
python -m library.cli init
```

### Add a Book

```sh
python -m library.cli add-book
```

### Update a Book

```sh
python -m library.cli update-book
```

### Delete a Book

```sh
python -m library.cli delete-book
```

### Add a User

```sh
python -m library.cli add-user
```

### Update a User

```sh
python -m library.cli update-user
```

### Delete a User

```sh
python -m library.cli delete-user
```

### Borrow a Book

```sh
python -m library.cli borrow-book
```

### Return a Book

```sh
python -m library.cli return-book
```

### List Borrowed Books

```sh
python -m library.cli list_of_borrowed_books
```

### List Available Books

```sh
python -m library.cli report_available_books
```
