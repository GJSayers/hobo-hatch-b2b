from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_type = str(product.product_type)
        size_qty = item_data[product_type]
        print(size_qty)
        
        size_names = size_qty.keys()
        qty = size_qty.values()
        print("qty", qty)
        # total += size_qty * product.product_price
        bag_items.append({ 
                                'item_id': item_id,
                                'product_type': str(product.product_type),
                                'qty': qty,
                                'size_names': size_names,
                                'product': product,
                            })
        print("bag items", bag_items)

    grand_total = delivery

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
