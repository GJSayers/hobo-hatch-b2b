from django.contrib import admin
from .models import Product, Category, Type, Ring, Clothing


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_sku',
        'product_name',
        'product_category',
        'product_type',
        'product_price',
        'rrp_price',
        'image',
    )
    ordering = ('product_sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'product_type',
    )

    ordering = ('friendly_name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'product_categories',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Ring)
admin.site.register(Clothing)
