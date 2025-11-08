from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name}:")
    for book in books:
        print(f"- {book.title}")


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # OneToOne relationship
    print(f"Librarian for {library.name}: {librarian.name}")


# Example calls (optional for testing)
if __name__ == "__main__":
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
