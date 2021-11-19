from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
