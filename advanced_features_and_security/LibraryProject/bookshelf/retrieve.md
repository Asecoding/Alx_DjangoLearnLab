from bookshelf.models import Book

# Retrieve the created book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
