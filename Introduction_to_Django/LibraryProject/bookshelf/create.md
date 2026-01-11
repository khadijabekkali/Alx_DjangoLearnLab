# Create Operation

This file documents the creation of a `Book` instance in the Django shell.

```python
# Import the Book model from the bookshelf app
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Check the created book
book  # Expected output: <Book: 1984>

# Explanation:
# Book.objects.create(...) creates and saves a new book in the database.
# The variable 'book' now references the created Book object.
