from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views import View
from .models import Book, Library

# ---------------------------
# 1️⃣ Function-Based View
# ---------------------------

def list_books(request):
    """Display a list of all books with their authors."""
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', Book.objects.all(){'books': books})


# ---------------------------
# 2️⃣ Class-Based View
# ---------------------------

class LibraryDetailView(View):
    """Display details of a specific library and its books."""
    template_name = 'library_detail.html'

    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        return render(request, self.relationship_app/library_detail.html", "from .models import Library, {'library': library})
