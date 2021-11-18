from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qty = item_data[product_type]
        size_items = size_qty.items()
        size_names = size_qty.keys()
        qty = size_qty.values()
        line_qty = int(sum(qty))
        line_total = line_qty * product.product_price
        bag_items.append({
                                'item_id': item_id,
                                'product_type': str(product.product_type),
                                'qty': qty,
                                'size_items': size_items,
                                'size_names': size_names,
                                'line_qty': line_qty,
                                'line_total': line_total,
                                'product': product,
                            })

    grand_total = delivery

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
