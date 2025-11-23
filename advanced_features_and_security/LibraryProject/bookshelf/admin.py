from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    search_fields = ('title', 'author')                     # search bar fields
    list_filter = ('publication_year',)                     # filter sidebar

    # Optional: order results by publication year
    ordering = ('publication_year',)
