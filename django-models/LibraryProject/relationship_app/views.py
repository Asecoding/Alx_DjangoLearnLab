from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library

# ---------------------------
# 1️⃣ Function-Based View
# ---------------------------

def list_books(request):
    """Display a list of all books with their authors."""
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})


# ---------------------------
# 2️⃣ Class-Based View
# ---------------------------

class LibraryDetailView(View):
    """Display details of a specific library and its books."""
    template_name = 'library_detail.html'

    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        return render(request, self.template_name, {'library': library})
