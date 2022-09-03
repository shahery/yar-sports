# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product


class TestProductsModel(TestCase):

    def test_checkout(self):
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com'
        )
        test_user.save()

    def test_products_detail(self):
        product = Product.objects.create(
            name='test',
            description='test description',
            price='90.99',
            rating='4.9',
            image='test'
            )
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), 'test')
