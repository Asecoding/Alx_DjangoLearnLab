from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation (Run once if needed) ---
# Uncomment these lines if you want to populate data for testing
# author1 = Author.objects.create(name="George Orwell")
# book1 = Book.objects.create(title="1984", author=author1)
# book2 = Book.objects.create(title="Animal Farm", author=author1)
# library1 = Library.objects.create(name="Central Library")
# library1.books.add(book1, book2)
# librarian1 = Librarian.objects.create(name="John Doe", library=library1)

# --- Queries ---

# 1️⃣ Query all books by a specific author
author_name = "George Orwell"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")
Book.objects.filter(author__name="George Orwell")

# 2️⃣ List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(f"- {book.title}")
Library.objects.get(name="Central Library").books.all()

# 3️⃣ Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian of {library_name}: {librarian.name}")
Librarian.objects.get(library="Central Library").librarian
Author.objects.get(name=author_name) objects.filter(author=author)

