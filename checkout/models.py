import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import Stockist


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    buyer_name = models.CharField(max_length=60, null=False, blank=False)
    stockist = models.ForeignKey(Stockist,
                                 null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='order')
    buyer_phone = models.CharField(max_length=20, null=False, blank=False)
    buyer_email = models.CharField(max_length=200, null=False, blank=False)
    accounts_phone = models.CharField(max_length=20, null=False, blank=False)
    address_1 = models.CharField(max_length=100, null=False, blank=False)
    address_2 = models.CharField(max_length=100, null=False, blank=True)
    town_or_city = models.CharField(max_length=35, null=False, blank=False)
    county_or_state = models.CharField(max_length=35, null=False, blank=False)
    postcode = models.CharField(max_length=12, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=False,
                                editable=False, blank=False)
    delivery_date = models.DateField(auto_now_add=True,
                                     editable=True, blank=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=12, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitem.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.delivery_cost = settings.STANDARD_DELIVERY
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, 
                              related_name='lineitem')
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)
    # add and update model with correct qty / size reference once bug sorted in add to bag
    lineitem_qty = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.product_price * self.lineitem_qty
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.product_sku} on order {self.order.order_number}'
