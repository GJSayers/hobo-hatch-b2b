from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Category


def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    
    for item_id, item_data in bag.items():
       
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qtys = item_data[product_type]
        # total += item_data * product.product_price
        # total_items += item_data
        bag_items.append({ 
            'item_id': item_id,
            'product_type': str(product.product_type),
            'size_qty': size_qtys,
            'product': product,
        })
        print("bag items", bag_items)

    # grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        # 'delivery': delivery,
        # 'grand_total': grand_total,
    }

    return context
