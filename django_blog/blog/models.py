
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model represents each blog article.
    - title: title of the blog post
    - content: full blog text content
    - published_date: automatically records date/time when created
    - author: foreign key referencing Django's built-in User model
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

