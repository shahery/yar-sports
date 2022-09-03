# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'test',
            'test@test.com',
            'testpassword')

    def test_checkout_url_empty_bag(self):
        self.client.login(username='test', password='testpassword')
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
