# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase


class TestWishlistViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_wishlist_page(self):
        response = self.client.get('wishlist/')
        self.assertEqual(response.status_code, 404)

    def test_can_add_to_bag(self):
        response = self.client.post('add/<item_id>/',
                                    {'title': 'Test add to bag'})
        self.assertNotEqual(response.status_code, 301)

    def test_can_delete_from_wishlist(self):
        response = self.client.get('delete_from_wishlist/')
        self.assertEqual(response.status_code, 404)
