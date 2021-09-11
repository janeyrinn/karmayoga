"""IMPORTS"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    """import tell django to listen to the signals module"""

    def ready(self):
        import checkout.signals
