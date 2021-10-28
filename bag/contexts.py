from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Category


def bag_contents(request):

    bag_items = []
    total = 0
    total_items = 0
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    # ring = Product.product_type(3)
    # clothing = Product.product_type(5,6,7,8,9,10)
    # universal = Product.one_size
    
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.product_price
            total_items += item_data
            bag_items.append({ 
                'item_id': item_id,
                'type': product.product_type,
                'quantity_l': item_data,
                'quantity_n': item_data,
                'quantity_p': item_data,
                'quantity_s': item_data,
                'quantity_u': item_data,
                'quantity': item_data,
                'product': product,
            })
            print("bag items", bag.items())
            print("bag_contents", item_data)

    grand_total = delivery + total
    total_items = total_items

    context = {
        #'item_id': item_id,
        'bag_items': bag_items,
        'total': total,
        'total_items': total_items,
        'delivery': delivery,
        'grand_total': grand_total,
        # 'ring': ring,
        # 'clothing': clothing,
        # 'universal': universal,
    }

    return context
