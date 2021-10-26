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
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.product_price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for sizes, (quantity_l, quantity_n, quantity_p, quantity_s,
                        quantity_u) in item_data['ring_items'].items():
                total += (quantity_l and quantity_n and quantity_p
                          and quantity_s and quantity_u) * product.product_price
                product_count += (quantity_l and quantity_n and quantity_p
                                  and quantity_s or quantity_u)
                bag_items.append({
                    'item_id': item_id,
                    'ring_items': {sizes:
                                   {['quantity_l']: quantity_l,
                                    ['quantity_n']: quantity_n,
                                    ['quantity_p']: quantity_p,
                                    ['quantity_s']: quantity_s,
                                    ['quantity_u']: quantity_u
                                    }
                                   },
                    'product': product,
                })

    grand_total = delivery + total
    total_items = product_count

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'total_items': total_items,
    }

    return context
