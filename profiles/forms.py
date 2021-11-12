from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'country', 'purchasing_currency',
                   'stockist_channel', 'stockist_market',
                   'categories', 'accounts_email', )
                  # not possible to enter due to bug / 'delivery_date',
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'buyer_name': 'Buyer Name',
            'stockist': 'Store Name',
            'buyer_phone': 'Buyer Name',
            'buyer_email': 'Buyer Email Address',
            'accounts_phone': 'Accounts Phone Number',
            # 'accounts_email': 'Accounts Email Address',
            'address_1': 'Address Line 1',
            'address_2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county_or_state': 'County or State',
            'postcode': 'Postcode / Zipcode',
            'website_url': 'Website',
            
        }

        # not possible to enter due to bug / 'delivery_date': 'Preferred Date of Delivery',

        self.fields['buyer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False