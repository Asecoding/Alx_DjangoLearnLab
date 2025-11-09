from bookshelf.models import Book

# Retrieve and update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
