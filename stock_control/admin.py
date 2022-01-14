from django.contrib import admin
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'category',
        'type',
        'cost',
        'rrp_price',
        'image',
    )
    ordering = ('product_sku',)


admin.site.register(Stock)
