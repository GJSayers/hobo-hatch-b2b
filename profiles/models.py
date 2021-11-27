from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A stockist model for creating a stockist account for placing orders:
    Without an account customers cannot place orders
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stockist = models.CharField(max_length=60, null=True, blank=True)
    buyer_name = models.CharField(max_length=60, null=True, blank=True)
    buyer_phone = models.CharField(max_length=20, null=True, blank=True)
    buyer_email = models.EmailField(max_length=200, null=True, blank=True)
    accounts_phone = models.CharField(max_length=20, null=True, blank=True)
    accounts_email = models.EmailField(max_length=200, null=True, blank=True)
    address_1 = models.CharField(max_length=80, null=True, blank=True)
    address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=35, null=True, blank=True)
    county_or_state = models.CharField(max_length=35, null=True, blank=True)
    postcode = models.CharField(max_length=12, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)

    CURRENCY_OPTIONS = (
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
    )
    purchasing_currency = models.CharField(max_length=30,
                                           choices=CURRENCY_OPTIONS)

    CHANNEL_OPTIONS = (
        ('Pureplay Ecomm', 'Pureplay Ecomm'),
        ('Physical Only', 'Physical Only'),
        ('Multi-Channel', 'Multi-Channel'),
        ('Marketplace', 'Marketplace'),
    )

    stockist_channel = models.CharField(max_length=100,
                                        choices=CHANNEL_OPTIONS)

    MARKET_OPTIONS = (
        ('Women', 'Women'),
        ('Home', 'Home'),
        ('Jewellery', 'Jewellery'),
        ('Accessories', 'Accessories'),
        ('Clothing', 'Clothing'),
        ('Gifting', 'Gifting'),
    )
    
    stockist_market = MultiSelectField(max_length=100,
                                       choices=MARKET_OPTIONS)
    website_url = models.URLField(max_length=200, null=True, blank=True)

    PURCHASING_CATEGORIES = (
        ('jewellery', 'Jewellery'),
        ('leather_accessories', 'Leather Accessories'),
        ('blankets', 'Blankets'),
        ('knitted_accessories', 'Knitted Accessories'),
        ('clothing', 'Clothing'),
    )

    categories = MultiSelectField(max_length=100,
                                  choices=PURCHASING_CATEGORIES)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_stockist(sender, instance, created, **kwargs):
    """
    Create / Update stockist profile 
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users save the updated profile if any changes are made
    instance.userprofile.save()
