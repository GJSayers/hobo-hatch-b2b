from django.db import models
from django.contrib.auth.models import User

from multiselectfield import MultiSelectField
from django_countries.fields import CountryField


class Stockist(models.Model):
    """
    A stockist model for creating a stockist account for placing orders:
    Without an account customers cannot place orders
    """
    stockist = models.OneToOneField(User, on_delete=models.CASCADE)
    stockist_name = models.CharField(max_length=60, null=False, blank=False)
    buyer_name = models.CharField(max_length=60, null=False, blank=False)
    buyer_phone = models.CharField(max_length=20, null=False, blank=False)
    buyer_email = models.EmailField(max_length=200, null=False, blank=False)
    accounts_phone = models.CharField(max_length=20, null=False, blank=False)
    accounts_email = models.EmailField(max_length=200, null=False, blank=False)
    address_1 = models.CharField(max_length=80, null=False, blank=False)
    address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=35, null=False, blank=False)
    county_or_state = models.CharField(max_length=35, null=False, blank=False)
    postcode = models.CharField(max_length=12, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=True, blank=True)

    CURRENCY_OPTIONS = (
        (1, "GBP"),
        (2, "EUR"),
    )
    purchasing_currency = models.CharField(max_length=30,
                                           choices=CURRENCY_OPTIONS)

    CHANNEL_OPTIONS = (
        (1, "Pureplay Ecomm"),
        (2, "Physical Only"),
        (3, "Multi-Channel"),
        (4, "Marketplace"),
    )

    stockist_channel = models.CharField(max_length=30,
                                        choices=CHANNEL_OPTIONS)

    MARKET_OPTIONS = (
        (1, "Women"),
        (2, "Home"),
        (3, "Jewellery"),
        (4, "Accessories"),
        (5, "Clothing"),
        (6, "Gifting"),
    )
    stockist_market = MultiSelectField(max_length=30,
                                       choices=MARKET_OPTIONS)
    website_url = models.URLField(max_length=200, null=True, blank=True)

    PURCHASING_CATEGORIES = (
        ('jewellery', 'Jewellery'),
        ('leather_accessories', 'Leather Accessories'),
        ('blankets', 'Blankets'),
        ('knitted_accessories', 'Knitted Accessories'),
        ('clothing', 'Clothing'),
        )

    categories = MultiSelectField(max_length=30,
                                  choices=PURCHASING_CATEGORIES)


def __str__(self):
    return self.stockist_name
