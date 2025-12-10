from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostCommentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.other = User.objects.create_user(username='other', password='pass1234')
        self.client.login(username='tester', password='pass1234')  # or use token auth

    def test_create_post(self):
        url = '/api/posts/'
        data = {'title': 'Test', 'content': 'Body'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().author, self.user)

    def test_only_owner_can_delete_post(self):
        post = Post.objects.create(author=self.other, title='X', content='Y')
        url = f'/api/posts/{post.id}/'
        # logged in as tester should not be able to delete other's post
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

    def test_create_comment(self):
        post = Post.objects.create(author=self.other, title='X', content='Y')
        url = '/api/comments/'
        data = {'post': post.id, 'content': 'Good one'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().author, self.user)
class FeedTests(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pass')
        self.u2 = User.objects.create_user(username='u2', password='pass')
        # u1 follows u2
        self.u1.following.add(self.u2)
        Post.objects.create(author=self.u2, title='X', content='Y')
        self.client.login(username='u1', password='pass')

    def test_feed_contains_followed_posts(self):
        resp = self.client.get('/api/posts/feed/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)  # paginated results
