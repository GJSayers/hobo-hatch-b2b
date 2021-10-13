from django.contrib import admin
from .models import Product, ProductCategory, ProductType, Ring, Clothing


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


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'product_type',
    )

    ordering = ('friendly_name',)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'product_categories',
    )

    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Ring)
admin.site.register(Clothing)
