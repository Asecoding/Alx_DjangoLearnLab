from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model: represents a book author
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model: represents a book with a relationship to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # allows author.books to access related books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    # Custom validation to ensure publication_year is not in the future
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")

