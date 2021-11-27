from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'purchasing_currency', 'stockist_channel',
                   'categories', 'stockist_market')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'buyer_name': 'Buyer Name',
            'stockist': 'Store Name',
            'buyer_phone': 'Buyer Phone',
            'buyer_email': 'Buyer Email Address',
            'accounts_phone': 'Accounts Phone Number',
            'accounts_email': 'Accounts Email Address',
            'address_1': 'Address Line 1',
            'address_2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county_or_state': 'County or State',
            'country': 'Country',
            'postcode': 'Postcode / Zipcode',
            'website_url': 'Website',

        }

        self.fields['buyer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
