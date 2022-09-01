# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
