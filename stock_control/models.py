from django.db import models

from products.models import Product, Category, Type
from checkout.models import Order


class Stock(models.Model):
    image = models.ForeignKey(Product.image, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product.product_name,
                                     on_delete=models.CASCADE)
    stock_in = models.DateTimeField(null=True,
                                    blank=True)
    cost = models.DecimalField(null=True, blank=True, max_digits=10,
                               decimal_places=2)
    rrp_price = models.ForeignKey(Product.rrp_price, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    related_orders = models.ForeignKey(Order.order_number,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_name} \
                quantity {self.quantity}'
