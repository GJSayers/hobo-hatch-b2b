from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        readonly_fields = 'stockist'
        fields = ('buyer_name', 'buyer_phone', 'stockist',
                  'buyer_email', 'accounts_phone', 'accounts_email',
                  'delivery_date',
                  'address_1', 'address_2', 'town_or_city',
                  'county_or_state', 'postcode',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'stockist': 'Store Name',
            'buyer_name': 'Buyer Name',
            'buyer_phone': 'Buyer Phone',
            'buyer_email': 'Buyer Email Address',
            'accounts_phone': 'Accounts Phone Number',
            'accounts_email': 'Accounts Email Address',
            'delivery_date': 'Required delivery date',
            'address_1': 'Address Line 1',
            'address_2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county_or_state': 'County or State',
            'country': 'Country',
            'postcode': 'Postcode / Zipcode',
        }

        self.fields['buyer_name'].widget.attrs['autofocus'] = True
        self.fields['delivery_date'].widget = forms.widgets.DateInput(
             attrs={'type': 'date'})
        self.fields['stockist'].widget.attrs['disabled'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
