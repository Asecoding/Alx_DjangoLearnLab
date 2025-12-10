from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.a = User.objects.create_user(username='a', password='pass')
        self.b = User.objects.create_user(username='b', password='pass')
        self.client.login(username='a', password='pass')

    def test_follow_unfollow(self):
        url_follow = f'/api/accounts/follow/{self.b.id}/'
        resp = self.client.post(url_follow)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.b in self.a.following.all())

        url_unfollow = f'/api/accounts/unfollow/{self.b.id}/'
        resp = self.client.post(url_unfollow)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(self.b in self.a.following.all())

