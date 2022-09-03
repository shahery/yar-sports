# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=[1])
        self.add_product = reverse('add_product')
        self.edit_product = reverse('edit_product', args=[1])
        self.delete_product = reverse('delete_product', args=[1])

        self.product_example = Product.objects.create(
            name='test',
            description='test description',
            price='99.99',
            rating='9.9',
            image='test'
        )

        self.client = Client()
        self.user = User.objects.create_superuser(
            'super',
            'super@test.com',
            'superpassword')

    def test_view_all_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_url(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_url(self):
        self.client.login(username='super', password='superpassword')
        response = self.client.get(self.add_product)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_url(self):
        self.client.login(username='super', password='superpassword')
        response = self.client.get(self.edit_product)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
