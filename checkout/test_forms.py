# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_fullname_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_oder_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_order_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_order_streetaddress1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_streetaddress2_is_not_required(self):
        form = OrderForm({'street_address2': 'test street_address2'})
        self.assertFalse(form.is_valid())

    def test_order_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_postcode_is_not_required(self):
        form = OrderForm({'postcode': 'test postcode'})
        self.assertFalse(form.is_valid())

    def test_order_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0],
                         'This field is required.')

    def test_county_is_not_required(self):
        form = OrderForm({'county': 'test county'})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertNotEqual(form.Meta.fields, ['full_name', 'email',
                            'phone_number', 'street_address1',
                                               'street_address2',
                                               'town_or_city',
                                               'postcode', 'country',
                                               'county', ])
