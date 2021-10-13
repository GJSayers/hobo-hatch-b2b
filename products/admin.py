from django.contrib import admin
from .models import Product, ProductCategory, ProductType, Ring

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(Ring)
