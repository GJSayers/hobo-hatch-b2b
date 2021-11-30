from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'stockist',
        'buyer_name',
        'buyer_phone',
        'buyer_email',
        'accounts_phone',
        'accounts_email',
        'address_1',
        'address_2',
        'town_or_city',
        'county_or_state',
        'postcode',
        'country',
        'purchasing_currency',
        'stockist_channel',
        'stockist_market',
        'website_url',
        'categories',
    )
    ordering = ('stockist',)


admin.site.register(UserProfile, UserProfileAdmin)
