from bookshelf.models import Book

# Retrieve and delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
