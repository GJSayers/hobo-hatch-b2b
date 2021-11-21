from django import forms
from .models import Product, Category, Type


class ProductFrom(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_name = [(
            c.id, c.get_friendly_name()) for c in categories]
        types = Type.objects.all()
        type_friendly_name = [(
            t.id, t.get_friendly_name()) for t in types]

        self.fields['category'].choices = category_friendly_name
        self.fields['type'].choices = type_friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-fields'


