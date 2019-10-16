from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        test_user1 = User.objects.create_user(username='testuser1', password='abc123')
        test_user1.save()
        # create a post
        test_post1 = Post.objects.create(author=test_user1, title='Test Title', body='Test Body')
        test_post1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Test Title')
        self.assertEqual(expected_body, 'Test Body')
