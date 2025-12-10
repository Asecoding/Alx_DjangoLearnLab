from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extends Django's AbstractUser.
    - bio: short biography
    - profile_picture: optional user avatar
    - followers: many-to-many self relationship (people who follow this user)
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # followers = users that follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',  # user.following gives users this user follows
        blank=True
    )
     # Users this user follows (asymmetric relationship)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

