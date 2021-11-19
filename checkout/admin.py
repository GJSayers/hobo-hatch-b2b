from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number',
              'buyer_name', 'stockist', 'delivery_date',
              'buyer_phone', 'buyer_email',
              'accounts_phone', 'accounts_email', 'address_1',
              'address_2', 'town_or_city',
              'county_or_state', 'postcode',
              'country',
              'delivery_cost', 'order_total',
              'grand_total',)

    list_display = ('order_number', 'date',
                    'buyer_name', 'stockist', 'delivery_date',
                    'delivery_cost', 'order_total',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
