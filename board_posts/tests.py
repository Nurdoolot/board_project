from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is only test')

    def test_post_content(self):
        post = Post.objects.get(pk=1)
        object_name = f'{post.text}'
        self.assertEqual(object_name, 'This is only test')


class IndexPageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='ass')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')