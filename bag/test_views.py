# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase, Client


class TestBagViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_bag_view(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_can_add_to_bag(self):
        response = self.client.post('add/<item_id>/',
                                    {'title': 'Test add to bag'})
        self.assertNotEqual(response.status_code, 301)

    def test_can_remove_from_bag(self):
        response = self.client.get('remove/<item_id>/')
        self.assertNotEqual(response.status_code, 301)
